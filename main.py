import flet as ft
import colors as cl
import os

save = os.path.join(os.path.dirname(__file__), "solde.txt")

if os.path.exists(save):
    with open(save) as f:
        content = f.read().strip()
        if content: 
            solde = int(content)
        else:
            solde = 30000 
else:
    solde = 30000

names = [
        {"num": "773734049", "name": "moussa"},
        {"num": "756700056", "name": "youssou"},
        {"num": "707857890", "name": "sabelle"},
        {"num": "704505623", "name": "abdou"},
        {"num": "789083067", "name": "khady"}
]


def main(page: ft.Page):
    page.title = "Flet Navigation Bar Demo"
    page.window.width = 360
    page.window.height = 260 
    page.bgcolor = cl.ap

    result = ft.Container(width = 200)

    def add():
        global solde
        solde += 5000
        for t in balance_text:
            t.value = str(solde)
        print(solde)
        with open(save, "w") as f:
            f.write(str(solde))
        page.update()

    def validate(e):
        global solde
        if solde > int(montant.value) and int(montant.value) >= 5:
            if num.value and montant.value:
                page.show_dialog(dialog)
                solde -= int(montant.value)
                for t in balance_text:
                    t.value = str(solde)
                print(solde)
                montant.value = ""
                num.value = ""
                with open(save, "w") as f:
                    f.write(str(solde))
                page.update()
        else:
            page.show_dialog(error)

    def achat(e):
        global solde
        if solde > int(credit.value) and int(credit.value) >= 5:
            if credit.value:
                page.show_dialog(dialog)
                solde -= int(credit.value)
                for t in balance_text:
                    t.value = str(solde)
                with open(save, "w") as f:
                    f.write(str(solde))
                page.update()
        else:
            page.show_dialog(error)

    balance_text = []

    def card():
        balance = ft.Text(f"{str(solde)}", color=cl.bt, weight=ft.FontWeight.W_900, size=30, margin = ft.Margin.only(right = 0, left = 10))
        balance_text.append(balance)
        return(
            ft.Container(
                width = 2000,
                height = 190,
                bgcolor = cl.bg,
                border_radius = 20,
                margin = ft.Margin.only(top = 20),
                content = 
                ft.Column(
                    controls = [
                        ft.Row(
                            controls = [
                                ft.Text(
                                    "SOLDE",
                                    color = cl.btx,
                                    weight = ft.FontWeight.W_500,
                                    margin = ft.Margin.only(top = 20, left = 20),
                                ),
                                ft.IconButton(
                                    icon = ft.CupertinoIcons.EYE,
                                    icon_color = cl.btx,
                                    margin = ft.Margin.only(left = 200, top = 20)
                                )
                            ]
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                            spacing = 5,
                            controls = [
                                ft.Container(balance),
                                ft.Text("FCFA", color=cl.bt, weight=ft.FontWeight.W_900, size=30, margin = ft.Margin.only(right = 70, left = 0)),
                            ]
                        ),
                        ft.ElevatedButton(
                            "Voir votre carte",
                            width = 2000, 
                            height = 45,
                            margin = ft.Margin.only(right = 30, left = 20, top = 0, bottom = 0),
                            on_click = add

                        ),
                    ],
                )
            )
        )


    def search(e):
        result.content = None
        num_list = ft.Column(scroll = ft.ScrollMode.ALWAYS)
        for contact in names:
            if num.value and contact["num"].startswith(num.value):
                num_list.controls.append(
                    ft.Row(
                        alignment = ft.Alignment(-1.0, 0.0),
                        controls =[
                            ft.Row(
                                controls = [
                                    ft.IconButton(
                                        icon_size  =30,
                                        icon_color = "#000000",
                                        icon = ft.CupertinoIcons.PERSON_ADD_SOLID,
                                        on_click = validate
                                    ),
                                    ft.Column(
                                        controls =[
                                            ft.Text(
                                                contact["num"],
                                                color = cl.btx,
                                                size = 15,
                                                weight = ft.FontWeight.BOLD,
                                                margin = ft.Margin.only(bottom = 0)
                                            ),
                                            ft.Text(
                                                contact["name"],
                                                color = cl.btx,
                                                size = 15,
                                                weight = ft.FontWeight.BOLD,
                                                margin = ft.Margin.only(top = 0)
                                            ),
                                        ]
                                    ),
                                ]
                            )
                        ]
                    )
                )
                result.content = num_list
        page.update()

    num = ft.TextField(
            width = 2000,
            color = "#202020",
            hint_text = "Numero",
            border = ft.Border(40),
            max_length = 12,
            input_filter = ft.NumbersOnlyInputFilter(),
            on_change = search
        )

    montant = ft.TextField(
        width = 2000,
        color = "#202020",
        hint_text = "Somme envoye (FCFA)",
        border = ft.Border(40),
        input_filter = ft.NumbersOnlyInputFilter()
    )
    credit = ft.TextField(
            width = 2000,
            color = "#202020",
            hint_text = "montant (FCFA)",
            border = ft.Border(40),
            input_filter = ft.NumbersOnlyInputFilter()
        )

    dialog = ft.AlertDialog(
        title=ft.Text("CONFIRMATION", color = "#202020",weight = ft.FontWeight.W_900),
        bgcolor = "#658f75",
        content=ft.Text(f"Transfert Reussi!", text_align = ft.TextAlign.CENTER, color = "#202020", weight = ft.FontWeight.W_600,),
        alignment=ft.Alignment.CENTER,
        on_dismiss=lambda e: print("Dialog dismissed!"),
        title_padding=ft.Padding.all(25),
    )

    dialog = ft.AlertDialog(
        title=ft.Text("CONFIRMATION", color = "#202020",weight = ft.FontWeight.W_900),
        bgcolor = "#658f75",
        content=ft.Text(f"Achat de credit Reussi!", text_align = ft.TextAlign.CENTER, color = "#202020", weight = ft.FontWeight.W_600,),
        alignment=ft.Alignment.CENTER,
        on_dismiss=lambda e: print("Dialog dismissed!"),
        title_padding=ft.Padding.all(25),
    )

    error = ft.AlertDialog(
            title=ft.Text("AVERTISSEMENT", color = "#202020",weight = ft.FontWeight.W_900),
            bgcolor = "#658f75",
            content=ft.Text(f"(solde insuffisant)", text_align = ft.TextAlign.CENTER, color = "#202020", weight = ft.FontWeight.W_600, size =18),
            alignment=ft.Alignment.CENTER,
            on_dismiss=lambda e: print("Dialog dismissed!"),
            title_padding=ft.Padding.only(top = 30, right = 30, left = 30),
        )


    page.theme = ft.Theme(
        navigation_bar_theme = ft.NavigationBarTheme(
            label_text_style = {
                ft.ControlState.SELECTED: ft.TextStyle(color="#6f8f78", weight = ft.FontWeight.BOLD),
                ft.ControlState.DEFAULT: ft.TextStyle(color="#6d9183", weight = ft.FontWeight.NORMAL),
            }
        )
    )

    home = ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Row(
                controls=[
                    ft.IconButton(
                        width = 34, 
                        height = 34,
                        margin = ft.Margin.all(2),
                        icon = ft.Icons.QUESTION_MARK,
                        icon_color = cl.bt,
                        on_click = lambda e: print("yur")
                    ),
                ]
            ),
            ft.Column(
                expand = True,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                controls =[
        #DashBoard
                    card(),
#TRANSFERT TEXT
                    ft.Text(
                        "Transferts",
                        color = cl.btx,
                        size = 18,
                        weight = ft.FontWeight.BOLD,
                    ),
#TRANSFERTS
                    ft.Container(
                        width = 2000,
                        height = 400,
                        bgcolor = cl.bg,
                        border_radius = 25,
                        content = ft.Column(
                            scroll = ft.ScrollMode.ALWAYS,
                            controls = [
                                ft.Container(
                                    alignment = ft.Alignment.TOP_CENTER,
                                    margin = ft.Margin.only(top = 20, right = 20, left = 20),
                                    content = num
                                ),
                                ft.Container(
                                    alignment = ft.Alignment(0, 0),
                                    margin = ft.Margin.only(top = 0, right = 20, left  = 20),
                                    content = montant
                                ),
                                ft.Container(
                                    alignment = ft.Alignment.TOP_CENTER,
                                    height = 500,
                                    content = result,
                                    border_radius = 10,
                                    margin = ft.Margin.only(top = 20, right = 20, left  = 20),
                                ),
                            ],
                        )
                    ),
                ],
            )
        ]
    )

    shop = ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Row(
                controls=[
                    ft.IconButton(
                        width = 34, 
                        height = 34,
                        margin = ft.Margin.all(2),
                        icon = ft.Icons.QUESTION_MARK,
                        icon_color = cl.bt,
                        on_click = lambda e: print("yur")
                    ),
                ]
            ),
            ft.Column(
                expand = True,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                controls =[
        #DashBoard
                    card(),
                    ft.Text(
                        "Credit",
                        color = cl.btx,
                        size = 18,
                        weight = ft.FontWeight.BOLD,
                    ),
                    ft.Container(
                        width = 2000,
                        height = 400,
                        bgcolor = cl.bg,
                        border_radius = 25,
                        content = ft.Column(
                            scroll = ft.ScrollMode.ALWAYS,
                            controls = [
                                ft.Container(
                                    alignment = ft.Alignment(0, 0),
                                    margin = ft.Margin.only(top = 20, right = 20, left  = 20),
                                    content = credit
                                ), 
                                ft.Text(
                                    "NB: sera envoye sur votre numero",
                                    margin = ft.Margin.only(top = 0, left = 20),
                                    color = cl.btx
                                ),
                                ft.Column(
                                    alignment = ft.Alignment(-1.0, 0.0),
                                    controls =[
                                        ft.Row(
                                            controls = [
                                                ft.IconButton(
                                                    icon_size  =25,
                                                    icon = ft.CupertinoIcons.CART,
                                                    on_click = achat
                                                ),
                                                ft.Column(
                                                    controls =[
                                                        ft.Text(
                                                            "Orange",
                                                            color = "#1F2937",
                                                            size = 25,
                                                            weight = ft.FontWeight.BOLD,
                                                            margin = ft.Margin.only(bottom = 0)
                                                        ),
                                                    ]
                                                ),
                                            ]
                                        ),
                                        ft.Row(
                                            controls = [
                                                ft.IconButton(
                                                    icon_size  =25,
                                                    icon = ft.CupertinoIcons.CART,
                                                    on_click = achat
                                                ),
                                                ft.Column(
                                                    controls =[
                                                        ft.Text(
                                                            "Yas",
                                                            color = "#1F2937",
                                                            size = 25,
                                                            weight = ft.FontWeight.BOLD,
                                                            margin = ft.Margin.only(bottom = 0)
                                                        ),
                                                    ]
                                                ),
                                            ]
                                        ),
                                        ft.Row(
                                            controls = [
                                                ft.IconButton(
                                                    icon_size  =25,
                                                    icon = ft.CupertinoIcons.CART,
                                                    on_click = achat
                                                ),
                                                ft.Column(
                                                    controls =[
                                                        ft.Text(
                                                            "Expresso",
                                                            color = "#1F2937",
                                                            size = 25,
                                                            weight = ft.FontWeight.BOLD,
                                                            margin = ft.Margin.only(bottom = 0)
                                                        ),
                                                    ]
                                                ),
                                            ]
                                        )
                                    ]
                                )
                            ],
                        )
                    ),
                ],
            )
        ]
    )

    paiement = ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Row(
                controls=[
                    ft.IconButton(
                        width = 34, 
                        height = 34,
                        margin = ft.Margin.all(2),
                        icon = ft.Icons.QUESTION_MARK,
                        icon_color = cl.bt,
                        on_click = lambda e: print("yur")
                    ),
                ]
            ),
            ft.Column(
                expand = True,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                controls =[
        #DashBoard
                    card(),

                ],
            )
        ],
    )

    def on_nav_change(e):
        idx = page.navigation_bar.selected_index
        page.clean()
        if idx == 0:
            page.add(home)  
        elif idx == 1:
            page.add(shop)
        else:
            page.add(paiement)


    page.navigation_bar = ft.NavigationBar(
        selected_index=0,
        bgcolor = cl.ap,
        indicator_color="blue_900",
        animation_duration = 0.02, 
        destinations=[
            ft.NavigationBarDestination(icon=ft.CupertinoIcons.ARROW_RIGHT_ARROW_LEFT, label="Transferts"),
            ft.NavigationBarDestination(icon=ft.CupertinoIcons.PHONE_FILL, label="Credit"),
            ft.NavigationBarDestination(icon=ft.CupertinoIcons.MONEY_DOLLAR, label="Paiements"),
        ],
        on_change=on_nav_change,
    )

    page.add(home)

ft.app(target=main)