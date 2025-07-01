# 🤖 AI Trading Bot with Dashboard

A modular, AI-powered trading bot with a built-in web dashboard for live monitoring, backtesting, and strategy visualization.

## 🚀 Features

- 📈 Live and simulated trading via Alpaca API
- 🧠 Strategy generation powered by LLMs (OpenAI, Mistral, etc.)
- 📊 Streamlit dashboard for:
  - Portfolio monitoring
  - Backtest performance
  - Trade logs & metrics
- 📦 Modular structure for strategies, data ingestion, and model management
- 🔐 Supports .env-based secrets management

---

## 🗂️ Project Structure
# 🧠 Multimedia RAG AI Application

An AI-powered Retrieval-Augmented Generation (RAG) app that can ingest and analyze **text**, **PDF**, **JSON**, **CSV**, **images**, **audio**, and **video** files. Built using Streamlit, LangChain, ChromaDB, and Whisper with support for OCR, image captioning, object detection, and multimodal search.

---

## 🚀 Features

- 🔍 **Multimodal file support**: PDF, text, JSON, CSV, JPEG, PNG, MP4, MP3, WAV
- 🧠 **RAG with LLMs**: Uses OpenAI or local LLMs via LangChain
- 🖼️ **Image OCR**, **captioning**, and **YOLOv8-based object detection**
- 🎧 **Audio & Video transcription** via OpenAI Whisper
- 🗄️ **Embeddings & retrieval** using ChromaDB
- 📊 Streamlit-based UI for interactive analysis
- 🔒 .env-based secure API key loading

---

## 📁 Folder Structure

```
multimedia_rag_app/
│
├── app.py                  # Streamlit entrypoint
├── requirements.txt        # Python dependencies
├── Dockerfile              # For containerization
├── .env                    # API keys and configs
├── .gitignore              # Git exclusions
│
├── utils/
│   ├── ocr.py              # OCR text extraction
│   ├── audio.py            # Audio transcription
│   ├── video.py            # Video extraction + audio handling
│   ├── embeddings.py       # Embedding and vectorstore logic
│   ├── captioning.py       # Image caption generation
│   └── object_detection.py # YOLOv8 object detection
│
├── retriever.py            # RAG logic with LangChain
├── ingest.py               # Ingestion and processing
├── vectorstore/            # ChromaDB persistent storage
```

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourname/multimedia_rag_app.git
cd multimedia_rag_app
```

### 2. Create virtual environment

```bash
python3.11 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Add environment variables

Create a `.env` file with your keys:

```env
OPENAI_API_KEY=your_key_here
```

---

## ▶️ Run the app

```bash
streamlit run app.py
```

---

## 🐳 Docker Support

Build and run with Docker:

```bash
docker build -t multimedia-rag-app .
docker run -p 8501:8501 --env-file .env multimedia-rag-app
```

---

## ☁️ Deployment Options

- AWS EC2 or EC2 Spot (t3.small/t3.medium recommended)
- ECS or EKS for scalable infrastructure
- Netlify not supported (no Python backend)

---

## 📌 Notes

- FFmpeg is required for audio/video processing.
- Tesseract OCR should be installed and available in PATH.
- Local LLM support (e.g., via Ollama) is pluggable.
- Bounding box visualizations available for YOLO.

---

## 📜 License

MIT

---

## 🙋‍♂️ Author

Viplav Fauzdar — [GitHub](https://github.com/viplavfauzdar) | [LinkedIn](https://linkedin.com/in/viplavfauzdar)