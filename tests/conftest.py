import os
import uuid

import pytest


@pytest.fixture()
def organisation_name():
    return str(uuid.uuid4())


@pytest.fixture
def selenium(selenium, base_url):
    selenium.implicitly_wait(6)
    selenium.get(base_url)
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
