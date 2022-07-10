from selenium.webdriver.common.by import By


class YoutubeLocator(object):
    playlist_locator = (By.XPATH, "//tp-yt-app-header/div[@id='contentContainer']/tp-yt-app-toolbar[1]/div[1]/div[1]/tp-yt-paper-tabs[1]/div[1]/div[1]/tp-yt-paper-tab[3]/div[1]")
    allPlaylist = (By.XPATH, '//ytd-grid-playlist-renderer[@class="style-scope ytd-grid-renderer"]')
    playlistName = (By.XPATH, './/a[@id="video-title"]')
    PlaylistLink = (By.XPATH, './/a[@class="yt-simple-endpoint style-scope yt-formatted-string"]')
    channelName = (By.XPATH, "//div[@id='inner-header-container']//div[@id='meta']//ytd-channel-name[@id='channel-name']//div[@id='container']//div[@id='text-container']//yt-formatted-string[@id='text']")
