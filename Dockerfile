FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install system dependencies required for some Python packages (like opencv or pandas)
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Make the startup script executable
RUN chmod +x start.sh

# Expose the port Streamlit uses
EXPOSE 8501

# Healthcheck to ensure the container is running properly
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Command to run both FastAPI and Streamlit
CMD ["./start.sh"]