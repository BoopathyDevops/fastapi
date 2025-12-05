# from fastapi import FastAPI

# app = FastAPI()
# print("Hello, World!")


# @app.get("/")
# def read_root():
#     return {"message": "Render ran successfully, and CI/CD has been implemented."}

# @app.get("/api")
# def read_root():
#     return {"message": "The jenkins ran successfully, and CI/CD has been implemented."}
# from fastapi import FastAPI
# from azure.functions import HttpRequest, HttpResponse
# from fastapi.responses import JSONResponse
# import azure.functions as func
# from fastapi.middleware.cors import CORSMiddleware
# from mangum import Mangum

# app = FastAPI()
# handler = Mangum(app)  # makes FastAPI compatible

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )

# @app.get("/api")
# def root():
#     return {"message": "FastAPI running in Azure Function serverless"}

# def main(req: HttpRequest) -> HttpResponse:
#     response = handler({"body": req.get_body(), "method": req.method, "path": req.url.path}, {})
#     return JSONResponse(response["body"])
# main.py
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from azure_functions_fastapi import AzureFunctionsFastAPI

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )

# @app.get("/api")
# def root():
#     return {"message": "FastAPI running in Azure Function serverless"}

# # Wrap FastAPI app for Azure Function
# main = AzureFunctionsFastAPI(app)
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import azure.functions as func

app = FastAPI()

@app.get("/api")
def root():
    return {"message": "FastAPI running in Azure Function serverless"}

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Simple routing for /api
    if req.method == "GET" and req.url.path.endswith("/api"):
        return func.HttpResponse(
            content='{"message": "FastAPI running"}',
            status_code=200,
            mimetype="application/json"
        )
    return func.HttpResponse("Not Found", status_code=404)
