import os

import subprocess

from pyrogram import Client, filters

app = Client("my_bot")

# Define the source and destination channels

source_channel = -192828110

destination_channel = "@AnimeMonk"

# Define a filter to only allow video messages in the source channel

video_filter = filters.video & filters.chat(source_channel)

# Define a function to take a screenshot of a video file using ffmpeg

def take_screenshot(video_path):

    screenshot_path = os.path.splitext(video_path)[0] + ".jpg"

    subprocess.call(["ffmpeg", "-i", video_path, "-ss", "00:00:30", "-vframes", "1", screenshot_path])

    return screenshot_path

# Define a handler function to process video messages

@app.on_message(video_filter)

async def process_video(client, message):

    # Download the video file

    video_path = await message.download()

    # Take a screenshot of the video

    screenshot_path = take_screenshot(video_path)

    # Send the screenshot to the destination channel

    await client.send_photo(destination_channel, photo=screenshot_path, caption="Screenshot of video from {}.".format(source_channel))

    # Remove the screenshot and video files

    os.remove(screenshot_path)

    os.remove(video_path)

# Start the bot

app.run()

