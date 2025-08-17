https://www.kaggle.com/datasets/ashydv/advertising-dataset/data


# Docker Containerize Web Application

1. To create docker image of webapplication : `docker build -t docker_image_name_of_app .`
2. Running the build docker image i.e docker container : `docker run -p 8501:8501 docker_image_name_of_app` Then It will maps port 8501 on your host machine to port 8501 inside the container, allowing you to access the Streamlit app in your browser at `http://localhost:8501`
