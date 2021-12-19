#isFacebook : verify if it's a facebook link
def isFacebook(string):
    if ("facebook" in string.lower() or "fb" in string.lower()):
        return True
    else : 
        return False

#isTwitter : verify if it's a twitter link
def isTwitter(string):
    if("twitter" in string.lower()):
        return True
    else:
        return False

#isGithub : verify if it's a github link
def isGithub(string):
    if("github" in string.lower()):
        return True
    else:
        return False