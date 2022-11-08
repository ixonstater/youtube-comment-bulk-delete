import re


class CommentDeleter:
    commentDir = ""
    extDir = "Takeout/YouTube and YouTube Music/my-comments/my-comments.html"
    apiKey = ""
    baseUrl = "https://youtube.googleapis.com/youtube/v3/comments?id={0}&key={1}"
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

        self.apiKey = input("Google console API key: ")
        pass

    def delete(self):
        with open(self.commentDir, "r") as comments_file:
            contents = comments_file.read()
            commentReplyIds = re.findall(self.commentReplyRegex, contents)
            commentIds = re.findall(self.commentRegex, contents)
            self.delete_comments(commentIds)
            self.delete_comments(commentReplyIds)

    def delete_comments(self, ids):
        failed = []
        for id in ids:
            url = self.baseUrl.format(id, self.apiKey)
            response = requests.delete(url)
            if response.status_code != requests.codes.no_content:
                failed.append(id)
        print("Failed to delete the following: ", failed)


if __name__ == "__main__":
    obj = CommentDeleter()
    obj.delete()
