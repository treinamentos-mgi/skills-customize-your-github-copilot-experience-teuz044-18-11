from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Study Tasks API")


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class TaskUpdate(BaseModel):
    completed: bool


class Task(TaskCreate):
    id: int


tasks: dict[int, Task] = {}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    # TODO: Retorne todas as tarefas armazenadas.
    raise NotImplementedError


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate):
    # TODO: Crie uma tarefa com um identificador único e armazene-a.
    raise NotImplementedError


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    # TODO: Retorne a tarefa ou lance HTTPException com status 404.
    raise NotImplementedError


@app.patch("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskUpdate):
    # TODO: Atualize o estado da tarefa ou lance HTTPException com status 404.
    raise NotImplementedError


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    # TODO: Remova a tarefa ou lance HTTPException com status 404.
    raise NotImplementedError


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)