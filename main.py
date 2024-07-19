from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import shortuuid

AND = "add"
MINUS = "minus"
DIV = "div"
MUL = "mul"
OPERAND = [AND, MINUS, DIV, MUL]

NOT_FOUND = "stack_id not found"

app = FastAPI()

stacks: dict[str, list[float]] = {}


class Value(BaseModel):
    value: float


@app.get("/rpn/op")
def list_all_the_operand():
    return {"operand": OPERAND}

@app.post("/rpn/op/{op}/stack/{stack_id}")
def apply_an_operand_to_a_stack(op: str, stack_id: str):
    if stack_id not in stacks.keys():
        raise HTTPException(status_code=404, detail=NOT_FOUND)
    if op not in OPERAND:
        raise HTTPException(status_code=400, detail="Wrong operand")
    if len(stacks[stack_id]) < 2:
        raise HTTPException(status_code=400, detail="Not enough stack")
    if stacks[stack_id][-1] == 0 and op == DIV:
        raise HTTPException(status_code=403, detail="Division by 0 impossible")
    
    item2, item1 = float(stacks[stack_id].pop()), float(stacks[stack_id].pop())
    if op == AND:
        stacks[stack_id].append(item1 + item2)
    if op == MINUS:
        stacks[stack_id].append(item1 - item2)
    if op == DIV:
        stacks[stack_id].append(item1 / item2)
    if op == MUL:
        stacks[stack_id].append(item1 * item2)
    return {"stack": stacks[stack_id]}

@app.post("/rpn/stack", status_code=status.HTTP_201_CREATED)
def create_a_new_stack():
    new_stack_id = shortuuid.uuid()
    stacks[new_stack_id] = []
    return {"new_stack_id": new_stack_id}

@app.get("/rpn/stack")
def list_the_available_stack():
    return {"stacks": stacks}

@app.delete("/rpn/op/{stack_id}")
def delete_a_stack(stack_id: str):
    if stack_id not in stacks.keys():
        raise HTTPException(status_code=404, detail=NOT_FOUND)
    del stacks[stack_id]
    return {"stacks": stacks}

@app.post("/rpn/stack/{stack_id}")
def push_a_new_value_to_a_stack(stack_id: str, value: Value):
    if stack_id not in stacks.keys():
        raise HTTPException(status_code=404, detail=NOT_FOUND)
    stacks[stack_id].append(value.value)
    return {"stack": stacks[stack_id]}

@app.get("/rpn/{stack_id}")
def get_a_stack(stack_id: str):
    if stack_id not in stacks.keys():
        raise HTTPException(status_code=404, detail=NOT_FOUND)
    return {"stack": stacks[stack_id]}