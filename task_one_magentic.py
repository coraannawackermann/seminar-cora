import asyncio
import io
import os
from pathlib import Path
import sys
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.teams.magentic_one import MagenticOne
from autogen_agentchat.ui import Console
from dotenv import load_dotenv


# Save agent chat logs
log_path = Path("agent_logs.txt")
log_file = log_path.open("w")
sys.stdout = io.TextIOWrapper(log_file.buffer, encoding='utf-8')

# Load environment variables
load_dotenv()

# Set environment variables for debugging Playwright
os.environ["PLAYWRIGHT_HEADLESS"] = "false"
# os.environ["PWDEBUG"] = "1"


async def task_one():
    client = OpenAIChatCompletionClient(model="gpt-4o")

    m1 = MagenticOne(client=client)

    task = "Find name, email and office location of the three responsible people that organize " \
    "Seminar CS715 at the University of Mannheim. Use this website https://www.uni-mannheim.de/ " \
    "to find the information."

    
    result = await Console(m1.run_stream(task=task))


    sys.stdout = sys.__stdout__
    print("Agent chat completed. Log saved to:", log_path.absolute())

if __name__ == "__main__":
    asyncio.run(task_one())