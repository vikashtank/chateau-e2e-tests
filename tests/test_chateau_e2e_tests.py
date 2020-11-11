import pytest


@pytest.mark.nondestructive
def test_homepage(selenium, base_url):
    selenium.get(base_url)

    assert "Château" in selenium.title

    selenium.find_element_by_link_text("Sign in")
    selenium.find_element_by_link_text("Get started")
