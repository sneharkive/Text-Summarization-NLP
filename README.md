# Text-Summarization-NLP

An end-to-end NLP application that summarizes long dialogues into concise text using the **Google Pegasus** model. This project features a modular data science pipeline, automated logging, and a FastAPI web interface, fully containerized with Docker for seamless cloud deployment.

**🚀 Live Link:** [https://text-summarization-nlp.onrender.com](https://text-summarization-nlp.onrender.com)

---


## 🛠 Tech Stack

* **Core Model:** `google/pegasus-cnn_dailymail`
* **Framework:** FastAPI
* **NLP Libraries:** Hugging Face (Transformers, Datasets), SacreBleu, Rouge_score
* **Infrastructure:** Docker, GitHub Actions (CI/CD)
* **Configuration:** YAML, Python-Box, Ensure

---

## 🏗 Project Structure

The project follows a modular architecture to separate research, configuration, and production logic:

```text
├── research/               # Jupyter notebooks for experimentation
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_validation.ipynb
│   ├── 03_data_transformation.ipynb
│   ├── 04_model_trainer.ipynb
│   └── 05_Model_evaluation.ipynb
├── src/textSummarizer/     # Main production source code
│   ├── components/         # Modular pipeline steps (Ingestion, Trainer, etc.)
│   ├── config/             # Configuration management logic
│   ├── pipeline/           # Training and Prediction orchestration
│   ├── entity/             # Data classes for configuration
│   ├── constants/          # Project-wide constants (file paths)
│   ├── logging/            # Custom logging setup
│   └── utils/              # Reusable helper functions
├── config/                 # YAML files for path and URL configurations
├── templates/              # HTML templates for the web app
├── app.py                  # FastAPI entry point
├── main.py                 # Training pipeline entry point
├── Dockerfile              # Containerization script
├── requirements.txt        # Project dependencies
├── setup.py                # Local package installation
└── params.yaml             # Model hyperparameters

```

---

## 📈 Pipeline Visualization

### 🛠 Modular Workflow

The project is structured around a 5-stage automated pipeline. Each stage follows the design pattern: **Configuration  Entity  Component  Pipeline**.

| Stage | Description | Key Component |
| --- | --- | --- |
| **01. Data Ingestion** | Downloads dataset from remote URL and extracts it to `artifacts/`. | `DataIngestion` |
| **02. Data Validation** | Checks if required files (`train`, `test`, `validation`) exist. | `DataValidation` |
| **03. Data Transformation** | Tokenizes dialogue and summaries using Pegasus API. | `DataTransformation` |
| **04. Model Training** | Fine-tunes the model on the SAMSum dataset. | `ModelTrainer` |
| **05. Model Evaluation** | Calculates ROUGE metrics to verify summary quality. | `ModelEvaluation` |

---

### 🔄 Prediction Pipeline

When a user interacts with the app, the following inference flow is triggered:

1. **User Input:** Receives dialogue via the FastAPI web UI.
2. **Preprocessing:** Tokenizes the text with a `"summarize: "` prefix.
3. **Model Inference:** Fine-tuned Pegasus model generates summary IDs.
4. **Decoding:** Converts numerical IDs back into human-readable text.

---

## 🚀 Getting Started

### 1. Environment Setup

```bash
conda create -n summary python=3.8 -y
conda activate summary
pip install -r requirements.txt

```

### 2. Run Training Pipeline

To execute all stages from ingestion to evaluation:

```bash
python main.py

```

### 3. Start the Web App

```bash
uvicorn app:app --reload

```

Access the UI at `http://localhost:8080`.

---

## 🐳 Dockerization & Deployment

### Build and Run Locally

```bash
docker build -t text-summarizer .
docker run -p 8080:8080 text-summarizer

```

### Deploy to Render

1. Connect your GitHub repository to [Render](https://render.com/).
2. Select **Environment: Docker**.
3. Add the `PORT` environment variable (default: `8080`).
4. **Note:** Ensure the instance has at least **4GB RAM** to load the Pegasus model.

---

## 📊 Model Training Parameters

Configuration in `params.yaml`:

* **Epochs:** 1
* **Batch Size:** 1
* **Warmup Steps:** 500
* **Weight Decay:** 0.01

---



---

## 🖥 Usage

Once the application is running, you can interact with the summarizer through a clean web interface.

### 1. Web Interface

Access the app at `http://localhost:8080`. You will see a simple text area to input your dialogue.

### 2. Steps to Summarize:

* **Enter Text**: Paste a long conversation or dialogue into the "Enter text to summarize..." field.
* **Submit**: Click the **Summarize** button.
* **Result**: The model will process the input using the fine-tuned Pegasus pipeline and display the concise summary in the results box below.

### 3. API Endpoints

If you wish to interact with the service programmatically, FastAPI provides automatic documentation:

* **Swagger UI**: `http://localhost:8080/docs`
* **Redoc**: `http://localhost:8080/redoc`

---

Here is the **Pipeline Visualization** and workflow details for your `README.md`. This section explains how your modular code moves from raw data to a deployed API.

---

## 📈 Pipeline Visualization

### 🛠 Modular Workflow

The project is structured around a 5-stage automated pipeline. Each stage is independent, modular, and follows a consistent design pattern: **Configuration  Entity  Component  Pipeline**.

| Stage | Description | Key Component |
| --- | --- | --- |
| **01. Data Ingestion** | Downloads the dataset from a remote URL and extracts it into the `artifacts/` folder. | `DataIngestion` |
| **02. Data Validation** | Checks if all required files (`train`, `test`, `validation`) exist before processing. | `DataValidation` |
| **03. Data Transformation** | Tokenizes the dialogue and summaries using the Pegasus tokenizer. | `DataTransformation` |
| **04. Model Training** | Fine-tunes the `google/pegasus-cnn_dailymail` model on the SAMSum dataset. | `ModelTrainer` |
| **05. Model Evaluation** | Calculates ROUGE metrics to verify the quality of the generated summaries. | `ModelEvaluation` |

---

### 🔄 Inference Pipeline (Prediction)

When a user interacts with the Web UI or API, the following flow is triggered:

1. **User Input:** A dialogue string is sent via the FastAPI interface.
2. **Preprocessing:** The input is prefixed with `"summarize: "` and tokenized.
3. **Model Inference:** The fine-tuned Pegasus model generates summary IDs using beam search.
4. **Decoding:** The tokenizer converts numerical IDs back into human-readable text.
5. **Output:** The summary is displayed on the UI or returned as a JSON response.

---

### ⚙️ CI/CD & Deployment Architecture

This project uses Docker to ensure the pipeline runs identically on your local machine and on Render.

* **GitHub Actions:** Automatically builds the Docker image on every push to the `main` branch.
* **Docker Container:** Packages the code, fine-tuned model weights, and dependencies.
* **Cloud Platform (Render):** Hosts the containerized FastAPI app and exposes it via a public URL.


## 📝 License

This project is licensed under the [MIT License](https://www.google.com/search?q=LICENSE).

**Author:** Sneha Roy

**Email:** sneharoy90737@gmail.com


