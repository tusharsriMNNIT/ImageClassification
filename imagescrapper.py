import os
import requests
from bs4 import BeautifulSoup

link1 = "https://www.google.com/search?q="
link2 = "&sxsrf=ALeKk00aZwqY0wlv9MGBLYYnyCTpX2vuGg:1592898314788&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj0iN3RuJfqAhVH_XMBHRFfBGUQ_AUoAnoECB0QBA&biw=1366&bih=659"

celb = ['lionel_messi','serena_williams','virat_kohli','rohit_sharma','maria_sharapova','roger_federer']
urls = []
parent = "/home/coder/Desktop/ImageClassification/images_dataset"

for val in celb:
    s = val.split('_')
    url = link1 + s[0] + "+" + s[1] + link2
    urls.append(url)

for i,url in enumerate(urls):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    img = soup.find_all('img')


    new_par = parent + "/" + str(celb[i])
    if os.path.isdir(new_par)==False:
        os.makedirs(new_par)

    for ind,val in enumerate(img):
        if ind==0:
            continue
        try:
            r = requests.get(val.get('src'), stream = True) 
        except:
            print('unable to get image')

        child = new_par + "/" + str(ind) + ".jpg"
        with open(child,"wb") as pdf: 
            for chunk in r.iter_content(chunk_size=1024):
                if chunk: 
                    pdf.write(chunk) 
