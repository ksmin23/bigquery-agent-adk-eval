from google.adk.agents.llm_agent import Agent
from google.adk.tools.bigquery import BigQueryCredentialsConfig, BigQueryToolset
import google.auth
import dotenv
from .prompts import BIGQUERY_AGENT_INSTRUCTION_1, BIGQUERY_AGENT_INSTRUCTION_2

dotenv.load_dotenv()

credentials, _ = google.auth.default()
credentials_config = BigQueryCredentialsConfig(credentials=credentials)
bigquery_toolset = BigQueryToolset(
  credentials_config=credentials_config,
)

root_agent = Agent(
  model="gemini-2.5-flash",
  name="bigquery_agent",
  description="Agent that answers questions about BigQuery data by executing SQL queries.",
  instruction=BIGQUERY_AGENT_INSTRUCTION_2,
  tools=[bigquery_toolset]
)

def get_bigquery_agent():
 return root_agent
