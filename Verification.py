#isFacebook : verify if it's a facebook link
def isFacebook(string):
    return "facebook" in string.lower() or "fb" in string.lower()

#isTwitter : verify if it's a twitter link
def isTwitter(string):
    return "twitter" in string.lower()


#isGithub : verify if it's a github link
def isGithub(string):
    return "github" in string.lower()

#isInstagram: verify if it's an instagram link
def isInstagram(string):
    return "instagram" in string.lower()