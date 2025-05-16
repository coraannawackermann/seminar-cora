import asyncio
import io
import os
from pathlib import Path
import sys
import time
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.teams.magentic_one import MagenticOne
from autogen_ext.models.openai._openai_client import ModelInfo
from autogen_agentchat.ui import Console
from dotenv import load_dotenv

# Save agent chat logs
log_path = Path("agent_logs10c.txt")
log_file = log_path.open("w")
sys.stdout = io.TextIOWrapper(log_file.buffer, encoding='utf-8')

# Load environment variables
load_dotenv()

# Set environment variables for debugging Playwright
os.environ["PLAYWRIGHT_HEADLESS"] = "false"
# os.environ["PWDEBUG"] = "1"


client = OpenAIChatCompletionClient(
    model="o4-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    model_info=ModelInfo(
        name="o4-mini",
        supports_function_calling=True,
        function_calling=True,
        is_openai=True,
        vision=True,
        json_output=True,
        family="openai"
    )
)

async def task_one():

    m1 = MagenticOne(client=client)

    task = "Find a GitHub project that demonstrates a cool AI demo using PyTorch. Download the repository, summarize its purpose and main functionality, and run a working demo if available."

    
    start_time = time.time()
    
    result = await Console(m1.run_stream(task=task))


    # Zeitmessung stoppen
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Dauer: {elapsed_time:.2f} Sekunden")

    sys.stdout = sys.__stdout__
    print("Agent chat completed. Log saved to:", log_path.absolute())


if __name__ == "__main__":
    asyncio.run(task_one())

    