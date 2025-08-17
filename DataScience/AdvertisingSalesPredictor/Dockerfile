# Use a slim Python image as the base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container, maintaining the directory structure
# This will copy the 'data', 'model', and 'research' folders, along with all other files.
COPY . .

# Expose the port on which Streamlit will run
EXPOSE 8501

# Command to run the Streamlit application.
# The entry point has been updated from 'app.py' to 'apps.py'
# to match your project structure.
CMD ["streamlit", "run", "apps.py", "--server.port=8501", "--server.address=0.0.0.0"]