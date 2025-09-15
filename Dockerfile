FROM python:3.13-slim

# Set working directory inside container
WORKDIR /app

# Copy the project
COPY . .

# command to run program
CMD ["python", "main.py"]