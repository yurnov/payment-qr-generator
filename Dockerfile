FROM python:3.12-slim

RUN mkdir -p /output && \
    pip install qrcode~=7.4

COPY app /app

ENTRYPOINT [ "python", "/app/qrgen.py" ]