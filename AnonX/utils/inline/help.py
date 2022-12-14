from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AnonX import app
from config import SUPPORT_GROUP


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ð¼á´á´á´ÉªÉ´ð¼",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="ð¼á´á´á´Êð¼",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="ð¼ÊÊá´á´á´ÊÉªsá´ð¼",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ð¼ÊÊá´á´á´á´á´sá´ð¼",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="ð¼É¢Êá´É´ð¼",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="ð¼ÊÊÊÉªá´sð¼",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ð¼á´©ÉªÉ´É¢ð¼",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="ð¼á´©Êá´Êð¼",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="ð¼á´©Êá´ÊÊÉªsá´ð¼",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ð¼á´ Éªá´á´á´á´Êá´á´sð¼",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="ð¼sá´á´Êá´ð¼",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="ð¼sá´á´á´ð¼",
                    callback_data="help_callback hb9",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                ),
                InlineKeyboardButton(
                    text="â¢ sá´á´©á´©á´Êá´ â¢", url=f"{SUPPORT_GROUP}"
                ),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ð¼ Êá´Êá´© ð¼",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
