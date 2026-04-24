import flet as ft

def main(page: ft.Page):
    page.title = "Pizza Builder"
    page.bgcolor = "#0f172a"  
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    
    base = ft.Image(
        src="pizza_base.png",
        width=300,
        height=300
    )

    pepperoni = ft.Image(
        src="pepperoni.py.png",
        width=300,
        height=300,
        visible=False
    )

    pineapple = ft.Image(
        src="pineapple.py.png",
        width=300,
        height=300,
        visible=False
    )

    bacon = ft.Image(
        src="bacon.py.png",
        width=300,
        height=300,
        visible=False
    )

  
    def toggle_pepperoni(e):
        pepperoni.visible = e.control.value
        page.update()

    def toggle_pineapple(e):
        pineapple.visible = e.control.value
        page.update()

    def toggle_bacon(e):
        bacon.visible = e.control.value
        page.update()

    
    pizza = ft.Stack(
        [
            base,
            pepperoni,
            pineapple,
            bacon
        ],
        width=300,
        height=300
    )

    
    controls = ft.Column(
        [
            ft.Switch(label="Pepperoni", on_change=toggle_pepperoni),
            ft.Switch(label="Pineapple", on_change=toggle_pineapple),
            ft.Switch(label="Bacon", on_change=toggle_bacon),
        ],
        spacing=15
    )

    
    page.add(
        ft.Column(
            [
                pizza,
                controls
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=30
        )
    )


ft.app(target=main)