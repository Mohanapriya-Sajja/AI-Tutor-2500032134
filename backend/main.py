from fastapi import FastAPI

klu = FastAPI(title="AI Tutor",
              description="AI Tutor Pbl Project",
              version="1.0.0")

@klu.get("/")
def home():
    return {"message":"Welcome to AI_Tutor project"}

@klu.get("/demo")

def demo():
    return{"meassage":"KL University"}

@klu.get("/askquestion")
def ask():
    return{"message":"What is LLM?", "Answer":"Large Language Model"}

@klu.get("/student")
def student():
    return{"id":"1", "Name":"John Doe", "gender":"male", "course":"DSA"}  

@klu.get("/students")
def getstudents():
    return[{"id":"1", "Name":"John Doe", "gender":"male", "course":"DSA"},
           {"id":"2", "Name":"seetha", "gender":"female", "course":"AI"},
           {"id":"3", "Name":"klu", "gender":"male", "course":"ML"}]


