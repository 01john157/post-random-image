import os, argparse, random, shutil, tweepy
import keys

# Create a parser to handle the command line arguments.
parser = argparse.ArgumentParser()

# Define all the command line arguments.
parser.add_argument(
    'image_folder_path', 
    help = "path to the folder containing the images"
)
parser.add_argument(
    '--append_name',
    dest = 'append_name',
    action = 'store_true',
    help = "append image name to the tweet"
)
parser.add_argument(
    '--exclude_text',
    dest = 'image_name_to_exclude',
    help = "images starting with this text will not have their name appended to the Tweet"
)
parser.add_argument(
    '--old_text',
    metavar = 'old',
    dest = 'old_text',
    nargs = '+',
    help = "replace these strings with the corresponding --new_text strings in the image name"
)
parser.add_argument(
    '--new_text',
    metavar = 'new',
    dest = 'new_text',
    nargs = '+',
    help = "replace the corresponding --old_text strings in the image name"
)

# Get all the provided command line arguments.
args = parser.parse_args()


# Check the validity of the provided command line arguments.
if not os.path.isdir(args.image_folder_path):
    raise Exception(
        "Specified directory does not exist."
    )

if not args.old_text == None:
    if not args.new_text == None:
        if len(args.old_text) != len(args.new_text):
            raise Exception(
                "-old_text and -new_text do not contain corresponding elements."
            )


# Change the current working directory to the image folder.
os.chdir(args.image_folder_path)

# List the names of all the files (not including folders) in the current working directory.
images = [i for i in os.listdir() if os.path.isfile(os.path.join(os.getcwd(), i))]

if len(images) == 0:
    raise Exception(
        "No more images to post."
    )

# Pick a random image from the list of all images.
image = random.choice(images)


# Authenticate for both v1.1 and v2 of the Twitter API as it is currently not possible to post a tweet with an image directly.
# v1.1 of the API is used to upload an image. The id of this uploaded image is then appended to v2 to post a tweet with an image.
# API keys are stored in keys.py.
auth = tweepy.OAuth1UserHandler(keys.API_KEY, keys.API_SECRET)
auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
api_v1 = tweepy.API(auth)
api_v2 = tweepy.Client(consumer_key = keys.API_KEY, consumer_secret = keys.API_SECRET, access_token = keys.ACCESS_TOKEN, access_token_secret = keys.ACCESS_TOKEN_SECRET)


# Upload the chosen image and retrieve its id.
uploaded_image = api_v1.media_upload(filename = image)
uploaded_image_id = uploaded_image.media_id


# Format the image name to remove the file extension, add quotes, and replace all "_" with "?" to get around Windows file name restrictions.
formatted_image_name = ""
if args.append_name:
    if not image.startswith(args.image_name_to_exclude if args.image_name_to_exclude else "/"):
        formatted_image_name += "".join(['"', os.path.splitext(image)[0],'"'])
        if not args.old_text == None:
            if not args.new_text == None:
                for i in range(len(args.old_text)):
                    formatted_image_name = formatted_image_name.replace(args.old_text[i], args.new_text[i])


try:
    # Post the tweet containing the image and the formatted name.
    api_v2.create_tweet(text = formatted_image_name, media_ids = [uploaded_image_id])
except Exception as e:
    print(e)
else:
    print("Successfully posted: " + os.getcwd() + "/" + image)
    # Move the successfully posted image into a new folder, excluding it from being posted again.
    if not os.path.isdir('posted'):
        os.mkdir('posted')
    shutil.move(os.getcwd() + "/" + image, os.getcwd() + '/posted/' + image)