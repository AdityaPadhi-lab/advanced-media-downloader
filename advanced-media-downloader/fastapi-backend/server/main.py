from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Task
from .schemas import TaskCreate, TaskOut
import os

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./dev.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.post("/api/tasks", status_code=201)
async def create_task(payload: TaskCreate):
    db = SessionLocal()
    t = Task(source_url=payload.source_url, status="pending")
    db.add(t)
    db.commit()
    db.refresh(t)
    db.close()
    return {"id": t.id}

@app.get("/api/tasks/pending")
async def pending_tasks():
    db = SessionLocal()
    rows = db.query(Task).filter(Task.status == "pending").limit(5).all()
    out = []
    for r in rows:
        out.append({"task_id": r.id, "source_url": r.source_url})
        r.status = "in_progress"
    db.commit()
    db.close()
    return out

@app.post("/api/tasks/{task_id}/complete")
async def task_complete(task_id: int, payload: dict):
    db = SessionLocal()
    t = db.query(Task).get(task_id)
    if not t:
        raise HTTPException(404)
    t.status = "done"
    t.result_path = payload.get("path")
    t.checksum = payload.get("checksum")
    db.commit()
    db.close()
    return {"ok": True}

@app.get("/api/tasks/{task_id}")
async def get_task(task_id: int):
    db = SessionLocal()
    t = db.query(Task).get(task_id)
    db.close()
    if not t:
        raise HTTPException(404)
    return TaskOut.from_orm(t)
