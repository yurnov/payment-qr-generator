FROM python:3.12-slim

LABEL org.opencontainers.image.source = "https://github.com/yurnov/payment-qr-generator" \
      org.opencontainers.image.authors = "Yuriy Novostavskiy" \
      org.opencontainers.image.licenses = "MIT" \
      org.opencontainers.image.title = "Payment QR Generator"

RUN mkdir -p /output && \
    pip install qrcode~=7.4

COPY app /app

ENTRYPOINT [ "python", "/app/qrgen.py" ]
