FROM python:3.10-slim

WORKDIR /app

COPY requirementsUI.txt .
RUN pip install --no-cache-dir --timeout=600 --retries=5 -r requirementsUI.txt

COPY . .

RUN chmod +x start.sh

EXPOSE 10000

CMD ["streamlit", "run", "app.py", "--server.port=10000", "--server.address=0.0.0.0"]
