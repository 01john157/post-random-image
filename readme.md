Requires [Python 3.7+](https://www.python.org/downloads/).  
A [Twitter Developer](https://developer.twitter.com) account is required.  
Store your API keys and access tokens in [environment variables](https://en.wikipedia.org/wiki/Environment_variable?&useskin=vector).  

# Usage
`python bot.py [-h] [--append_name] [--quotes] [-exclude_text IMAGE_NAME_TO_EXCLUDE] [--old_text old [old ...]] [--new_text new [new ...]] API_KEY API_SECRET ACCESS_TOKEN ACCESS_TOKEN_SECRET image_folder_path`

positional arguments:  
  `API_KEY`               name of the environment variable storing the API key  
  `API_SECRET`            name of the environment variable storing the API secret  
  `ACCESS_TOKEN`          name of the environment variable storing the access token  
  `ACCESS_TOKEN_SECRET`   name of the environment variable storing the access token secret  
  `image_folder_path`     path to the folder containing the images  

options:  
  `-h, --help`                                show help  
  `--append_name`                             append image name to the tweet  
  `--quotes`                                  add quotes around the tweet text  
  `--exclude_text IMAGE_NAMES_TO_EXCLUDE`     images starting with this text will not have their name appended to the Tweet  
  `--old_text old [old ...]`                  replace these strings with the corresponding --new_text strings in the image name  
  `--new_text new [new ...]`                  replace the corresponding --old_text strings in the image name  

# Examples
See the script in use at https://twitter.com/xenoscreenshots.
