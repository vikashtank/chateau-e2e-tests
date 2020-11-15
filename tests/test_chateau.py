import os
import time
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

    sign_in(
        selenium, email_address="hello@orycion.com", password=os.environ["PASSWORD"]
    )

    selenium.find_element_by_xpath('//*[text()="test"]')


def test_subscribe(selenium, base_url, organisation_name):
    selenium.get(base_url)

    create_organisation_and_sign_in(selenium, name=organisation_name)

    click_link(selenium, text="Settings")

    click_button(selenium, text="Change payment details")

    selenium.switch_to.frame(selenium.find_element_by_xpath("//iframe"))

    fill_form(
        selenium,
        cardnumber="4242424242424242",
        cvc="123",
        postal="12345",
        **{"exp-date": "10 / 30"},
    )

    selenium.switch_to.default_content()

    selenium.find_element_by_xpath(f'(//button[text()="Save"])[2]').click()

    selenium.find_element_by_xpath('//*[text()="Success!"]')
