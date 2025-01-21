# main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Define a request model
class CalculationRequest(BaseModel):
    a_list: list
    b_list: list


@app.post("/gpu_calculate")
async def calculate(request: CalculationRequest):
    from gpu_module import gpu_vector_addition  # Module import

    result = gpu_vector_addition(request.a_list, request.b_list)

    return {"result": result}


# Server start (devel)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
