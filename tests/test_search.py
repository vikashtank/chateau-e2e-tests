from . import helpers


def search(selenium, *, value):
    helpers.get_element(selenium, "div", text="Search").click()
    helpers.fill_input(selenium, value=value, aria_label="Search")


def test_finds_property(selenium, organisation_name):
    group_name = "My Group"

    helpers.create_organisation_and_sign_in(selenium, name=organisation_name)
    helpers.create_group(selenium, name=group_name)

    # Go to homepage to avoid two links with the name 'My Group'
    helpers.click_link(selenium, text="Château")

    search(selenium, value=group_name)

    helpers.click_link(selenium, text=group_name)

    # test group column is displayed
    helpers.get_element(selenium, "h5", text=group_name)
