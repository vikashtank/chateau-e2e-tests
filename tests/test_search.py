from . import helpers


def test_group(selenium, organisation_name):
    group_name = "My Group"

    helpers.create_organisation_and_sign_in(selenium, name=organisation_name)
    helpers.create_group(selenium, name=group_name)

    # Go to homepage to avoid two links with the name 'My Group'
    helpers.click_link(selenium, text=organisation_name)

    helpers.find_element(selenium, "div", text="Search").click()
    helpers.fill_input(selenium, value=group_name, aria_label="Search")

    helpers.click_link(selenium, text=group_name)

    # Ensure group column is displayed
    helpers.find_element(selenium, "h5", text=group_name)
