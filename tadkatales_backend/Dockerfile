FROM python:3.12.2-slim-bullseye

# Set working directory
WORKDIR /usr/src/tadkatales_backend

# Install dependencies
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy entrypoint script and adjust permissions
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/tadkatales_backend/entrypoint.sh
RUN chmod +x /usr/src/tadkatales_backend/entrypoint.sh

# Copy the rest of the application code
COPY . .

# Run entrypoint script
ENTRYPOINT [ "/usr/src/tadkatales_backend/entrypoint.sh" ]

# Define the default command (commented out, uncomment if needed)
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
