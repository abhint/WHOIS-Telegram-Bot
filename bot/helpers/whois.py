#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/AbhijithNT/WHOIS-Telegram-Bot
# (c) Abhijith N T

from pyrogram import Client, Filters
from pyrogram.client.methods import messages
import whois
from urllib.parse import urlparse 

@Client.on_message(Filters.command(["start"]))
async def startMsg(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"""
        <b>
        Hey {message.from_user.first_name},
        \nThis is a simple Telegram Bot which will produce WHOIS data for a given domain.
        \nCreated using the available open-source code.
        \nSource Code: https://github.com/Abhijith-cloud/WHOIS-Telegram-Bot
        \n© @thankappan369
        </b>
        """,
        reply_to_message_id=message.message_id,
        parse_mode="html"
    )
@Client.on_message(Filters.regex(pattern=".*http.*"))
async def whoisDomain(clinet, message):
    user_url = str(message.text)
    domain = urlparse(user_url)
    whios_domain = whois.whois(domain.netloc)
    domain_text = whios_domain.text
    user_text = domain_text.split('>>>') # MESSAGE_TOO_LONG
    if domain_text == 'Socket not responding':
        await clinet.send_message(
        chat_id=message.chat.id,
        text = f"""
        <b>TLD not supported\n</b>
        Please contact Admin\n
        @thankappan369
        """,
        parse_mode="html"
        )
    else:
        try:
            await clinet.send_message(
                chat_id=message.chat.id,
                text = user_text[0],
                parse_mode="html"
                )
        except Exception as error:
            await clinet.send_message(
                chat_id = message.chat.id,
                text = f"""
                {error}\n 
                Please contact Admin\n 
                @thankappan369""",
                parse_mode="html"
            )


