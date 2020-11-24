from pathlib import Path

from . import helpers


def test_change_logo(selenium, organisation_name):
    helpers.create_organisation_and_sign_in(selenium, name=organisation_name)

    helpers.click_link(selenium, text="Settings")

    helpers.fill_form(
        selenium,
        file=str(Path(__file__).parent.parent / "fixtures" / "logo.png"),
    )

    selenium.find_element_by_xpath('//button[text()="Upload"]').click()

    selenium.find_element_by_xpath('//*[text()="Success!"]')

    selenium.find_element_by_xpath('//*[@class="navbar-brand"]//img')


def test_payment_subscribe(selenium, organisation_name):
    helpers.create_organisation_and_sign_in(selenium, name=organisation_name)

    helpers.click_link(selenium, text="Settings")

    helpers.click_button(selenium, text="Change payment details")

    selenium.switch_to.frame(selenium.find_element_by_xpath("//iframe"))

    helpers.fill_form(
        selenium,
        cardnumber="4242424242424242",
        cvc="123",
        postal="12345",
        **{"exp-date": "10 / 30"},
    )

    selenium.switch_to.default_content()

    selenium.find_element_by_xpath('//button[text()="Save"]').click()

    selenium.find_element_by_xpath('//*[text()="Success!"]')
