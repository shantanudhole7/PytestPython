import pytest
from config.config import WEBFORMURL
from pages.practice_page import PracticePage
from tests.base_test import BaseTest, log_information, assert_displayed, assert_hidden


class TestElementDisplayedPage(BaseTest):

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

    @pytest.mark.description("Verify the text box is displayed when the page opens.")
    @pytest.mark.ui
    @pytest.mark.minor
    def test_textbox_displayed_by_default(self, practice_page):
        """@priority P4 @owner Shantanu @feature element-displayed"""
        log_information("Verify the text box is displayed")
        assert_displayed("Verify the text box is displayed", practice_page.input_hide_show_example)

    @pytest.mark.description("Verify clicking Hide hides the text box.")
    @pytest.mark.ui
    @pytest.mark.minor
    def test_textbox_hidden_after_hide(self, practice_page):
        """@priority P4 @owner Shantanu @feature element-displayed"""
        log_information("Click Hide")
        practice_page.click_button(practice_page.btn_hide)

        log_information("Verify the text box is hidden")
        assert_hidden("Verify the text box is hidden", practice_page.input_hide_show_example)

    @pytest.mark.description("Verify clicking Show after Hide displays the text box again.")
    @pytest.mark.ui
    @pytest.mark.minor
    def test_textbox_displayed_after_show(self, practice_page):
        """@priority P4 @owner Shantanu @feature element-displayed"""
        log_information("Click Hide")
        practice_page.click_button(practice_page.btn_hide)

        log_information("Verify the text box is hidden")
        assert_hidden("Verify the text box is hidden", practice_page.input_hide_show_example)

        log_information("Click Show")
        practice_page.click_button(practice_page.btn_show)

        log_information("Verify the text box is displayed again")
        assert_displayed("Verify the text box is displayed again", practice_page.input_hide_show_example)

