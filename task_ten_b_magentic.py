import asyncio
import io
import os
from pathlib import Path
import sys
import time
from autogen_ext.models.anthropic import AnthropicChatCompletionClient
from autogen_ext.teams.magentic_one import MagenticOne
from autogen_agentchat.ui import Console
from dotenv import load_dotenv

# Save agent chat logs
log_path = Path("agent_logs10b.txt")
log_file = log_path.open("w")
sys.stdout = io.TextIOWrapper(log_file.buffer, encoding='utf-8')

# Load environment variables
load_dotenv()


async def task_one():
    client = AnthropicChatCompletionClient(model="claude-3-haiku-20240307")  

    m1 = MagenticOne(client=client)

    task = "Find a GitHub project that demonstrates a cool AI demo using PyTorch. Download the repository, summarize its purpose and main functionality, and run a working demo if available."

    start_time = time.time()
    
    result = await Console(m1.run_stream(task=task))

    end_time = time.time()
    print(f"Dauer: {end_time - start_time:.2f} Sekunden")

    sys.stdout = sys.__stdout__
    print("Agent chat completed. Log saved to:", log_path.absolute())

if __name__ == "__main__":
    asyncio.run(task_one())
