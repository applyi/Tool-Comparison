from os import getenv
from dotenv import load_dotenv


load_dotenv()


TARGET_URL = getenv("TARGET_URL", "https://trends.google.com/trends/trendingsearches/daily?geo=ID")