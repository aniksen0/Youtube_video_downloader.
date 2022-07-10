from pages.base_page import BasePage
from utils import locators
from utils import testcase_data
from utils.openpyxlfunction import *
import time
from datetime import datetime
import pathlib
import os
import youtube_dl


class youtube(BasePage):
    def __init__(self, driver):
        self.locator = locators.YoutubeLocator
        self.filepath = pathlib.Path(__file__).parent.parent / f"utils/{testcase_data.filename}"
        self.channelsheet = testcase_data.channellist
        self.playlistsheet = testcase_data.playlist
        super(youtube, self).__init__(driver)

    def goto_channel(self, url):
        try:
            self.driver.get(url)
        except:
            print("URL isn't valid")

    def go_to_playlist(self):
        self.find_element2(*self.locator.playlist_locator).click()
        time.sleep(3)
        self.scroll_to_down()

    def playlist_downloader(self, playlist):
        # command = f"youtube-dl -o '{path}' --ignore-errors --format bestaudio --extract-audio --audio-format mp3 --audio-quality 160K --output '%(title)s.%(ext)s' --yes-playlist https://www.youtube.com/{playlist}"
        # command = f"youtube-dl -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re"

        command = f"youtube-dl -o'%(playlist)s/%(playlist_index)s-%(title)s.%(ext)s' {playlist}"
        os.system(command)
        time.sleep(5)

    def filter_channel_name(self, name):
        if "?" or "\\" or "/" or "*" or ":" or '"' or ">" or "<" in name:
            x = name.replace("?", "0")
            x = x.replace("\\", "o")
            x = x.replace("/", "o")
            x = x.replace("*", "o")
            x = x.replace(":", "o")
            x = x.replace("\"", "o")
            x = x.replace(">", "o")
            y = x.replace("<", "o")
            return y

    def channael_name(self):
        channelName = self.find_element2(*self.locator.channelName).text
        filtered_channel_name = self.filter_channel_name(channelName)
        return filtered_channel_name

    def collect_playlist_data(self):
        allplaylist = self.find_elements(*self.locator.allPlaylist)
        for playlist in allplaylist:
            channel_name1 = self.channael_name()
            playlist_name = playlist.find_element(*self.locator.playlistName).text
            playlist_url = playlist.find_element(*self.locator.PlaylistLink).get_attribute('href')
            print(playlist_name, playlist_url)
            data = [channel_name1, playlist_name, playlist_url]
            writecolautomatic(self.filepath, self.playlistsheet, data)

    def test_make_folder_and_download(self, channelname, url):
        print(f"this is url link {url}")
        path_play_list = pathlib.Path(__file__).parent.parent / f"videos/{channelname}"
        print(path_play_list)
        try:
            os.mkdir(path_play_list)
            os.chdir(path_play_list)
        except:
            print("couldn't make a folder reason: There could be existed folder please check")
            try:
                os.chdir(path_play_list)
            except:
                print("couldn't change the directory")
        self.playlist_downloader(url)

    def youtube_video_downloader(self):
        channelUrl = readallsheetdata(self.filepath, self.channelsheet, 1)
        totalplaylist = getRowCount(self.filepath, self.playlistsheet)
        for url in channelUrl:
            print("*" * 80)
            print(url)
            self.goto_channel(url)
            time.sleep(3)
            self.go_to_playlist()
            time.sleep(3)
            self.collect_playlist_data()
            time.sleep(1)
        for i in range(2, totalplaylist):
            channel_name = readData(self.filepath, self.playlistsheet, i, 1)
            url = readData(self.filepath, self.playlistsheet, i, 3)
            self.test_make_folder_and_download(channel_name, url)
