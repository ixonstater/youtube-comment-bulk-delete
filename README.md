# Youtube Comment Bulk Deletion

## Pre-requisites

You need two things for this to work:

1. To export your Youtube comment data from [Google Takeout](https://takeout.google.com/)
    * You can deselect all from the other Google apps and deselect all from Youtube and Youtube Music except for my-comments.
    * The export process can take some time to complete, but this step is necessary because the Youtube API doesn't allow searching for comments by user id.
2. To setup an OAuth client id in the [Google Developer Console](https://console.cloud.google.com/apis/credentials).
    * You will need to create a project, but you can use an account other than the one you wish to delete comments from if you wish.
    * You will need to configure an OAuth consent screen, just filling in the required stuff should be fine.
    * You will need to add yourself and anyone else that will be using this app as test users.
    * Once the OAuth client config is done enable the [Youtube Data API V3](https://console.cloud.google.com/apis/library/youtube.googleapis.com).

## Running

On a machine with a valid Python installation (I tested on version 3.10.6) run `python main.py` and enter the requested information.
* The path to your takeout folder should be the top level folder you get upon extracting the zip file.
* If you get path errors you may need to mess around with the values in the `CommentDeleter` class.
* I ran this in a conda environment, but venv should also work fine.  If you run on iOS or Linux some of the packages in the requirements file may be platform specific to Windows.

## Clean-up

Once you are done deleting your comments its best to delete your API key if you do not expect to keep using it.