FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --timeout=600 --retries=5 -r requirements.txt

COPY . .

RUN chmod +x start.sh

EXPOSE 8501

CMD ["./start.sh"]
