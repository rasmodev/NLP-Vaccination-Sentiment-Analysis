docker build -t gradio-app -f src/Dockerfile .
docker images
docker run -p 7860:7860 --name gradio_app image_id
docker ps