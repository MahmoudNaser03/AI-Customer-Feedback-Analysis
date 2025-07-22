# Customer Sentiment & Intent Classifier using LLMs

This project is a Customer Sentiment & Intent Classifier that leverages Large Language Models (LLMs) to analyze customer messages, classify their sentiment (positive, negative, neutral), and detect customer intent. It is designed to help customer service teams better understand and respond to customer needs at scale.

## Features
- **Sentiment Analysis:** Automatically classifies customer messages as positive, negative, or neutral.
- **Intent Detection:** Identifies the intent behind customer messages (e.g., complaint, inquiry, feedback, request).
- **LLM-Powered:** Utilizes state-of-the-art language models for high accuracy.
- **API Access:** Includes a Flask API for easy integration with other systems.
- **Batch & Single Message Processing:** Supports both single message and batch processing.
- **Docker Support:** Easily deployable using Docker.

## Project Structure
- `flask_api.py` — REST API for message classification
- `llm.py` — LLM integration and core classification logic
- `one_message_handler.py` — Handler for single message classification
- `prediction_test.py` — Test script for predictions
- `test.py` — Additional tests
- `customer_messages_20000_no_repeats.csv` — Large dataset of customer messages
- `messages.csv` — Sample messages
- `messages_classification.json` — Labeled data for training/testing
- `requirements.txt` — Python dependencies
- `docker_app/` — Docker deployment files

## Getting Started

### Prerequisites
- Python 3.8+
- pip
- (Optional) Docker

### Installation
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd llm_cust_service
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running the API
To start the Flask API:
```sh
python flask_api.py
```
The API will be available at `http://localhost:5000`.

### Using Docker
To build and run the app with Docker:
```sh
docker build -t llm-cust-service ./docker_app
# Run the container
# docker run -p 5000:5000 llm-cust-service
```

### Testing
Run the test scripts:
```sh
python prediction_test.py
python test.py
```

## API Endpoints
- `POST /classify` — Classify a single customer message
- `POST /batch_classify` — Classify a batch of messages

## Data
- `customer_messages_20000_no_repeats.csv` — Large dataset for evaluation
- `messages_classification.json` — Labeled data for supervised tasks

## Customization
- Update `llm.py` to change the LLM provider or model.
- Modify `one_message_handler.py` for custom message handling logic.

## License
MIT License

## Authors
- Mahmoud AlNaser

## Acknowledgements
- OpenAI, Hugging Face, and other LLM providers
- Flask community
