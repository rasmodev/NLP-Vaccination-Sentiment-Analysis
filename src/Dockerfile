# Use the official Python 3.11.3 image as the base image.
FROM python:3.11.3

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt from the home folder to the working directory in the container
COPY ../requirements.txt .

# Install the needed packages specified in the requirements.txt file
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose a port for the Gradio app to run on (the same port as the Gradio app)
EXPOSE 7860

# Command to run the Gradio app when the container starts
CMD ["python", "src/app.py"]