from lesson20.factoey_example.edge import EdgeBrowser
from lesson20.factoey_example.firefox import FirefoxBrowser
from lesson20.factoey_example.chrome import ChromeBrowser


class BrowserFactory:
    def __init__(self):
        self.__last_browser = None

    def get_browser(self, name:str):
        if name == 'Chrome':
            return ChromeBrowser()
        if name == 'Firefox':
            return FirefoxBrowser()
        if name == 'Edge':
            return EdgeBrowser()
        else:
            raise Exception('You entered wrong browser name')





