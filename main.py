import logging
import time

import requests
import telebot

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

TOKEN = "PLACE_YOUR_BOT_TOKEN"

DEFAULT_LINK_INFO = "https://api.yani.tv/search"
SOCIAL_LINK_INFO = "https://api.yani.tv/anime/"


class GetAnimeHttpInfo:
    def __init__(self, anime_name):
        self.anime_name = anime_name
        self.params = {"q": self.anime_name}

        anime_data = self.get_anime_by_name()
        self.anime_id = anime_data.get("anime_id") if anime_data else None

        print(f"ANIME ID: {self.anime_id}.")

    def get_anime_by_name(self):
        try:
            response = requests.get(url=DEFAULT_LINK_INFO, params=self.params)
            response.raise_for_status()
            data = response.json()

            if data and "response" in data and len(data["response"]) > 0:
                anime_info = data["response"][0]
                status_stats = anime_info.get("anime_status", {})
                anime_status = status_stats.get("title", "nothing found...")

                return {
                    "title": anime_info.get("title"),
                    "anime_id": anime_info.get("anime_id"),
                    "description": anime_info.get("description"),
                    "year": anime_info.get("year"),
                    "status": anime_status,
                    "season": anime_info.get("season"),
                }
        except requests.exceptions.RequestException as e:
            print(f"Couldn't get information from the website, reason: {e}.")
            return None

    def get_anime_views(self):
        try:
            response = requests.get(url=DEFAULT_LINK_INFO, params=self.params)
            response.raise_for_status()
            data = response.json()

            if data and "response" in data and len(data["response"]) > 0:
                anime_info = data["response"][0]

                return {"views": anime_info.get("views", "nothing views found...")}
        except requests.exceptions.RequestException as e:
            print(f"❌ Can't get information from the website, the reason is: {e}.")
            return None

    def get_anime_reviews(self):
        if not self.anime_id:
            print(f"anime_id is {self.anime_id}. Continued.")
            return

        try:
            url = f"{SOCIAL_LINK_INFO}{self.anime_id}"
            print(f"Url = {url}..")

            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data and "response" in data and len(data["response"]) > 0:
                social_anime_info = data["response"]

                # Rating
                rating_dict = social_anime_info.get("rating", {})
                average_rating = rating_dict.get("average")
                rate_counters = rating_dict.get("counters")
                shikimori_rating = rating_dict.get("shikimori_rating")
                myanimelist_rating = rating_dict.get("myanimelist_rating")

                # Social
                comments_count = social_anime_info.get("comments_count")
                reviews_count = social_anime_info.get("reviews_count")
                partner_videos_count = social_anime_info.get("partner_videos_count")
                trailers_count = social_anime_info.get("trailers_count")

                return {
                    "average_rating": average_rating,
                    "rate_counters": rate_counters,
                    "shikimori_rating": shikimori_rating,
                    "myanimelist_rating": myanimelist_rating,
                    "comments_count": comments_count,
                    "reviews_count": reviews_count,
                    "partner_videos_count": partner_videos_count,
                    "trailers_count": trailers_count,
                }
        except requests.exceptions.RequestException as e:
            print(f"❌ Can't get information from the website, the reason is: {e}.")
            return None


class AnimeStatsBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)

        self.bot_controls()

    def start_bot(self):
        """Launching a fall-proof bot."""

        logging.info("🛫 Starting bot...")

        while True:
            try:
                self.bot.polling(non_stop=False, timeout=60, long_polling_timeout=60)
            except Exception as e:
                logging.error(f"❌ The bot crashed with an error: {e}.")
                logging.info("🔃 Restart after 10 seconds.")
                time.sleep(10)
                continue
            break

    def bot_controls(self):
        @self.bot.message_handler(commands=["start"])
        def starting_bot(message):
            self.bot.send_message(
                message.chat.id,
                "💢 Hello, I'm an anime statistics bot.\n"
                "💚 Always at your service!"
                "💌 My commands: \n\n"
                "💥  /get_anime_stats [Anime Name],\n"
                "💫  /get_anime_views [Anime Name], \n"
                "💟  /get_anime_reviews [Anime Name].\n\n"
                "💖Write any of these commands, I will be glad to help!",
            )

        @self.bot.message_handler(commands=["get_anime_stats"])
        def send_anime_stats(message):
            try:
                anime_name = message.text.split(" ", 1)[1]
            except IndexError:
                self.bot.send_message(
                    message.chat.id,
                    f"❌ Write the name after the command, for example /get_anime_status Re:Zero 4.",
                )
                return

            get_anime = GetAnimeHttpInfo(anime_name)
            anime_info = get_anime.get_anime_by_name()
            if not anime_info:
                self.bot.send_message(message.chat.id, "❌ This anime was not found")
                return

            self.bot.send_message(
                message.chat.id,
                (
                    "Anime Info \n\n"
                    f"anime_id: {anime_info.get("anime_id", "noting anime_id found...")}\n"
                    f"title_name: {anime_info.get("title", "noting title found...")}\n"
                    f"year: {anime_info.get("year", "noting year found...")}\n"
                    f"status: {anime_info.get("status", "noting status found...")}\n"
                    f"season: {anime_info.get("season", "noting season found...")}\n\n"
                    f"description: {anime_info.get("description", "noting description found...")}"
                ),
            )

        @self.bot.message_handler(commands=["get_anime_views"])
        def send_anime_views(message):
            try:
                anime_name = message.text.split(" ", 1)[1]
            except IndexError:
                self.bot.send_message(
                    message.chat.id,
                    "❌ Write the name after the command, for example: /get_anime_views Tabakoshka",
                )
                return

            get_anime = GetAnimeHttpInfo(anime_name)
            anime_info = get_anime.get_anime_views()
            if not anime_info:
                self.bot.send_message(
                    message.chat.id, "❌ Enter the correct anime name."
                )
                return

            views = anime_info.get("views", "nothing views found...")

            self.bot.send_message(
                message.chat.id,
                (
                    f"Anime found | {anime_name}!\n\n"
                    f"Current number of views: {views:_}"
                ),
            )

        @self.bot.message_handler(commands=["get_anime_reviews"])
        def send_anime_reviews(message):
            try:
                anime_name = message.text.split(" ", 1)[1]
            except IndexError:
                self.bot.send_message(
                    message.chat.id,
                    "❌ Write the name after the command, for example: /get_anime_reviews Van Pease",
                )
                return

            get_anime = GetAnimeHttpInfo(anime_name)
            reviews_anime_info = get_anime.get_anime_reviews()

            if not reviews_anime_info:
                print("❌ Send the correct anime.")
                return

            message_text = (
                f"💹 Anime found | {anime_name}\n\n"
                f"💛 Average rating: {reviews_anime_info.get('average_rating', 'N/A')}\n"
                f"💚 Number of reviews: {reviews_anime_info.get('rate_counters', 'N/A')}\n"
                f"💙 Rating from shikimori: {reviews_anime_info.get('shikimori_rating', 'N/A')}\n"
                f"💜 Rating from myAnime: {reviews_anime_info.get('myanimelist_rating', 'N/A')}\n\n"
                f"💬 Number of comments: {reviews_anime_info.get('comments_count', 'N/A')}\n"
                f"🧭 Number of reviews: {reviews_anime_info.get('reviews_count', 'N/A')}\n"
                f"〽 Number of partner materials: {reviews_anime_info.get('partner_videos_count', 'N/A')}\n"
                f"💌 Number of trailers: {reviews_anime_info.get('trailers_count', 'N/A')}"
            )

            self.bot.send_message(message.chat.id, message_text)


if __name__ == "__main__":
    bot = AnimeStatsBot(TOKEN)
    bot.start_bot()
