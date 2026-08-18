# 🎌 ANIME STATS TELEGRAM BOT

<p align="center">
  <img src="assets/banner.jpg" alt="Anime Stats Bot Banner" width="100%">
</p>

> A Telegram bot for retrieving anime statistics, views, and reviews

## TABLE OF CONTENTS

- About the Project
- Features
- Bot Commands
- Technologies
- Installation
- Usage
- Project Structure
- Examples
- Roadmap
- Contributing
- License
- Contact
- Acknowledgments

## 1. ABOUT THE PROJECT

>Anime Stats Telegram Bot is a convenient Telegram bot that allows users to 
quickly get information about anime. The bot accesses the open API of 
yani.tv and provides users with up-to-date data in a convenient format.

>This project is created for anime fans who want to quickly find out:
- Basic anime information
- View counts
- Ratings and reviews

## FEATURES

Command                     | Description                    | What You Get
----------------------------|--------------------------------|------------------------------
/get_anime_stats [name]     | Full statistics                | ID, title, year, status, 
                            |                                | season, description
/get_anime_views [name]     | View count                     | Title and number of views
/get_anime_reviews [name]   | Ratings and reviews            | Average rating, Shikimori
                            |                                | and MyAnimeList ratings,
                            |                                | comments, reviews, trailers

## BOT COMMANDS

/start
--------
Welcome message with a list of all available commands.

Example:
/start

Response:
💢 Hello, I'm an anime statistics bot.
💚 Always at your service!💌 My commands: 

💥  /get_anime_stats [Anime Name],
💫  /get_anime_views [Anime Name], 
💟  /get_anime_reviews [Anime Name].

💖Write any of these commands, I will be glad to help!

/get_anime_stats [anime name]
--------------------------------
Get full information about an anime.

Example:
/get_anime_stats Naruto

Response:
Anime Info 

anime_id: 12345
title_name: Naruto
year: 2002
status: Finished
season: Spring

description: The story of Naruto Uzumaki, a young ninja...

/get_anime_views [anime name]
-------------------------------
Get the number of views.

Example:
/get_anime_views One Piece

Response:
Anime found | One Piece!

Current number of views: 1,234,567

/get_anime_reviews [anime name]
---------------------------------
Get ratings and reviews.

Example:
/get_anime_reviews Attack on Titan

Response:
💹 Anime found | Attack on Titan

💛 Average rating: 8.5
💚 Number of reviews: 234
💙 Rating from shikimori: 8.7
💜 Rating from myAnmar: 8.4

💬 Number of comments: 1234
🧭 Number of reviews: 56
〽 Number of partner materials: 12
💌 Number of trailers: 3

## TECHNOLOGIES

- Python 3.10+         - Core programming language
- pyTelegramBotAPI     - Library for working with Telegram Bot API
- Requests             - For HTTP requests to yani.tv API
- Logging              - For event and error logging

ARCHITECTURE:
-------------
                    ┌─────────────────────────────────┐
                    │       Telegram Bot             │
                    │     (AnimeStatsBot)            │
                    ├─────────────────────────────────┤
                    │                                 │
                    │  ┌──────────┐  ┌────────────┐  │
                    │  │ /start   │  │ /get_anime_│  │
                    │  │ Command  │  │   stats    │  │
                    │  └──────────┘  └────────────┘  │
                    │                                 │
                    │  ┌──────────────────────────┐   │
                    │  │   GetAnimeHttpInfo       │   │
                    │  │ - get_anime_by_name()    │   │
                    │  │ - get_anime_views()      │   │
                    │  │ - get_anime_reviews()    │   │
                    │  └──────────────────────────┘   │
                    │            │                    │
                    │            ▼                    │
                    │  ┌──────────────────────────┐   │
                    │  │    API yani.tv           │   │
                    │  │ /search                  │   │
                    │  │ /anime/{id}              │   │
                    │  └──────────────────────────┘   │
                    └─────────────────────────────────┘

## INSTALLATION

> Clone the repository
------------------------
- git clone https://github.com/Y90G7IYO0987/AnimeStatsBot
cd anime-telegram-bot

- Create a virtual environment (optional but recommended)
------------------------------------------------------------
> python -m venv venv
source venv/bin/activate     # Linux/Mac
# or
> venv\Scripts\activate        # Windows

### Install dependencies
------------------------
pip install pyTelegramBotAPI requests

Or using requirements.txt:
pip install -r requirements.txt

### Configure the bot token
---------------------------
Open the file "import logging.txt" and replace TOKEN = "PLACE_YOUR_BOT_TOKEN" 
with your actual token:

TOKEN = "your_actual_bot_token_here"

How to get a bot token:
- Message @BotFather on Telegram
- Send /newbot command
- Choose a name for your bot
- Choose a username (must end with 'bot', e.g., anime_stats_bot)
- Copy the received token

- Run the bot
---------------
python "import logging.txt"

Successful startup:
2024-01-15 10:30:45 - INFO - 🛫 Starting bot...

## USAGE

- Find your bot on Telegram by its username
- Send /start command for a welcome message
- Use commands with anime names:

> /get_anime_stats Vinland Saga

> /get_anime_views Demon Slayer

> /get_anime_reviews Jujutsu Kaisen

## PROJECT STRUCTURE

anime-telegram-bot/
├── import logging.txt     # Main bot code file
├── requirements.txt       # Project dependencies
├── README.md             # Documentation
└── LICENSE               # License

CLASS DESCRIPTIONS:
-------------------

GetAnimeHttpInfo
- Class for working with yani.tv API
- get_anime_by_name()   - Gets basic anime information
- get_anime_views()     - Gets view count
- get_anime_reviews()   - Gets ratings and reviews

AnimeStatsBot
- Main bot class
- start_bot()           - Starts the bot with auto-restart on errors
- bot_controls()        - Registers all command handlers

## EXAMPLES

/get_anime_stats NARUTO
------------------------
Anime Info 

anime_id: 12345
title_name: Naruto
year: 2002
status: Finished
season: Spring

description: The story of Naruto Uzumaki, a young ninja who dreams of 
becoming the Hokage, the leader of his village...

/get_anime_views ONE PIECE
---------------------------
Anime found | One Piece!

Current number of views: 1,234,567

/get_anime_reviews DEMON SLAYER
--------------------------------
💹 Anime found | Demon Slayer

💛 Average rating: 8.6
💚 Number of reviews: 312
💙 Rating from shikimori: 8.8
💜 Rating from myAnmar: 8.5

💬 Number of comments: 2341
🧭 Number of reviews: 78
〽 Number of partner materials: 15
💌 Number of trailers: 4

## ROADMAP

- Add multi-language support (EN/RU toggle)
- Improve error handling with user-friendly messages
- Add request caching for faster responses
- Create inline mode for quick search
- Add random anime recommendation command
- MyAnimeList API integration
- Add rating charts and visualizations
- Voice command support
- Add database for search history
- Daily popular anime newsletter

## CONTRIBUTING

1. Fork the repository
2. Create a feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add some amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request

Guidelines:
- Follow PEP 8 style guide
- Write clear commit messages
- Test your changes before submitting
- Update documentation if needed

## LICENSE

Distributed under the MIT License. See LICENSE file for details.

MIT License Summary:
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use
- ❌ Liability
- ❌ Warranty

## CONTACT

- Author: Ats_Profi_Code
- GitHub: https://github.com/Y90G7IYO0987
- Email: atsprofi427@gmail.com
- Project Link: https://github.com/Y90G7IYO0987/AnimeStatsBot

## ACKNOWLEDGMENTS

- yani.tv for providing the anime API
- Telegram Bot API for the excellent platform
- pyTelegramBotAPI for the Python library
- All contributors and users who help improve the bot

## PROJECT STATISTICS

GitHub Stars: ⭐ Star the project if you like it!
GitHub Forks: 🍴 Fork to contribute!
Issues: 🐛 Report bugs!
Pull Requests: 🔧 Submit improvements!

---

⭐ If you found this project helpful, please give it a star on GitHub!

📢 Share with friends who love anime!

Made with ❤️ and ☕ for anime fans
---