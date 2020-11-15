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

    email_address = "test@example.com"
    password = str(uuid.uuid4())

    fill_form(
        selenium,
        name=name,
        owner_email_address=email_address,
        owner_password=password,
    )

    click_button(selenium, text="Let's go!")

    return email_address, password


def sign_in(selenium, *, email_address, password):
    fill_form(selenium, email_address=email_address, password=password)

    click_button(selenium, text="Log In")


def create_organisation_and_sign_in(selenium, *, name):
    email_address, password = create_organisation(selenium, name=name)
    sign_in(selenium, email_address=email_address, password=password)
