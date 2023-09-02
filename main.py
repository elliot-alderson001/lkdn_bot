from bot import JobApplicationBot
from pathlib import Path
import yaml
from _config import Config

def main():
    credfile = open("credentials.yml", "r")
    credentials = yaml.safe_load(credfile)
    username = credentials["username"]
    password = credentials["password"]
    config = Config(username=username, password=password)
    bot = JobApplicationBot(config)
    bot.run()

if __name__ == "__main__":
    main()