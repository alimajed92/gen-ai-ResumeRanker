# Use an official Python runtime as a parent image
FROM python:3.11.7-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the .env file into the container
COPY .env .env

# Install any needed packages specified in requirements
RUN pip install --upgrade pip
RUN pip install -r requirements/requirements.txt
RUN pip install -r requirements/requirements-dev.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable
ENV NAME=ResumeRanker

# Run run.py when the container launches
CMD ["python", "run.py"]