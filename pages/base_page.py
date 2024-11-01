from playwright.sync_api import Page, ElementHandle


class BasePage:

    def __init__(self, page:Page):
        self.page = page

    def open(self):
        self.page.goto(url="https://www.saraykina-numerolog.ru/index.html")

    def page_reload(self) -> str:
        self.page.reload()
        return "Page reload"

    def get_by_placeholder(self, text:str, exact: bool=True):
        locator = self.page.get_by_placeholder(text, exact=exact)
        assert locator is not None
        return locator
    def get_text_from_element(self, locator: str, timeout: int=30) -> str:
        element = self.wait_element(locator,timeout)
        assert element is not None
        text = self.page.evaluate('element => element.textContent', element)
        return text


    def get_current_url(self) -> str:
        return self.page.url

    def wait_element(self, locator:str, timeout: int=30) -> ElementHandle:
        return self.page.wait_for_selector(locator, timeout=timeout * 1000)

    def click_by_placeholder(self,text: str, exact: bool=True):
        locator = self.page.get_by_placeholder(text, exact=exact)
        locator.click()
        return locator

    def click_by_locator(self, locator: str, timeout: int = 30):
        element = self.wait_element(locator,timeout)
        if element and element.is_enabled():
            element.click()
            return element
        else:
            raise AssertionError(f"Element wait '{locator}'")
