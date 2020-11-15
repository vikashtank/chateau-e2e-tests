import os

import pytest


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(6)
    return selenium


@pytest.fixture
def chrome_options(chrome_options):
    if os.environ.get("CI"):
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-dev-shm-usage")
    return chrome_options


@pytest.fixture
def firefox_options(firefox_options):
    if os.environ.get("CI"):
        firefox_options.add_argument("--headless")
    return firefox_options
