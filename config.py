AccountsRecheckTime = 300
MaxRandomDelay = 120
AccountList = [
    {
        "account_name": "Account 1",  # A custom name for the account (not important, just for logs)
        "Authorization": "Bearer 17265438602281JB8FfgzuB8zGINDOgvHoazkKdak70s10TkTgeUykG24pgpBf8gvh14c8NDfTf5z7378429478",  # To get the token, refer to the README.md file
        "UserAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",  # Refer to the README.md file to obtain a user agent
        "Proxy": {},  # You can use proxies to avoid getting banned. Use {} for no proxy
        # Example of using a proxy:
        # "Proxy": {
        #   "https": "https://10.10.1.10:3128",
        #   "http": "http://user:pass@10.10.1.10:3128/"
        # },
        "config": {
            "auto_tap": True,  # Enable auto tap by setting it to True, or set it to False to disable
            "auto_free_tap_boost": True,  # Enable auto free tap boost by setting it to True, or set it to False to disable
            "auto_get_daily_cipher": True,  # Enable auto get daily cipher by setting it to True, or set it to False to disable
            "auto_get_daily_task": True,  # Enable auto-get daily tasks by setting it to True, or set it to False to disable
            "auto_get_task": True,  # Enable auto get (Youtube/Twitter and ...) task to True, or set it to False to disable
            "auto_finish_mini_game": True,  # Enable auto finish mini game by setting it to True, or set it to False to disable
            "auto_claim_daily_combo": True,  # Enable auto claim daily combo by setting it to True, or set it to False to disable
            "auto_daily_combo_enable": True,  # Enable auto daily combo by setting it to True, or set it to False to disable
            "auto_daily_combo_max_price": 5_000_000,  # Maximum price of combo for purchase
            "auto_playground_games": True,  # Enable auto playground games by setting it to True, or set it to False to disable
            # If you have over 5 accounts, disable the auto_playground_games feature or use a proxy for each account.
            "auto_upgrade": True,  # Enable auto-upgrade by setting it to True, or set it to False to disable
            "auto_upgrade_start": 2_000_000,  # Start buying upgrades when the balance is greater than this amount
            "auto_upgrade_min": 100_000,  # Stop buying upgrades when the balance is less than this amount
            "enable_parallel_upgrades": True,  # Enable parallel card upgrades. This will buy cards in parallel if the best card is on cooldown. It should speed up the profit.
            "parallel_upgrades_max_price_per_hour": 1000,  # Cards with less than X coins per 1k will be bought
            "show_num_buy_options": 0,  # Number of card buy options to show in the logs, ranked by best value, 0 disables this.
            "max_promo_games_per_round": 3,  # Maximum number of promo games to play in a single round, 0 disables this.
        },
        "telegram_chat_id": "7378429478",  # String - you can get it from https://t.me/chatIDrobot
    }
]
telegramBotLogging = {
    "is_active": False,  # Set it to True if you want to use it, and make sure to fill out the below fields
    "bot_token": "",  # HTTP API access token from https://t.me/BotFather ~ Start your bot after creating it
    # Configure the what you want to receive logs from the bot
    "messages": {
        "general_info": True,  # General information
        "account_info": True,  # Account information
        "http_errors": False,  # HTTP errors
        "other_errors": False,  # Other errors
        "daily_cipher": True,  # Daily cipher
        "daily_task": False,  # Daily task
        "upgrades": True,  # Upgrades
    },
}

ConfigFileVersion = 1
