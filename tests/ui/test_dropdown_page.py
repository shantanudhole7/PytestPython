import pytest
from config.config import WEBFORMURL
from pages.practice_page import PracticePage
from tests.base_test import BaseTest, log_information, assert_equal, assert_selected


class TestDropdownPage(BaseTest):
    """
    Tests for the static dropdown on the Automation Practice page (WEBFORMURL).
    """

    EXPECTED_OPTIONS = ["Select", "Option1", "Option2", "Option3"]
    OPTIONS = [("Option1", "option1"), ("Option2", "option2"), ("Option3", "option3")]

    @pytest.fixture
    def url(self):
        """
        Open the Automation Practice page instead of the default PRACTICEURL.
        """
        return WEBFORMURL

    @pytest.fixture
    def practice_page(self, navigate_url) -> PracticePage:
        """
        Open WEBFORMURL and return it as a PracticePage.

        Args:
            navigate_url: The shared tab, already on WEBFORMURL.

        Returns:
            PracticePage: The practice page object.
        """
        return PracticePage(navigate_url)

    @pytest.mark.description("Verify an option can be selected in the dropdown by its visible text.")
    @pytest.mark.ui
    @pytest.mark.minor
    @pytest.mark.parametrize("_option_name, _option_value", OPTIONS)
    def test_dropdown_select_by_label(self, practice_page, _option_name, _option_value):
        """@priority P4 @owner Shantanu @feature dropdown"""
        log_information(f"Select '{_option_name}' from the dropdown by its visible text")
        practice_page.select_by_label(practice_page.drp_options, _option_name)

        log_information("Verify the selected option's text and value")
        assert_selected(f"Verify {_option_name} is selected", practice_page.drp_options, _option_value)
        assert_equal(f"Verify selected option text is {_option_name}", _option_name,
                     practice_page.drp_options.get_selected_option())

    @pytest.mark.description("Verify an option can be selected in the dropdown by its value attribute.")
    @pytest.mark.ui
    @pytest.mark.minor
    @pytest.mark.parametrize("_option_name, _option_value", OPTIONS)
    def test_dropdown_select_by_value(self, practice_page, _option_name, _option_value):
        """@priority P4 @owner Shantanu @feature dropdown"""
        log_information(f"Select '{_option_value}' from the dropdown by its value")
        practice_page.select_by_label(practice_page.drp_options, _option_name)

        log_information("Verify the selected option's text and value")
        assert_selected(f"Verify {_option_name} is selected", practice_page.drp_options, _option_value)
        assert_equal(f"Verify selected option text is {_option_name}", _option_name,
                     practice_page.drp_options.get_selected_option())

    @pytest.mark.description("Verify the dropdown lists the expected options in order.")
    @pytest.mark.ui
    @pytest.mark.minor
    def test_dropdown_options(self, practice_page):
        """@priority P4 @owner Shantanu @feature dropdown"""
        log_information("Read all options from the dropdown")
        _all_options = practice_page.drp_options.get_all_options()

        log_information("Verify the dropdown options")
        assert_equal("Verify the dropdown options", self.EXPECTED_OPTIONS, _all_options)
