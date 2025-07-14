#docker build -t multimedia-rag-app .
docker run -p 80:8501 --env-file .env multimedia-rag-app
#For running on server
#echo "OPENAI_API_KEY=your_actual_api_key" > .env
sudo docker run -p 80:8501 -e OPENAI_API_KEY=your_actual_api_key_here multimedia-rag-app