from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return "Hello"

@app.get("/calculate/{operation}/{x}/{y}")
def calculateRoute(operation: str, x: int, y:int):
    return calculate(operation,x,y)


def calculate(operation, x,y):

    if operation == "Addition":
        return x+y

    if operation == "Subtraction":
        if x>y:
            return x-y
        else:
            return y-x

    elif operation == "Multiplication":
        return x*y

    elif operation == "Division":
        return x/y