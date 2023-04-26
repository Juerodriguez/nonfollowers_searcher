from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import getpass
import argparse

BROWSER = webdriver.Chrome()
BROWSER.implicitly_wait(5)


def get_followers(username: str):
    BROWSER.get(f"https://www.instagram.com/{username}/followers/")
    sleep(5)
    scroll_page()
    html_source = BROWSER.page_source
    soup = BeautifulSoup(html_source, 'lxml')
    soup_list = soup.findAll("div", class_="_ab8w _ab94 _ab97 _ab9f _ab9k _ab9p _ab9- _aba8 _abcm")
    listfollowers = [soup_element.find("a")["href"] for soup_element in soup_list]
    return listfollowers


def get_following(username: str):
    BROWSER.get(f"https://www.instagram.com/{username}/following/")
    sleep(5)
    scroll_page()
    html_source = BROWSER.page_source
    soup = BeautifulSoup(html_source, 'lxml')
    soup_list = soup.findAll("div", class_="_ab8w _ab94 _ab97 _ab9f _ab9k _ab9p _ab9- _aba8 _abcm")
    listfollowing = [soup_element.find("a")["href"] for soup_element in soup_list]
    return listfollowing


def scroll_page():
    flag = True
    while flag:
        try:
            element = BROWSER.find_element(By.CLASS_NAME, "_aanq")
            BROWSER.execute_script("arguments[0].scrollIntoView();", element)
            sleep(5)
        except:
            break


def login(username: str, password: str):
    username_input = BROWSER.find_element(By.CSS_SELECTOR, "input[name='username']")
    password_input = BROWSER.find_element(By.CSS_SELECTOR, "input[name='password']")
    username_input.send_keys(username)
    password_input.send_keys(password)
    sleep(2)
    login_button = BROWSER.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()


def run_searcher(username: str, password: str):
    BROWSER.get('https://www.instagram.com/')
    sleep(2)
    login(username, password)
    sleep(15)
    list_followers = get_followers(username)
    list_following = get_following(username)
    nonfollowers = set(list_following) - set(list_followers)
    print(nonfollowers)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="Username to login", required=True)
    password = getpass.getpass('Ingrese la contraseña: ')

    args = parser.parse_args()
    run_searcher(args.username, password)


if __name__ == "__main__":
    main()
