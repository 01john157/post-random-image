Posts a random image from a local folder to Twitter using [Tweepy](https://www.tweepy.org/).

# Prerequisites
Requires Python 3.7+.
A [Twitter Developer](https://developer.twitter.com) account is required. Store the API keys in `keys.py`.

# Usage
`python bot.py PATH_TO_IMAGE_FOLDER IMAGE_FILENAME_TO_EXCLUDE`

`PATH_TO_IMAGE_FOLDER` the path to the folder to pick images from e.g "./images/"

`IMAGE_FILENAME_TO_EXCLUDE` all images starting with this text will not have their filename appended to the tweet as text e.g. "PXL_"

See the script in use at https://twitter.com/xenoscreenshots.