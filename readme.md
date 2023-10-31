Posts a random image from a local folder to Twitter using [Tweepy](https://www.tweepy.org/).

# Prerequisites
Requires Python 3.7+.
A [Twitter Developer](https://developer.twitter.com) account is required. Store your API keys in `keys.py`.

# Usage
`python bot.py [-h] [-append_name] [-exclude_text IMAGE_NAME_TO_EXCLUDE] [-old_text old [old ...]] [-new_text new [new ...]] image_folder_path`

positional arguments:
  `image_folder_path`     path to the folder containing the images

options:
  `-h, --help`                                show help
  `--append_name`                             append image name to the tweet
  `--exclude_text IMAGE_NAMES_TO_EXCLUDE`     images starting with this text will not have their name appended to the Tweet
  `--old_text old [old ...]`                  replace these strings with the corresponding --new_text strings in the image name
  `--new_text new [new ...]`                  replace the corresponding --old_text strings in the image name

See the script in use at https://twitter.com/xenoscreenshots.