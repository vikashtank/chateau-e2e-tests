import uuid


def click_link(selenium, *, text):
    element = selenium.find_element_by_link_text(text)
    element.click()


def click_button(selenium, *, text):
    element = selenium.find_element_by_xpath(f'//button[text()="{text}"]')
    element.click()


def fill_input(selenium, *, name, value):
    element = selenium.find_element_by_name(name)
    element.send_keys(value)


def fill_form(selenium, **kwargs):
    for key, value in kwargs.items():
        fill_input(selenium, name=key, value=value)


def create_organisation(selenium, *, name):
    click_link(selenium, text="Get started")

    fill_form(
        selenium,
        name=name,
        owner_email_address="test@example.com",
        owner_password=str(uuid.uuid4()),
    )

    click_button(selenium, text="Let's go!")
