import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.window.maximizable = True
    page.window.resizable = False

    def on_over_sigin(e):
        e.control.bgcolor = ft.Colors.YELLOW
        e.control.update()

    login = ft.Column(
        [
            ft.Container(
                bgcolor=ft.Colors.GREEN_200,
                width=page.window.width - 10,
                height=page.window.height - 60,
                border_radius=10,
                content=ft.Column(
                    [
                        ft.Container(
                            bgcolor=ft.Colors.BLACK,
                            width=400,
                            height=320,
                            border_radius=10,
                            # content=ft.Text(
                            #     value="Sign-in",
                            #     weight=ft.FontWeight.BOLD,
                            #     size=20,
                            # ),
                        ),
                    ],
                ),
            ),
            ft.Text(value="Teste"),
        ]
    )

    register = ft.Column([])

    page.add(login)


if __name__ == "__main__":
    ft.app(target=main)
