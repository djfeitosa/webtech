import flet as ft
from flet import Colors


def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.window.maximizable = True
    page.window.resizable = False

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
                            bgcolor=ft.Colors.WHITE70,
                            width=400,
                            height=320,
                            border_radius=10,
                            content=ft.Column(
                                [
                                    ft.Container(
                                        padding=ft.padding.only(top=10, bottom=12),
                                        content=ft.Column(
                                            [
                                                ft.Text(
                                                    value="Sign-in",
                                                    weight=ft.FontWeight.BOLD,
                                                    size=20,
                                                )
                                            ]
                                        ),
                                    ),
                                    ft.Column(
                                        [
                                            ft.TextField(
                                                autofocus=True,
                                                hint_text="Digite o seu email",
                                                width=300,
                                                height=40,
                                                border_radius=ft.border_radius.all(40),
                                                prefix_icon=ft.Icons.PERSON,
                                                keyboard_type=ft.KeyboardType.EMAIL,
                                                text_vertical_align=1,
                                            ),
                                            ft.TextField(
                                                autofocus=True,
                                                hint_text="Digite sua senha",
                                                width=300,
                                                height=40,
                                                border_radius=ft.border_radius.all(40),
                                                prefix_icon=ft.Icons.LOCK,
                                                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                                                password=True,
                                                text_vertical_align=1,
                                            ),
                                            ft.ElevatedButton(
                                                text="Sign-in",
                                                bgcolor=Colors.GREEN_100,
                                                on_hover=Colors.GREEN_200,
                                                width=300,
                                                height=40,
                                            ),
                                            ft.Row(
                                                [
                                                    ft.TextButton(
                                                        "Recuperar sua senha"
                                                    ),
                                                    ft.TextButton("Criar nova conta"),
                                                ],
                                                width=300,
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            ),
                                        ],
                                        spacing=10,
                                    ),
                                    ft.Row(
                                        [
                                            ft.IconButton(icon=ft.Icons.EMAIL),
                                            ft.IconButton(icon=ft.Icons.FACEBOOK),
                                            ft.IconButton(icon=ft.Icons.TELEGRAM),
                                        ],
                                        alignment="center",
                                    ),
                                ],
                                horizontal_alignment="center",
                            ),
                        )
                    ],
                    horizontal_alignment="center",
                    alignment="center",
                ),
            )
        ]
    )

    register = ft.Column([])

    page.add(login)


if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)
