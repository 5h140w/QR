import Verification
from details import Details
def QrCode(data_link):
    colors= ["#000000","#ffffff"]
    logo=""
    if(Verification.isFacebook(data_link)):
        colors= Details.facebook.value['colors']
        logo =Details.facebook.value['logo']
    elif(Verification.isGithub(data_link)):
        colors= Details.github.value['colors']
        logo =Details.github.value['logo']
    elif(Verification.isInstagram(data_link)):
        colors= Details.instagram.value['colors']
        logo =Details.instagram.value['logo']
    elif(Verification.isTwitter(data_link)):
        colors= Details.twitter.value['colors']
        logo =Details.twitter.value['logo']
    

print(QrCode("facxxxebook.com"))