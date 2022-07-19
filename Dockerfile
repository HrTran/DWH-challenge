# User an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD ./solution/ /app/solution
ADD ./data/ /app/data

RUN pip install -r solution/requirements.txt

CMD ["python", "solution/app.py"]
