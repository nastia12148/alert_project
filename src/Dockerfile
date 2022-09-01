
# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app

ADD alert_system.py /
ADD requirements.txt /
ADD data/data.csv /
# Copy the current directory contents into the container at /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Define environment variable

# Run app.py when the container launches
CMD ["python","alert_system.py"]