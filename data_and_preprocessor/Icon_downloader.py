import requests
from bs4 import BeautifulSoup
import os

url = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/profile-icons/"
save_dir = "lol_profile_icons"
os.makedirs(save_dir, exist_ok=True)

# 获取目录页面
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

# 找出所有 jpg / png 链接
links = [
    a["href"] for a in soup.find_all("a")
    if a.has_attr("href") and (a["href"].endswith(".png") or a["href"].endswith(".jpg"))
]

print(f"找到 {len(links)} 个头像文件")

for link in links:
    filename = link.split("/")[-1]
    img_url = url + filename
    print(f"Downloading {filename}")
    r = requests.get(img_url)
    with open(os.path.join(save_dir, filename), "wb") as f:
        f.write(r.content)
