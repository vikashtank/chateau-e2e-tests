import uuid


def get_element(selenium, type, text=None, aria_label=None, name=None):
    if text is not None:
        return selenium.find_element_by_xpath(f'//{type}[.="{text}"]')
    elif aria_label is not None:
        return selenium.find_element_by_xpath(f'//{type}[@aria-label="{aria_label}"]')
    elif name is not None:
        return selenium.find_element_by_xpath(f'//{type}[@name="{name}"]')
    else:
        raise ValueError(
            "Invalid argument provided, please ensure either aria_label or text is given"
        )


def click_link(selenium, *args, **kwargs):
    get_element(selenium, "a", *args, **kwargs).click()


def click_button(selenium, *args, **kwargs):
    get_element(selenium, "button", *args, **kwargs).click()


def fill_input(selenium, *, value, **kwargs):
    get_element(selenium, "input", **kwargs).send_keys(value)


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
