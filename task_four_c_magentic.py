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
log_path = Path("agent_logs4c.txt")
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

    task = "Analyze the picture “dresscolor.png” from my downloads folder and give me a detailed description about the colors. After that find out, why people see different colors in this dress, use google ans search 'dress different colors illusion'."
    start_time = time.time()
    
    result = await Console(m1.run_stream(task=task))

    end_time = time.time()
    print(f"Dauer: {end_time - start_time:.2f} Sekunden")

    sys.stdout = sys.__stdout__
    print("Agent chat completed. Log saved to:", log_path.absolute())

if __name__ == "__main__":
    asyncio.run(task_one())
