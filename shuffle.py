import os
import time
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver import ActionChains
    from selenium.webdriver.common.actions.action_builder import ActionBuilder
    from pytube import Playlist
    from art import *
    import numpy 
except ModuleNotFoundError:
    os.system('pip install selenium')
    os.system('pip install webdriver-manager')
    os.system('pip install pytube')
    os.system('pip install art')
    os.system('pip install numpy')

print("Playlist Bot")
print("PEBBING OUT")
print("------------------------------------------")


def get_playlist(playlists):
    urls = []

    for playlist in playlists:
        playlist_urls = Playlist(playlist)

        for url in playlist_urls:
            urls.append(url)
    return urls

playlists = []
video_links = get_playlist(playlists)
numpy.random.shuffle(video_links)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

room = input("Name of room: ")

driver.get(f"https://jukebox.today/{room}")

driver.maximize_window()
time.sleep(0.5)


search_bar = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[1]/input")
action = ActionBuilder(driver)
for x in video_links:
    search_bar.send_keys(x)
    search_bar.send_keys(Keys.ENTER)
    time.sleep(0.3)
    action.pointer_action.move_to_location(980,171)
    action.pointer_action.click()
    action.perform()
    search_bar.clear()