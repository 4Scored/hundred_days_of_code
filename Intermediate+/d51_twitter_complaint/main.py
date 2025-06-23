import os
from ist_bot import InternetSpeedTwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")

isp_bot = InternetSpeedTwitterBot()
isp_bot.get_internet_speed()
isp_bot.tweet_at_provider()
