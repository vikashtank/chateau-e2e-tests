import uuid

import pytest


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    return selenium


@pytest.mark.nondestructive
def test_homepage(selenium, base_url):
    selenium.get(base_url)

    assert "Château" in selenium.title

    selenium.find_element_by_link_text("Sign in")
    selenium.find_element_by_link_text("Get started")


def test_get_started(selenium, base_url):
    selenium.get(base_url)

    selenium.find_element_by_link_text("Get started").click()

    organisation_name = str(uuid.uuid4())
    name_input = selenium.find_element_by_name("name")
    name_input.send_keys(organisation_name)

    email_address_input = selenium.find_element_by_name("owner_email_address")
    email_address_input.send_keys("test@example.com")

    password_input = selenium.find_element_by_name("owner_password")
    password_input.send_keys(str(uuid.uuid4()))

    submission_button = selenium.find_element_by_xpath('//button[text()="Let\'s go!"]')
    submission_button.click()

    selenium.find_element_by_xpath(
        f'//*[text()="Sign in to {organisation_name}"]',
    )
