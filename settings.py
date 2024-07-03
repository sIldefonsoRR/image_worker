import os
from dotenv import load_dotenv

load_dotenv()

# Got API Key from https://platform.stability.ai/account/keys
STABILITY_API_KEY = os.environ.get('STABILITY_API_KEY')
STABILITY_URL = 'https://api.stability.ai/v2beta/stable-image/generate/core'
