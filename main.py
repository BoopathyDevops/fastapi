from fastapi import FastAPI

app = FastAPI()
print("Hello, World!")


@app.get("/")
def read_root():
    return {"message": "Render ran successfully, and CI/CD has been implemented."}

@app.get("/api")
def read_root():
    return {"message": "The jenkins ran successfully, and CI/CD has been implemented."}
