#!/bin/bash
alembic upgrade head  # Run database migrations
uvicorn app.main:app --host 0.0.0.0 --port 8000  # Start FastAPI