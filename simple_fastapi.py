from fastapi import FastAPI

app = FastAPI()


@app.get("/login")
async def login():
    return {"LOGIN": "GET"}


@app.post("/login")
async def login():
    return {"LOGIN": "POST"}


@app.put("/login")
async def login():
    return {"LOGIN": "PUT"}


@app.patch("/login")
async def login():
    return {"LOGIN": "PATCH"}


@app.delete("/login")
async def login():
    return {"LOGIN": "DELETE"}
