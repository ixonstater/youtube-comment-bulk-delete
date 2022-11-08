# Youtube Comment Bulk Deletion

## Pre-requisites

You need two things for this to work:

1. To export your Youtube comment data from [Google Takeout](https://takeout.google.com/)
    * You can deselect all from the other Google apps and deselect all from Youtube and Youtube Music except for my-comments.
    * The export process can take some time to complete, but this step is necessary because the Youtube API doesn't allow searching for comments by user id.
2. A valid Youtube API key from the [Google Developer Console](https://console.cloud.google.com/apis/credentials).
    * You could also link your account and use OAuth tokens, but that is more work than I wanted to do.
    * Go to the link above and register an API key.
    * Once the API key is registered enable the [Youtube Data API V3](https://console.cloud.google.com/apis/library/youtube.googleapis.com).

## Running

On a machine with a valid Python installation (I tested on version 3.10.6) run `python main.py` and enter the requested information.
* The path to your takeout folder should be the top level folder you get upon extracting the zip file.
* If you get path errors you may need to mess around with the values in the `CommentDeleter` class.
* I ran this in a conda environment, but venv should also work fine.  The only real dependency is [Requests](https://pypi.org/project/requests/).

## Clean-up
Once you are done deleting your comments its best to delete your API key if you do not expect to keep using it.