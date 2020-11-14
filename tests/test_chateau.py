import os
import uuid

import pytest

from .helpers import *


@pytest.fixture
def organisation_name():
    return str(uuid.uuid4())


@pytest.mark.nondestructive
def test_homepage(selenium, base_url):
    selenium.get(base_url)

    assert "Château" in selenium.title

    selenium.find_element_by_link_text("Sign in")
    selenium.find_element_by_link_text("Get started")


def test_get_started(selenium, base_url, organisation_name):
    selenium.get(base_url)

    create_organisation(selenium, name=organisation_name)

    selenium.find_element_by_xpath(
        f'//*[text()="Sign in to {organisation_name}"]',
    )


@pytest.mark.nondestructive
def test_sign_in(selenium, base_url):
    selenium.get(base_url)

    click_link(selenium, text="Sign in")

    fill_input(selenium, name="organisation", value="test")
    click_button(selenium, text="Sign in")

    fill_form(
        selenium, email_address="hello@orycion.com", password=os.environ["PASSWORD"]
    )
    click_button(selenium, text="Log In")

    selenium.find_element_by_xpath('//*[text()="test"]')
