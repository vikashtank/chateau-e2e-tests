import os

import pytest

from . import helpers


def test_get_started(selenium, base_url, organisation_name):
    selenium.get(base_url)

    helpers.create_organisation(selenium, name=organisation_name)

    selenium.find_element_by_xpath(
        f'//*[text()="Sign in to {organisation_name}"]',
    )


@pytest.mark.nondestructive
def test_sign_in(selenium, base_url):
    selenium.get(base_url)

    helpers.click_link(selenium, text="Sign in")

    helpers.fill_input(selenium, name="organisation", value="test")
    helpers.click_button(selenium, text="Sign in")

    helpers.sign_in(
        selenium, email_address="hello@orycion.com", password=os.environ["PASSWORD"]
    )

    selenium.find_element_by_xpath('//*[text()="test"]')
