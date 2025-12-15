# Stage 1: Builder
FROM python:3.13-slim AS builder
# Install uv (see https://docs.astral.sh/uv/guides/integration/docker/#installing-uv)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/bin/uv
WORKDIR /app
COPY pyproject.toml uv.lock ./
# Use cache mount for faster rebuilds
RUN --mount=type=cache,target=/root/.cache/uv \
    uv venv && \
    uv sync && \
    uv pip install --system --no-cache-dir .

# Stage 2: Final
FROM python:3.13-slim
WORKDIR /app
# Copy the installed packages from the builder stage
COPY --from=builder /app/.venv /usr/src/app/.venv
# Activate the virtual environment implicitly (adjust according to base image)
ENV PATH="/usr/src/app/.venv/bin:$PATH"
COPY . .
# Your entrypoint and command here (e.g., CMD ["gunicorn", ...])
CMD ["python", "manage.py", "runserver"]
