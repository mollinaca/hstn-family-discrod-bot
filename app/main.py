#!/usr/bin/env python3
import os
import time
import discord as d
import dotenv

dotenv.load_dotenv()


def pip_freeze():
    import subprocess

    proc = subprocess.run(["pip", "freeze"], stdout=subprocess.PIPE)
    print(proc.stdout.decode("utf-8"))
    exit(0)

def discord_bot():
    TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    client = d.Client(intents=d.Intents.all())

    bot_help = (
        "/hstn-family-bot の使い方だよ\n"
        "```"
        "/hstn-bot help    : このテキストを表示するよ。 \n"
        "```"
    )

    # 起動時に動作する処理
    @client.event
    async def on_ready():
        print("bot login to channel")

    # メッセージ受信時に動作する処理
    @client.event
    async def on_message(message):
        if message.author.bot:
            return

        if message.content == "/hstn-bot bot-test":
            await message.channel.send("bot-test だよ. Hello!")

        if message.content == "/hstn-bot help":
            await message.channel.send(bot_help)

    # Botの起動とDiscordサーバーへの接続
    client.run(TOKEN)


if __name__ == "__main__":
    # pip_freeze()
    discord_bot()
    exit(0)
