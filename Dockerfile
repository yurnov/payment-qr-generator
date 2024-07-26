FROM python:3.12-slim

LABEL org.opencontainers.image.source = "https://github.com/yurnov/payment-qr-generator" \
      org.opencontainers.image.authors = "Yuriy Novostavskiy" \
      org.opencontainers.image.licenses = "MIT" \
      org.opencontainers.image.title = "Payment QR Generator"

RUN --mount=type=bind,source=./app/requirements.txt,target=/tmp/requirements.txt \
      mkdir -p /output && \
      python -m pip install --no-cache-dir -r /tmp/requirements.txt

COPY app /app

ENTRYPOINT [ "python", "/app/qrgen.py" ]
