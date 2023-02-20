import asyncio
import base64
import os
import subprocess
from bot import bot 
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from helper_func import encode




@client.on_message(filters.chat(source_channel) & filters.document)
async def on_file(client, message: Message):
    file = await message.download()
    screenshot_file = os.path.join(os.path.dirname(file), 'screenshot.png')

    # Take screenshot using ffmpeg
    process = subprocess.Popen(
        ['ffmpeg', '-i', file, '-ss', '00:00:01', '-vframes', '1', screenshot_file],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = await process.communicate()

    # Generate link button
    caption = f"Link to file:"
    link = generate_link(message)
    button = InlineKeyboardButton(text="Get file", url=link)
    reply_markup = InlineKeyboardMarkup([[button]])

    # Send screenshot to reply_channel with link button
    await client.send_photo(reply_channel, photo=screenshot_file, caption=caption, reply_markup=reply_markup)

    # Clean up temporary files
    os.remove(file)
    os.remove(screenshot_file)


def generate_link(message: Message) -> str:
    # Generate link using the file sent by the user
    converted_id = message.message_id * abs(client.db_channel.id)
    string = f"get-{converted_id}"
    base64_string = encode(string)
    link = f"https://t.me/{client.get_me().username}?start={base64_string}"
    return link


