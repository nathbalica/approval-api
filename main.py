from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4
import uvicorn

app = FastAPI()

# Simula um "banco de dados" em memória
approvals = {}

class ApprovalRequest(BaseModel):
    message: str

class ApprovalResponse(BaseModel):
    id: str
    status: str

@app.post("/approval-request", response_model=ApprovalResponse)
def create_approval_request(request: ApprovalRequest):
    approval_id = str(uuid4())
    approvals[approval_id] = "pending"
    return {"id": approval_id, "status": "pending"}

@app.post("/approval-response/{approval_id}/{action}")
def update_approval_status(approval_id: str, action: str):
    if approval_id not in approvals:
        raise HTTPException(status_code=404, detail="Approval ID not found")
    
    if action not in ["approve", "reject"]:
        raise HTTPException(status_code=400, detail="Invalid action")

    approvals[approval_id] = action
    return {"id": approval_id, "status": action}

@app.get("/approval-status/{approval_id}", response_model=ApprovalResponse)
def get_approval_status(approval_id: str):
    if approval_id not in approvals:
        raise HTTPException(status_code=404, detail="Approval ID not found")
    
    return {"id": approval_id, "status": approvals[approval_id]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)
