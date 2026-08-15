from fastapi import FastAPI, HTTPException, Header
app = FastAPI(title="API Security BOLA Testbed")

@app.get("/api/v1/accounts/{account_id}")
def get_account(account_id: str):
    return {"status": "success", "account_id": account_id}
