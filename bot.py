import os, sys, random, shutil, tweepy
import keys


# Path to the folder containing the images, recieved as a command line argument when running the script.
image_folder_path = sys.argv[1]
image_name_to_ignore = sys.argv[2]

# Check if the specified folder exists, then change the current working directory to that folder.
if os.path.isdir(image_folder_path):
    os.chdir(image_folder_path)
    current_working_directory = os.getcwd()
else:
    raise Exception(
        "Specified directory does not exist."
    )

# List the names of all the files (not including folders) in the current working directory.
images = [i for i in os.listdir() if os.path.isfile(os.path.join(current_working_directory, i))]

if len(images) > 0:
    # Pick a random image from the list of all images.
    image = random.choice(images)
else:
    raise Exception(
        "No more images to post."
    )

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

# Format the image name to remove the file extension and add quotes.
formatted_image_name = ""
if not image.startswith(image_name_to_ignore):
    formatted_image_name = '"' + os.path.splitext(image)[0] + '"'


try:
    # Post the tweet containing the image and the formatted name.
    api_v2.create_tweet(text = formatted_image_name, media_ids = [uploaded_image_id])
except Exception as e:
    print(e)
else:
    # Move the successfully posted image into a new folder, excluding it from being posted again.
    if not os.path.isdir('posted'):
        os.mkdir('posted')
    shutil.move(current_working_directory + "/" + image, current_working_directory + '/posted/' + image)