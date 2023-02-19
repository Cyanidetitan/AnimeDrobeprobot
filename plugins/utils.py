from math import floor

import os


import cv2

import random

from string import ascii_letters, ascii_uppercase, digits

from pyrogram.types import Message, MessageEntity
    def get_screenshot(file):

    cap = cv2.VideoCapture(file)

    name = "./" + \

        "".join(random.choices(ascii_uppercase + digits, k=10)) + ".jpg"

    total_frames = round(cap.get(cv2.CAP_PROP_FRAME_COUNT))-1

    frame_num = random.randint(0, total_frames)

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num-1)

    res, frame = cap.read()

    cv2.imwrite(name, frame)

    cap.release()

    # cv2.destroyAllWindows()

    return name
