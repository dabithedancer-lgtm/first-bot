# config.py
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("DISCORD_TOKEN environment variable not set!")

PREFIXES = [
    "ls ", "ls",      # lower
    "LS ", "LS",      # upper
    "Ls ", "Ls",      # capital L, lower s
    "lS ", "lS",      # lower l, capital S
]
ADMINS = [1315746066900975770]  # Your User ID

# Constants
MAX_PULLS = 12
PULL_REGEN_SECONDS = 900
DAILY_COOLDOWN = 86400
GANG_CREATE_COST = 150000
MINE_COOLDOWN = 14400  # 4 hours

# URLs (Placeholders - Replace with your actual URLs)
IMG_SUMMON_ORB = "https://media.tenor.com/2RoDo8pZt6wAAAAC/black-clover-mobile-summon.gif"
IMG_TERRITORY_MAP = "https://example.com/map.jpg"

# File Paths
DATA_DIR = "./data"

# Patreon Roles (from lowest to highest tier)
# Copy (Tier 1), UI (Tier 2), TUI (Tier 3)
PATREON_ROLES = [
    1444529717704261652,  # Copy
    1444529800751480902,  # UI
    1444529879918837831,  # TUI
]
