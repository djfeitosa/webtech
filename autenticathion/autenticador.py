import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.window.maximizable = True
    page.window.resizable = False

    def logar(e):
        page.remove(register)
        page.add(login)
        page.update()

    def register(e):
        page.remove(login)
        page.add(register)
        page.update()

    def open_msgbox(e):
        page.dialog = MsgBox
        MsgBox.open = True
        page.update()

    def close_msgbox(e):
        MsgBox.open = False
        page.update()

    MsgBox = ft.AlertDialog(
        content=ft.Container(
            width=260,
            height=30,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(ft.icons.CANCEL, size=30, color=ft.Colors.RED),
                            ft.Text(
                                value="Email ou senha incorretos",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                            ),
                        ],
                        spacing=5,
                    )
                ]
            ),
        ),
        actions=[ft.TextButton(text="OK", on_click=close_msgbox)],
    )

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
                                                bgcolor=ft.Colors.GREEN_100,
                                                # on_hover=on_over_sigin,
                                                width=300,
                                                height=40,
                                                style=ft.ButtonStyle(
                                                    overlay_color=ft.Colors.GREEN_200
                                                ),
                                                on_click=open_msgbox,
                                            ),
                                            ft.Row(
                                                [
                                                    ft.TextButton(
                                                        "Recuperar sua senha"
                                                    ),
                                                    ft.TextButton(
                                                        "Criar nova conta",
                                                        on_click=register,
                                                    ),
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
    register = ft.Column(
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
                            height=450,
                            border_radius=10,
                            content=ft.Column(
                                [
                                    ft.Container(
                                        padding=ft.padding.only(top=10, bottom=12),
                                        content=ft.Column(
                                            [
                                                ft.Text(
                                                    value="Register",
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
                                                hint_text="Primeiro nome",
                                                width=300,
                                                height=40,
                                                border_radius=ft.border_radius.all(40),
                                                prefix_icon=ft.Icons.PERSON,
                                                keyboard_type=ft.KeyboardType.NAME,
                                                text_vertical_align=1,
                                            ),
                                            ft.TextField(
                                                hint_text="Segundo nome",
                                                width=300,
                                                height=40,
                                                border_radius=ft.border_radius.all(40),
                                                prefix_icon=ft.Icons.PERSON,
                                                keyboard_type=ft.KeyboardType.NAME,
                                                text_vertical_align=1,
                                            ),
                                            ft.TextField(
                                                hint_text="Digite seu e-mail",
                                                width=300,
                                                height=40,
                                                border_radius=ft.border_radius.all(40),
                                                prefix_icon=ft.Icons.EMAIL,
                                                keyboard_type=ft.KeyboardType.EMAIL,
                                                text_vertical_align=1,
                                            ),
                                            ft.TextField(
                                                hint_text="Digite seu telefone",
                                                width=300,
                                                height=40,
                                                border_radius=ft.border_radius.all(40),
                                                prefix_icon=ft.Icons.PHONE,
                                                keyboard_type=ft.KeyboardType.PHONE,
                                                text_vertical_align=1,
                                            ),
                                            ft.TextField(
                                                hint_text="Digite sua senha",
                                                width=300,
                                                height=40,
                                                border_radius=ft.border_radius.all(40),
                                                prefix_icon=ft.Icons.LOCK,
                                                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                                                password=True,
                                                text_vertical_align=1,
                                            ),
                                            ft.TextField(
                                                hint_text="Confirme sua senha",
                                                width=300,
                                                height=40,
                                                border_radius=ft.border_radius.all(40),
                                                prefix_icon=ft.Icons.LOCK,
                                                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                                                password=True,
                                                text_vertical_align=1,
                                            ),
                                            ft.ElevatedButton(
                                                text="Register",
                                                bgcolor=ft.Colors.GREEN_100,
                                                style=ft.ButtonStyle(
                                                    overlay_color=ft.Colors.GREEN_200
                                                ),
                                                width=300,
                                                height=40,
                                            ),
                                            ft.Row(
                                                [
                                                    ft.TextButton(
                                                        "Recuperar sua senha"
                                                    ),
                                                    ft.TextButton(
                                                        "Já tenho uma conta",
                                                        on_click=logar,
                                                    ),
                                                ],
                                                width=300,
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            ),
                                        ],
                                        spacing=8,
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

    def resize_controls(e):
        login.controls[0].width = page.window_width - 10
        login.controls[0].height = page.window_height - 60

        register.controls[0].width = page.window_width - 10
        register.controls[0].height = page.window_height - 60

        page.update()

    page.on_resize = resize_controls

    page.add(login)


if __name__ == "__main__":
    ft.app(target=main)
