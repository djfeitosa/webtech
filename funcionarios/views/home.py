import flet as ft


def home(page: ft.Page, width: int, length: int):
    view = ft.View(route="/", controls=[ft.Text(value="Olá Mundo!!!")])
    return view
