import flet as ft
import colors as cl

def blizz(page: ft.Page):
    page.title = "blizz"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 390
    page.window.height = 844
    page.bgcolor = '#CFF0D3'

    page.add(
        ft.Container(
            content =
            ft.Column(
                controls =[ 
                    ft.Text(
                        "WELCOME", 
                        size = 40, 
                        weight=ft.FontWeight.W_900, 
                        color = "#000000",
                        text_align = ft.TextAlign.CENTER
                    ),
                    ft.TextField(
                        width = 280,
                        height = 50,
                        bgcolor = "#E1F3E2",
                        border = ft.InputBorder.OUTLINE,
                        border_color = ft.Colors.TRANSPARENT,
                        border_radius = 10,
                        hint_text = "Username",
                        color = "#000000",
                    ),
                    ft.TextField(
                        width = 280,
                        height = 50,
                        bgcolor = "#E1F3E2",
                        border = ft.InputBorder.OUTLINE,
                        border_color = ft.Colors.TRANSPARENT,
                        border_radius = 10,
                        hint_text = "Password",
                        color = "#000000",
                    ),
                    ft.TextField(
                        width = 280,
                        height = 50,
                        bgcolor = "#E1F3E2",
                        border = ft.InputBorder.OUTLINE,
                        border_color = ft.Colors.TRANSPARENT,
                        border_radius = 10,
                        hint_text = "Number",
                        color = "#000000",
                    ),
                    ft.Checkbox(
                        label = "i agree to stuff",
                        label_style = ft.TextStyle(color = "#000000", weight = ft.FontWeight.BOLD),
                    ),
                    ft.Button(
                        "SIGN UP", 
                        width = 150,
                        height = 40,
                        elevation = 3,
                        bgcolor = "#D2F5D4",
                        on_click = lambda e: print("yur")
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
                spacing=15,
            )
        )
    )


ft.run(blizz)
