import flet as ft

from views.home import home


def main(page: ft.Page):
    page.title = page.route

    WIDTH = page.width
    HEIGHT = page.height

    def router(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(home(page, WIDTH, HEIGHT))

        page.title = page.route
        page.add(ft.Text(value="Página Inicial", color=ft.Colors.BLACK))

    page.on_route_change = router
    page.go(page.route)


if __name__ == "__main__":
    ft.app(target=main)
     #ft.app(target=main, view=ft.WEB_BROWSER)
