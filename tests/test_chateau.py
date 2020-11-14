import os
import uuid

import pytest

from .helpers import *


@pytest.mark.nondestructive
def test_homepage(selenium, base_url):
    selenium.get(base_url)

    assert "Château" in selenium.title

    selenium.find_element_by_link_text("Sign in")
    selenium.find_element_by_link_text("Get started")


def test_get_started(selenium, base_url):
    selenium.get(base_url)

    click_link(selenium, text="Get started")

    organisation_name = str(uuid.uuid4())

    fill_form(
        selenium,
        name=organisation_name,
        owner_email_address="test@example.com",
        owner_password=str(uuid.uuid4()),
    )

    click_button(selenium, text="Let's go!")

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
