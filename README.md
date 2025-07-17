# 🧠 LLM FAQ Chatbot (Fullstack + CPU-only + Kubernetes Ready)

This project is a fullstack chatbot using a lightweight Q&A engine with FastAPI (backend) + HTML/JS (frontend), designed to run with CPU-only models, Docker, CI/CD, and Kubernetes on EC2 or local dev.

---

## 📦 Features

- ✅ FastAPI backend with `/ask` API
- ✅ HTML/JS frontend (no JS frameworks)
- ✅ Dockerized for deployment
- ✅ GitHub Actions CI/CD pipeline
- ✅ Kubernetes manifests included
- ✅ Runs on CPUs (no GPU required)

---

## 🚀 Getting Started (Local)

```bash
# Clone
git clone https://github.com/YOUR_USERNAME/llm-faq-bot.git
cd llm-faq-bot

# Set up virtualenv
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload
```

Open: http://127.0.0.1:8000

---

## 🐳 Docker

```bash
docker build -t llm-faq-bot .
docker run -p 8000:8000 llm-faq-bot
```

---

## ☸️ Kubernetes Deployment

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

---

## 🧪 Example API Call

```bash
curl -X POST http://localhost:8000/ask \
-H "Content-Type: application/json" \
-d '{"question": "what is kubernetes?"}'
```

---

## 🌐 Frontend UI

Accessible at `/`:

- Enter a question
- View the answer returned by the backend

---

## 🧠 LLM Options

- ✅ Default: uses `qa_pairs.json` lookup
- 🔁 Replace with `llama-cpp-python` for real model
- 🔁 Or use OpenAI `gpt-3.5-turbo` via API call

---

## 🔄 GitHub Actions CI/CD

`.github/workflows/deploy.yml` is ready to:

- Build Docker image
- Push to Docker Hub
- SSH into EC2 and trigger K8s deployment

Set GitHub Secrets:

- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`
- `EC2_IP`

---

## 📁 Structure

```
.
├── app/
│   ├── main.py
│   ├── model.py
│   ├── qa_pairs.json
│   └── static/index.html
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── .github/workflows/deploy.yml
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 📜 License

MIT License

---

## 🙌 Author

Built by [@YourGitHub](https://github.com/YOUR_USERNAME)
