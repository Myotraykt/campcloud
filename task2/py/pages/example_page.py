from playwright.sync_api import Page # type: ignore

class ExamplePage:
    def __init__(self, page: Page):
        self.page = page
        self.more_info_link = "a:has-text('More information')"

    def load(self):
        self.page.goto("https://example.com")
    
    def get_title(self) -> str:
        return self.page.title()
    
    def click_more_info(self):
        self.page.click(self.more_info_link)
    
    def get_current_url(self) -> str:
        return self.page.url