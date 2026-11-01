from pages.base_page import BasePage
from pages.core.base_element import BaseElement
from pages.core.checkbox import Checkbox
from pages.core.dropdown import Dropdown
from pages.core.radio import Radio


class PracticePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.rdo_radio_1 = Radio(page.locator("input[type='radio'][value='radio1']"))
        self.rdo_radio_2 = Radio(page.locator("input[type='radio'][value='radio2']"))
        self.rdo_radio_3 = Radio(page.locator("input[type='radio'][value='radio3']"))
        self.chk_checkbox_1 = Checkbox(page.locator("#checkBoxOption1"))
        self.chk_checkbox_2 = Checkbox(page.locator("#checkBoxOption2"))
        self.chk_checkbox_3 = Checkbox(page.locator("#checkBoxOption3"))
        self.drp_options = Dropdown(page.locator("select[name='dropdown-class-example']"))

    # noinspection PyMethodMayBeStatic
    def check_radio(self, radio: Radio) -> None:
        """
        Check the given radio button.

        Args:
           radio (Radio): The radio button to check, e.g. self.rdo_radio_1.
        """
        radio.check()

    # noinspection PyMethodMayBeStatic
    def is_checked(self, base_element: BaseElement) -> bool:
        """
        Check the given element is checked.

        Args:
            base_element (BaseElement): The element to check, e.g. self.rdo_radio_1.
        Returns:
            bool: True if the element is checked, False otherwise.
        """
        return base_element.is_checked()

    # noinspection PyMethodMayBeStatic
    def check_checkbox(self, checkbox: Checkbox) -> None:
        """
        Check the given checkbox.

        Args:
           checkbox (Checkbox): The Checkbox button to check, e.g. self.chk_checkbox_1.
        """
        checkbox.check()

    # noinspection PyMethodMayBeStatic
    def uncheck_checkbox(self, checkbox: Checkbox) -> None:
        """
        Un-check the given checkbox.

        Args:
           checkbox (Checkbox): The Checkbox button to check, e.g. self.chk_checkbox_1.
        """
        checkbox.uncheck()

    # noinspection PyMethodMayBeStatic
    def select_by_label(self, dropdown: Dropdown, label: str) -> None:
        """
        Select an option in the given dropdown by its visible text.

        Args:
            dropdown (Dropdown): The dropdown to use, e.g. self.drp_options.
            label (str): Visible text of the option, e.g. "Option2".
        """
        dropdown.select_by_label(label)

     # noinspection PyMethodMayBeStatic
    def select_by_value(self, dropdown: Dropdown, value: str) -> None:
        """
        Select an option in the given dropdown by its value attribute.

        Args:
            dropdown (Dropdown): The dropdown to use, e.g. self.drp_options.
            value (str): Value attribute of the option, e.g. "option2".
        """
        dropdown.select_by_value(value)

