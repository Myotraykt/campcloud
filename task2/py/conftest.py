import pytest
from playwright.sync_api import Playwright, Browser

@pytest.fixture(scope="session")
def browser(playwright: Playwright) -> Browser:
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()
