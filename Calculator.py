# Import dependencies
import flet as ft
import math


# Configure calculator landing page
def main(page: ft.Page):
    page.title = "Calculator"
    page.bgcolor = "#2d2d2d"
    page.window.width = 350
    page.window.height = 300

    values = ""  # variable initially empty

    # Configure result display
    result = ft.Text(value="0", size=28, color="white", text_align="right")

    # Function to receive input values
    def append_value(e):
        nonlocal values
        values += str(e.control.text)
        result.value = values
        page.update()

    # Function to clear values
    def clear_values(e):
        nonlocal values
        values = ""
        result.value = "0"
        page.update()

    # Function to evaluate expression
    def calculate(e):
        nonlocal values
        try:
            # Receiving the value and converting to str
            result.value = str(eval(values))
            values = result.value
        except:
            result.value = "Error"
            values = ""
        page.update()

    # Square root operation
    def square_root(e):
        nonlocal values
        conversion = float(values)
        result.value = math.sqrt(conversion)
        values = str(result.value)
        page.update()

    # Exponentiation operation (square)
    def square(e):
        nonlocal values
        conversion = float(values)
        result.value = conversion**2
        values = str(result.value)
        page.update()

    # Reciprocal operation (1/x)
    def reciprocal(e):
        nonlocal values
        conversion = float(values)
        result.value = float(1 / conversion)
        values = str(result.value)
        page.update()

    # Remove last digit
    def backspace(e):
        nonlocal values
        values = values[:-1]
        result.value = values or "0"
        page.update()

    # Result container configuration
    page = ft.Container(
        content=result,
        bgcolor="#37474F",
        padding=10,
        border_radius=10,
        height=70,
        alignment=ft.alignment.center_right,
    )

    # Number button style
    style_numbers = {
        "height": 60,
        "bgcolor": "#4d4d4d",
        "color": "white",
        "expand": 1,
    }

    # Operator button style
    style_operators = {
        "height": 60,
        "bgcolor": "#FF9500",
        "color": "white",
        "expand": 1,
    }

    # Clear button style
    style_clear = {
        "height": 60,
        "bgcolor": "#FF3B30",
        "color": "white",
        "expand": 1,
    }

    # Equal button style
    style_equal = {
        "height": 60,
        "bgcolor": "#34C759",
        "color": "white",
        "expand": 1,
    }

    # Define calculator buttons
    button_grid = [
        [
            ("%", style_operators, append_value),
            ("/", style_operators, append_value),
            ("*", style_operators, append_value),
            ("C", style_clear, clear_values),
        ],
        [
            ("⨉²", style_operators, square),
            ("√", style_operators, square_root),
            ("¹⁄ₓ", style_operators, reciprocal),
            ("CE", style_clear, backspace),
        ],
        [
            ("7", style_numbers, append_value),
            ("8", style_numbers, append_value),
            ("9", style_numbers, append_value),
            ("-", style_operators, append_value),
        ],
        [
            ("4", style_numbers, append_value),
            ("5", style_numbers, append_value),
            ("6", style_numbers, append_value),
            ("+", style_operators, append_value),
        ],
        [
            ("1", style_numbers, append_value),
            ("2", style_numbers, append_value),
            ("3", style_numbers, append_value),
            ("=", style_equal, calculate),
        ],
        [  # Style of the number 0
            ("0", {**style_numbers, "expand": 2}, append_value),
            (".", style_numbers, append_value),
            ("⌫", style_operators, backspace),
        ],
    ]

    buttons = []

    # Create buttons
    for line in button_grid:
        line_control = []
        for text, style, handler, *_ in line:
            btn = ft.ElevatedButton(
                text=text,
                on_click=handler,
                **style,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    padding=0,
                ),
            )
            line_control.append(btn)
        buttons.append(ft.Row(line_control, spacing=5))

    # Create main column
    page.add(ft.Column([page, ft.Column(buttons, spacing=5)]))


ft.app(target=main)
