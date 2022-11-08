import os
import re
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


class CommentDeleter:
    commentDir = ""
    extDir = "Takeout/YouTube and YouTube Music/my-comments/my-comments.html"
    # Lazy match up to 150 characters between lc= and ">replied
    commentReplyRegex = 'lc\=(.{,150}?)(?="\>replied)'
    # Lazy match up to 50 characters preceeded by 'You added a ' and up to 100 subsequent uncaptured characters
    # and followed by ">comment
    commentRegex = 'You\sadded\sa\s(?:.{,100})lc\=(.{,50}?)(?="\>comment)'

    def __init__(self):
        commentDir = input("Path to takeout dump main folder: ")
        if commentDir[-1] != "/" or commentDir[-1] != "\\":
            self.commentDir = commentDir + "/" + self.extDir
        else:
            self.commentDir = commentDir + self.extDir
        pass

    def delete(self):
        with open(self.commentDir, "r", encoding="utf8") as comments_file:
            contents = comments_file.read()
            commentReplyIds = re.findall(self.commentReplyRegex, contents)
            commentIds = re.findall(self.commentRegex, contents)

            api_service_name = "youtube"
            api_version = "v3"
            client_secrets_file = "creds.json"
            scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                client_secrets_file, scopes
            )
            credentials = flow.run_console()
            youtube = googleapiclient.discovery.build(
                api_service_name, api_version, credentials=credentials
            )
            self.delete_comments(commentIds, youtube)
            self.delete_comments(commentReplyIds, youtube)

    def delete_comments(self, ids, client):
        for id in ids:
            request = client.comments().delete(id=id)
            request.execute()


if __name__ == "__main__":
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    obj = CommentDeleter()
    obj.delete()
