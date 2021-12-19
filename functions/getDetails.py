import Verification
from details import Details

def Get_Details(data_link):
    colors= Details.others.value['colors']
    logo=Details.others.value['logo']
    location= Details.others.value['location']

    if(Verification.isFacebook(data_link)):
        colors= Details.facebook.value['colors']
        logo =Details.facebook.value['logo']
        location= Details.facebook.value['location']
    elif(Verification.isGithub(data_link)):
        colors= Details.github.value['colors']
        logo =Details.github.value['logo']
        location= Details.github.value['location']
    elif(Verification.isInstagram(data_link)):
        colors= Details.instagram.value['colors']
        logo =Details.instagram.value['logo']
        location=Details.instagram.value['location']
    elif(Verification.isTwitter(data_link)):
        colors= Details.twitter.value['colors']
        logo =Details.twitter.value['logo']
        location= Details.twitter.value['location']

    return colors,logo, location