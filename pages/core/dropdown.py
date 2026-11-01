from playwright.sync_api import Locator
from pages.core.base_element import BaseElement


class Dropdown(BaseElement):
    def __init__(self, locator: Locator):
        super().__init__(locator)

    def select_by_label(self, label: str):
        """
        Select an option by its visible text (label).

        Args:
            label: The visible text of the option to select, e.g. "Option1".
        """
        self.locator.select_option(label=label)

    def select_by_value(self, value: str):
        """
        Select the option with the given value attribute.

        Args:
            value (str): Value attribute of the option, e.g. "option1".
        """
        self.locator.select_option(value=value)

    def select_by_index(self, index: int):
        """
        Select the option at the given position (0 is the first option).

        Args:
            index (int): Position of the option.
        """
        self.locator.select_option(index=index)

    def get_selected_option(self) -> str:
        """
        Get the visible text of the selected option.

        Returns:
            str: Visible text of the selected option, e.g. "Option1".
        """
        return self.locator.locator("option:checked").inner_text().strip()

    def get_selected_value(self) -> str:
        """
        Get the value attribute of the selected option.

        Returns:
            str: Value of the selected option, e.g. "option1".
        """
        return self.locator.input_value()

    def get_all_options(self) -> list[str]:
        """
        Get the visible text of every option, in page order.

        Returns:
            list[str]: Option texts, e.g. ["Select", "Option1", "Option2", "Option3"].
        """
        return [_label.strip() for _label in self.locator.locator("option").all_inner_texts()]
