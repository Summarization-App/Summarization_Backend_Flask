# Use the official Python image as a base image
FROM python

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# These environment variables are commonly set in Dockerfiles to configure Python's behavior within the Docker container. Here's what they mean:

# PYTHONDONTWRITEBYTECODE: When set to 1, this prevents Python from writing .pyc files to disk (bytecode files). Bytecode files are used to speed up the loading of Python modules, but they are not necessary in a containerized environment and can clutter the file system. Setting this environment variable to 1 disables bytecode generation.

# PYTHONUNBUFFERED: When set to 1, this disables Python's output buffering. By default, Python buffers stdout and stderr when they are not directed to a terminal. In a containerized environment where logs are often collected by a logging driver, buffering can delay the availability of log messages. Setting this environment variable to 1 ensures that Python's output streams are unbuffered, allowing logs to be immediately available.

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

RUN ls

ENV OPENAI_API_KEY 0

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application with Gunicorn
CMD ["gunicorn", "-c", "gunicorn_config.py", "wsgi:hostedApp"]