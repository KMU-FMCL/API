# main.py
import os
import importlib
from fastapi import FastAPI, Request, HTTPException, Depends
from pydantic import BaseModel
from typing import List

app = FastAPI()
MODULES_DIR = "/app/modules"

import sqlite3
DB_PATH = "/app/mydb.sqlite"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS tokens (
    token TEXT PRIMARY KEY,
    description TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS usage_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    token TEXT,
    endpoint TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()
conn.close()

class DataInput(BaseModel):
    data_list: List[float]
    token: str


def get_valid_token(token: str):
    # sqlite3에서 토큰 검사
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT token FROM tokens WHERE token=?", (token,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=401, detail="Invalid Token")
    return token


def log_usage(token: str, endpoint: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usage_logs (token, endpoint) VALUES (?, ?)", (token, endpoint))
    conn.commit()
    conn.close()


import time
from datetime import datetime, timedelta

RATE_LIMIT = 10
WINDOW_IN_SECONDS = 3600


def check_rate_limit(token: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    one_hour_ago = datetime.utcnow() - timedelta(seconds=WINDOW_IN_SECONDS)
    cursor.execute("""
        SELECT COUNT(*) FROM usage_logs
         WHERE token = ?
           AND timestamp > ?
    """, (token, one_hour_ago))
    count = cursor.fetchone()[0]
    conn.close()

    if count >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")


def load_gpu_module():
    for file in os.listdir(MODULES_DIR):
        if file.endswith(".py"):
            module_name = file[:-3]
            full_module_path = f"modules.{module_name}"
            yield importlib.import_module(full_module_path)


@app.post("/process")
async def process_data(input_data: DataInput):
    token = get_valid_token(input_data.token)
    check_rate_limit(token)

    for m in load_gpu_module():
        if hasattr(m, "gpu_sum_of_squares"):
            result = m.gpu_sum_of_squares(input_data.data_list)
            log_usage(token, "/process")

            return {"result": result}

    raise HTTPException(status_code=404, detail="No suitable module found")
