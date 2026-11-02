import pytest

from tests.base_test import BaseTest, log_information, assert_displayed, assert_hidden


class TestElementDisplayedPage(BaseTest):

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
