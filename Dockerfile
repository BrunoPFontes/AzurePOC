# Use an official Python runtime as a parent image
#FROM python:3.12.1
FROM python:3.8-slim


# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in dependencies.txt
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r dependencies.txt

# Define environment variable
ENV ROBOT_OPTIONS="-d /usr/src/app/reports"

# Run script.py when the container launches
CMD ["robot", "${ROBOT_OPTIONS}", "tests"]
