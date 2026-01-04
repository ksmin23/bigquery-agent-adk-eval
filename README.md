# Build and Evaluate BigQuery Agents using Agent Development Kit (ADK) and GenAI Eval Service

> :information_source: This project is based on the **[Build and Evaluate BigQuery Agents using ADK and GenAI Eval Service Codelab](https://codelabs.developers.google.com/bigquery-adk-eval)**.

This project demonstrates how to build a conversational analytics agent using [Google's Agent Development Kit (ADK)](https://google.github.io/adk-docs/) that interacts with data stored in [BigQuery](https://cloud.google.com/bigquery). It also includes a comprehensive evaluation framework using [Vertex AI's GenAI Evaluation service](https://cloud.google.com/vertex-ai/docs/generative-ai/models/evaluation-overview).

## Project Overview

- **Agent Application**: A BigQuery data analysis agent that uses the `BigQueryToolset` to answer natural language questions by executing SQL queries.
- **Evaluation Framework**: A structured way to measure the performance of your agent using metrics like Factual Accuracy, Completeness, and Tool Use Trajectory.

## Prerequisites

- A Google Cloud Project with billing enabled.
- Enabled APIs: BigQuery API, Vertex AI API.
- Python 3.10 or higher.

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd bigquery-agent-adk-eval
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install google-adk google-cloud-aiplatform[evaluation] pandas python-dotenv
   ```

4. **Configure environment variables**:
   Create a `.env` file in the `data_agent_app/` directory (or use the one provided) with the following content:
   ```env
   GOOGLE_GENAI_USE_VERTEXAI=1
   GOOGLE_CLOUD_PROJECT=your-project-id
   GOOGLE_CLOUD_LOCATION=us-central1
   ```

## BigQuery Data Setup

The agent is designed to work with the `ecommerce` dataset based on the `thelook_ecommerce` public dataset. The following setup steps are sourced from the [Build and Evaluate BigQuery Agents using ADK and GenAI Eval Service Codelab](https://codelabs.developers.google.com/bigquery-adk-eval#3).

1. **Create the dataset**:
   ```bash
   bq mk --dataset --location=US ecommerce
   ```

2. **Load the tables**:
   Run the following commands to load the static snapshot of the dataset from the public GCS bucket:
   ```bash
   bq load --source_format=AVRO --autodetect ecommerce.events gs://sample-data-and-media/thelook_dataset_snapshot/events/*.avro.gz
   bq load --source_format=AVRO --autodetect ecommerce.order_items gs://sample-data-and-media/thelook_dataset_snapshot/order_items/*.avro.gz
   bq load --source_format=AVRO --autodetect ecommerce.products gs://sample-data-and-media/thelook_dataset_snapshot/products/*.avro.gz
   bq load --source_format=AVRO --autodetect ecommerce.users gs://sample-data-and-media/thelook_dataset_snapshot/users/*.avro.gz
   bq load --source_format=AVRO --autodetect ecommerce.orders gs://sample-data-and-media/thelook_dataset_snapshot/orders/*.avro.gz
   bq load --source_format=AVRO --autodetect ecommerce.inventory_items gs://sample-data-and-media/thelook_dataset_snapshot/inventory_items/*.avro.gz
   bq load --source_format=AVRO --autodetect ecommerce.distribution_centers gs://sample-data-and-media/thelook_dataset_snapshot/distribution_centers/*.avro.gz
   ```


## Usage

### 1. Chat with the Agent (Web UI)
Launch the built-in ADK web server to interact with your agent:
```bash
adk web
```
Then open the provided URL (usually `http://127.0.0.1:8000`) in your browser.

### 2. Run Evaluation
Execute the evaluation script to assess the agent's performance against the `evaluation_dataset.json`:
```bash
python evaluate_agent.py
```

You can also specify a custom evaluation dataset:
```bash
python evaluate_agent.py --dataset custom_dataset.json
```

## Project Structure

```text
bigquery-agent-adk-eval/
├── data_agent_app/             # Main ADK application folder
│   ├── agent.py                # Agent definition and toolset assignment
│   ├── prompts.py              # System instructions for the agent
│   └── .env                    # Environment configuration
├── evaluate_agent.py           # Vertex AI Evaluation script
├── evaluation_dataset.json     # Ground truth dataset for evaluation
├── run_agent.py                # Logic for running agent conversations
├── utils.py                    # Utility functions for evaluation and reporting
└── requirements.txt            # Project dependencies
```

## Evaluation Metrics

The evaluation script uses the following Vertex AI metrics:
- **Factual Accuracy**: Measures if the agent's response correctly reflects the facts in the reference answer.
- **Completeness**: Measures if the agent's response provides all the essential information requested.
- **Tool Use (Trajectory)**: Validates if the agent used the expected tools (e.g., `list_table_ids`).

Results are saved in the `eval_results/` directory as JSON files for detailed inspection.

## References

- [Build and Evaluate BigQuery Agents using ADK and GenAI Eval Service Codelab](https://codelabs.developers.google.com/bigquery-adk-eval#0)
- [ADK Agents for BigQuery Series (2025-08-05)](https://medium.com/google-cloud/adk-agents-for-bigquery-series-40de8cf4e3ca)
- [ADK Evaluation](https://google.github.io/adk-docs/evaluate/)
- [User Simulation in ADK Evals](https://github.com/google/adk-samples/blob/main/python/notebooks/evaluation/user_simulation_in_adk_evals.ipynb)
- [Announcing user simulation in ADK evaluation (2025-11-07)](https://developers.googleblog.com/en/announcing-user-simulation-in-adk-evaluation/)
- [Get started with Cloud API Registry](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/tutorial_get_started_with_cloud_api_registry.ipynb)