import requests
from bs4 import BeautifulSoup

# 定义要抓取的网页URL
url = 'https://www.massey.ac.nz'  # 替换成你想要抓取的网页地址

# 发送HTTP请求获取网页内容
response = requests.get(url)

# 检查是否成功获取网页
if response.status_code == 200:
    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 在这里可以使用soup对象来提取和处理网页上的数据
    # 例如，查找所有的链接：
    links = soup.find_all('a')

    # 打印找到的链接
    for link in links:
        print(link.get('href'))
else:
    print("无法获取网页内容。")
