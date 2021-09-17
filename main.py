"""
Get github username from user and print github image url and its public repos 
"""

from typing import List
import requests
from bs4 import BeautifulSoup

# locators
LIST = 'div ul li.col-12.d-flex.width-full.py-4.border-bottom.color-border-secondary.public'
NAME = 'h3.wb-break-all a'


def getContent(username):
    url = f"https://github.com/{username}?tab=repositories"
    r = requests.get(url)

    if r.status_code != 200:
        raise RuntimeError("Github user not found. Pls enter correct username")

    return r.content


def printImg(soup):
    print("")
    img = soup.find('img', {'alt': 'Avatar'})
    if not img:
        print("Image not found")
    else:
        print("Image url : ", img.get('src'), "\n")


def printRepo(soup):

    list = soup.select(LIST)
    print("Total Repo ", len(list))
    print("Repo list : \n")
    for l in list:
        repo = l.select_one(NAME)
        print(repo.string.strip())


def main():
    reponame = input("Enter git hub user name ")

    if reponame == None or reponame == "":
        raise ValueError("Name is required")

    content = getContent(reponame)
    soup = BeautifulSoup(content, 'html.parser')
    printImg(soup)
    printRepo(soup)


if __name__ == '__main__':
    main()
