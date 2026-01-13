# Copyright (c) 2026 Kenny B (kennyb7322)
# Confidential and Proprietary (template).

FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml README.md LICENSE NOTICE CONFIDENTIALITY.md /app/
COPY src /app/src
COPY configs /app/configs

RUN pip install --no-cache-dir -e ".[dev]" || pip install --no-cache-dir -e .

ENV AGI_CONFIG=/app/configs/app.default.yaml
ENV AGI_WORKSPACE=/app/workspace

EXPOSE 8000
CMD ["python", "-m", "agi.cli", "serve", "--host", "0.0.0.0", "--port", "8000"]
