import Verification
from details import Details
def QrCode(data_link):
    colors= ["#000000","#ffffff"]
    if(Verification.isFacebook(data_link)):
        colors= Details.facebook.value['colors']
    elif(Verification.isGithub(data_link)):
        colors= Details.github.value['colors']
    elif(Verification.isGithub(data_link)):
        colors= Details.github.value['colors']
    elif(Verification.isGithub(data_link)):
        colors= Details.github.value['colors']
    
    return colors


print(QrCode("facxxxebook.com"))