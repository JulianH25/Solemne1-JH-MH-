FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
COPY uv.lock .
COPY main.py .

RUN pip install uv
RUN uv sync --frozen
RUN uv run playwright install chromium
RUN uv run playwright install-deps chromium

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]