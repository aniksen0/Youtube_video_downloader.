from pages.signin_page import SignInPage
from functionality.base_test import BaseTest
from pages.yotube_page import youtube


class TestVerifyDownloadYoutubeVideo(BaseTest):
    def test_download_video(self):
        page1 = youtube(self.driver)
        page1.youtube_video_downloader()

# python3 -m unittest functionality.test1
# python3 -m pytest -s functionality/youtube_video_download_function.py --alluredir=ReportAllure &&  allure serve ReportAllure/
