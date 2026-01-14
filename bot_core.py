import logging
import os
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    handlers=[logging.FileHandler("bot.log"),
              logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger("bot_core")

load_dotenv()
ENV = os.getenv("ENV", "prod").lower()

if ENV == "test":
    TOKEN = os.getenv("BOT_TOKEN_TEST")
else:
    TOKEN = os.getenv("BOT_TOKEN_PROD")

if not TOKEN or TOKEN == "NO_TOKEN":
    raise ValueError(f"Token not found for environment: {ENV}")

logger.info(f"Bot starting in {ENV} mode | token ends with ...{TOKEN[-6:]}")

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
