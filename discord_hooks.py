import discord
import os
import random
from dotenv import load_dotenv
from llm_agent import OpsLLMAgent

load_dotenv()

# ---- Discord Intents ----
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

token = os.getenv("DISCORD_TOKEN")
llm_agent = OpsLLMAgent()

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = message.author.name
    user_message = message.content.strip().lower()

    print(f"📩 {username}: {user_message}")

    # ---- Fast local commands ----
    if user_message in ("hello", "hi"):
        await message.channel.send(f"Hello {username} 👋")
        return

    if user_message == "bye":
        await message.channel.send(f"Bye {username} 👋")
        return

    # ---- Route everything else to LLM ----
    await message.channel.send("🔍 Analyzing operational context...")

    ops_context = f"""
        User: {username}
        Channel: {message.channel.name}

        Message:
        {message.content}
        """

    response = llm_agent.generate_response(ops_context)

    # Discord message limit safety
    for chunk in [response[i:i+1900] for i in range(0, len(response), 1900)]:
        await message.channel.send(chunk)

client.run(token)
