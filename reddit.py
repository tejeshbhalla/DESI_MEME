from request_reddit_token import recieve_token
import requests
import os 
import shutil 

header=""
def refresh_header():
  global header
  header=recieve_token()

def save_file(name,content):
  path=f"images/{name}"
  if not os.path.isfile(path):
    f=open(path,"wb")
    f.write(content)
    return True,path
  return False,None


def images_folder_refresh():
  print(len(os.listdir("images/")))
  if  len(os.listdir("images/"))>100:
    shutil.rmtree("images/")
    os.mkdir("images/")
  return


def req_memes(subreddit):
  refresh_header()
  images_folder_refresh()

  res = requests.get(f"https://oauth.reddit.com/r/{subreddit}/hot",
                    headers=header)

  for post in res.json()["data"]["children"]:
    id=post['data']['id']
    image_url=post['data']['url']
    if  ".jpg" in image_url: 
      uri=f"{id}_.jpg"
      r=requests.get(image_url)
      cond,path=save_file(uri,r.content)
      if cond:
        return path
      else:
        continue



  
  