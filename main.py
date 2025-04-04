from fastapi import FastAPI

app = FastAPI()
print("Hello, World!")


@app.get("/")
def read_root():
    return {"message": "The GitHub Action ran successfully, and CI/CD has been implemented."}