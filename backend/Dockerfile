# Base image: official Python 3.12 slim variant (smaller than the full image)
FROM python:3.12-slim

# Set the working directory inside the container
# All subsequent commands run from here
WORKDIR /app

# Copy only requirements first so Docker can cache this layer
# If requirements.txt hasn't changed, pip install is skipped on rebuild
COPY requirements.txt .

# Install dependencies — no cache keeps the image smaller
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend source code into the container
COPY . .

# Document that the app listens on port 8000 (uvicorn default)
EXPOSE 8000

# Start the FastAPI app with uvicorn
# --host 0.0.0.0 makes it reachable from outside the container
# --reload watches for file changes (useful during development)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
