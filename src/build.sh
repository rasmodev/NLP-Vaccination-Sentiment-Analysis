docker build -t gradio-app -f src/Dockerfile .
docker images
docker run -p 7860:7860 --name gradio_app 8ce33b2898e0
docker ps