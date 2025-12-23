**
This document describes how to set up a Discord bot integrated with an LLM and verify that it responds correctly inside a Discord channel.

Setup Instructions
1. Create and Verify Discord Account

Sign up and verify your account at https://discord.com

2. Create a Discord Server

Click Add a Server

Create a new server (private or internal)

3. Create a Channel

Inside the server, create a text channel

Example: #ops

![Uploading Screenshot from 2025-12-23 09-39-24.png…]()

4. Create a Discord Application (Bot)

Go to https://discord.com/developers/applications

Click New Application

Provide an application name

5. Add a Bot to the Application

Navigate to Bot

Click Add Bot

6. Generate and Copy Bot Token

Under Bot → Token

Click Reset Token

Copy the token securely

Do not commit this token to source control.

7. Configure Bot Permissions and Intents

Under Bot → Privileged Gateway Intents:

Enable Message Content Intent

Recommended bot permissions:

View Channels

Send Messages

Read Message History

Save changes.

<img width="1943" height="962" alt="Screenshot from 2025-12-23 09-44-44" src="https://github.com/user-attachments/assets/de84d8bb-3e13-4f40-9547-67fe1ce638da" />


8. Configure Environment Variables

Create a .env file:

DISCORD_TOKEN=<discord_bot_token>
OPENAI_API_KEY=<openai_api_key>

9. Build Docker Image
docker build -t discord-ops-bot .

10. Run the Container
docker run -it --env-file .env discord-ops-bot

11. Start the Bot Inside the Container
python discord_hooks.py

<img width="1917" height="962" alt="Screenshot from 2025-12-23 11-08-56" src="https://github.com/user-attachments/assets/bdd0d6c4-e4b2-454b-976b-7c80d244bdec" />**Discord Ops Bot – Setup & Usage

You should see:

Logged in as <BotName>

Example Usage
Example 1: Basic Command

User:

hello

Bot:

Hello <username>

Example 2: Operations Query Routed to LLM

User:

Line 3 OEE dropped during night shift

Bot:

Observation:
- Sudden OEE decline on Line 3 during night shift

Likely Causes:
- Equipment instability
- Operator handover gap
- Material inconsistency

Recommended Actions:
- Review downtime logs
- Validate shift handover
- Escalate if recurrence persists

<img width="1917" height="962" alt="Screenshot from 2025-12-23 11-08-56" src="https://github.com/user-attachments/assets/0bdab9e2-6145-4387-a747-2dcfe44b3cc1" />

