import asyncio
import io
import os
from pathlib import Path
import sys
import time
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.teams.magentic_one import MagenticOne
from autogen_agentchat.ui import Console
from dotenv import load_dotenv

# Save agent chat logs
log_path = Path("agent_logs6.txt")
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

    task = "Go to https://www.chess.com/de/play/computer and click on “Spielen” or “Play” to start a game against a computer. " \
    "You do not need an account. Play the game until you win or lose. Document each move you make in a .txt document and add in " \
    "the end if you won or lost. Give yourself feedback of how you played. Safe the .txt document to my Desktop."

    
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

    