


class BaseLocator:
    def __init__(self):
        self.login = ('xpath', '//a[@class="userbar__button __active"]')
        self.banner = ('xpath','//a[@class="header__logo-link"]')
        self.contacts =('xpath', '//span[@class="site-menu__item"]/a[@href="/kontakty/"]')
