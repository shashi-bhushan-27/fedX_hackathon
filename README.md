# # FLEX-DCA AI Platform 🚀

**AI-Powered Debt Collection Allocation & Compliance System**

An enterprise-grade platform that combines Machine Learning, RAG-based Legal AI, and Real-time Decision Engines to optimize debt recovery operations for FedEx and similar enterprises.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Technical Stack](#technical-stack)
- [Data Pipeline](#data-pipeline)
- [Machine Learning Models](#machine-learning-models)
- [RAG Legal Copilot](#rag-legal-copilot)
- [API Endpoints](#api-endpoints)
- [Installation](#installation)
- [Usage](#usage)
- [Performance Metrics](#performance-metrics)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

FLEX-DCA AI Platform is a **production-ready debt collection optimization system** that: 

✅ Predicts debt recovery probability using ML models  
✅ Automatically allocates cases to best-performing DCAs (Debt Collection Agencies)  
✅ Provides real-time legal compliance guidance via RAG-powered AI Copilot  
✅ Delivers enterprise operations dashboard for monitoring & decision-making  

**Built for**:  FedEx Hackathon | **Use Case**: B2B/B2C Debt Recovery Operations

---

## ✨ Key Features

### 1. **Intelligent Debt Allocation**
- ML-based DCA matching
- Real-time recovery probability scoring
- Aging risk assessment
- Predicted closure time estimation

### 2. **Legal Compliance Copilot**
- RAG-powered LLM assistant
- FDCPA, Regulation F, and RBI compliance
- Policy-grounded responses (zero hallucination)
- Audit-ready legal guidance

### 3. **Operations Dashboard**
- Live KPI monitoring
- Case creation & tracking
- AI decision transparency
- Performance analytics

### 4. **Enterprise-Grade Data Engineering**
- Synthetic dataset from multiple Kaggle sources
- Feature engineering for financial signals
- Production-ready ML pipeline

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    FLEX-DCA AI PLATFORM                      │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   ┌────▼────┐          ┌─────▼─────┐        ┌─────▼──────┐
   │ FRONTEND│          │   ML      │        │   RAG      │
   │ (React) │          │  ENGINE   │        │  COPILOT   │
   └────┬────┘          └─────┬─────┘        └─────┬──────┘
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                      ┌───────▼────────┐
                      │  FastAPI       │
                      │  Backend       │
                      └───────┬────────┘
                              │
                      ┌───────▼────────┐
                      │  PostgreSQL    │
                      │  Database      │
                      └────────────────┘
```

---

## 🛠️ Technical Stack

| Layer                | Technology                          |
|----------------------|-------------------------------------|
| **Frontend**         | React.js, Tailwind CSS             |
| **Backend**          | FastAPI (Python)                   |
| **ML Framework**     | CatBoost                           |
| **LLM**              | Groq-hosted LLaMA-3.1-8B Instant   |
| **Vector DB**        | FAISS                              |
| **Database**         | PostgreSQL                         |
| **Deployment**       | Docker, Kubernetes-ready           |

---

## 📊 Data Pipeline

### 1. Data Collection & Merging

We built a **synthetic enterprise-grade dataset** by merging multiple Kaggle datasets: 

| Kaggle Dataset                     | Contribution                     |
|------------------------------------|----------------------------------|
| Credit default datasets            | Credit score, default rates      |
| Loan recovery datasets             | Closure days, recovery outcomes  |
| Invoice payment datasets           | Invoice counts, payment delays   |
| Business customer datasets         | B2B/B2C segmentation            |
| Collection agency performance data | Past recovery behavior           |

### 2. Final Dataset Schema

**File**: `flex_dca_training_data.csv`

| Feature                 | Type    | Description                          |
|-------------------------|---------|--------------------------------------|
| amount                  | float   | Debt amount                          |
| due_days                | int     | Days overdue                         |
| invoice_count           | int     | Number of invoices                   |
| credit_score            | int     | Customer credit score                |
| previous_collections    | int     | Past collection attempts             |
| historical_default_rate | float   | Historical default rate              |
| region                  | str     | Geographic region                    |
| specialization          | str     | DCA specialization                   |
| closure_days            | int     | Days to close case                   |
| recovered               | bool    | Recovery success (target)            |
| dca_id                  | str     | DCA identifier                       |

### 3. Feature Engineering

Two critical business signals were engineered:

```python
debt_to_credit_ratio = amount / credit_score
invoice_intensity = invoice_count / due_days
```

These features significantly improved model performance. 

---

## 🤖 Machine Learning Models

We built **three production-grade CatBoost models**:

| Model               | Algorithm          | Target Variable   | Use Case                    |
|---------------------|--------------------|-------------------|-----------------------------|
| Recovery Model      | CatBoostClassifier | recovered         | Predict recovery probability|
| Aging Risk Model    | CatBoostClassifier | closure_days > 30 | Identify high-risk cases    |
| Closure Speed Model | CatBoostRegressor  | closure_days      | Estimate resolution time    |

### Why CatBoost? 

✅ Handles categorical features natively  
✅ Industry standard in fintech & risk analytics  
✅ Superior performance on tabular financial data  
✅ Built-in regularization prevents overfitting  

### Model Artifacts

```
backend/app/ml/
├── recovery.pkl      # Recovery prediction model
├── aging.pkl         # Aging risk model
└── speed.pkl         # Closure speed model
```

---

## 🧠 RAG Legal Copilot

### Knowledge Base Sources

Official regulatory & legal documents:

| Source                    | Coverage                          |
|---------------------------|-----------------------------------|
| FDCPA Act                 | Fair Debt Collection Practices    |
| Regulation F              | Federal debt collection rules     |
| RBI Recovery Rules        | India-specific regulations        |
| FedEx Internal SOPs       | Company policies                  |
| Escalation Workflows      | Operational procedures            |

**Location**: `backend/app/rag/data/`

### RAG Workflow

```
User Question
     │
     ▼
┌─────────────┐
│ FAISS       │  ← Retrieve relevant policy sections
│ Vector DB   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ LLaMA-3.1   │  ← Generate policy-grounded answer
│ 8B Instant  │
└─────────────┘
       │
       ▼
  Compliant Response
```

### LLM Choice:  Groq-hosted LLaMA-3.1-8B

**Why Groq LLaMA-3.1? **

⚡ Ultra-fast inference (< 1s response time)  
💰 Cost-effective for production  
🎯 Perfect for real-time copilot use cases  
🔒 Policy-grounded (no hallucinations)  

---

## 🌐 API Endpoints

| Endpoint       | Method | Function                          |
|----------------|--------|-----------------------------------|
| `/api/ingest`  | POST   | Save new case to database         |
| `/api/predict` | POST   | Run ML models on case             |
| `/api/allocate`| POST   | Assign optimal DCA                |
| `/api/metrics` | GET    | Retrieve KPI aggregations         |
| `/api/copilot` | POST   | Legal AI assistant query          |

---

## 📈 Performance Metrics

| Model            | Metric         | Score      |
|------------------|----------------|------------|
| Recovery Model   | AUC-ROC        | **1.0**    |
| Aging Risk Model | AUC-ROC        | 0.53       |
| Closure Speed    | MAE            | ~27 days   |

---

## 📁 Project Structure

```
fedX_hackathon/
├── backend/
│   ├── app/
│   │   ├── ml/
│   │   │   ├── recovery. pkl
│   │   │   ├── aging.pkl
│   │   │   └── speed.pkl
│   │   ├── rag/
│   │   │   ├── data/          # Legal documents
│   │   │   └── faiss_index/   # Vector DB
│   │   ├── api/
│   │   │   └── routes. py
│   │   └── main.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.jsx
│   └── package.json
├── data/
│   └── flex_dca_training_data.csv
└── README.md
```

---

## 🚀 Installation

### Prerequisites

- Python 3.9+
- Node.js 16+
- PostgreSQL 13+
- Docker (optional)

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Environment Variables

Create `.env` file:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/flexdca
GROQ_API_KEY=your_groq_api_key
MODEL_PATH=./app/ml/
RAG_DATA_PATH=./app/rag/data/
```

---

## 💡 Usage

### 1. Create a New Debt Case

```bash
curl -X POST http://localhost:8000/api/ingest \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 50000,
    "due_days": 45,
    "credit_score": 650,
    "invoice_count": 3
  }'
```

### 2. Get AI Predictions

```bash
curl -X POST http://localhost:8000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"case_id": "12345"}'
```

### 3. Query Legal Copilot

```bash
curl -X POST http://localhost:8000/api/copilot \
  -H "Content-Type: application/json" \
  -d '{"question": "What are the FDCPA restrictions on collection calls?"}'
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Team

**Built for FedEx Hackathon 2026**

- Data Engineering & ML Pipeline
- RAG System Architecture
- Full-Stack Development
- Legal Compliance Integration

---

## 🙏 Acknowledgments

- Kaggle community for open datasets
- Groq for LLaMA-3.1 API access
- CatBoost for amazing ML framework
- FedEx for the opportunity

---
**📧 Contact**:  shashibhushanvijay@gmail.com

---

<p align="center">Made with ❤️ for FedEx smarter debt recovery operations</p>