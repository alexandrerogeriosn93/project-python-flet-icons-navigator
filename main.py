import flet as ft

is_dark_mode = False


def main(page: ft.Page):
    def toggle_dark_mode(event):
        global is_dark_mode

        is_dark_mode = not is_dark_mode
        page.theme_mode = ft.ThemeMode.DARK if is_dark_mode else ft.ThemeMode.LIGHT

        page.update()

    def show_search_page(event=None):
        page.clean()

        search_bar = ft.TextField(prefix_icon=ft.icons.SEARCH, hint_text="Pesquisar")
        layout = ft.Column(
            expand=True,
            controls=[
                search_bar,
                ft.ElevatedButton("Alterar tema visual", on_click=toggle_dark_mode),
            ],
        )

        page.add(layout)

    page.theme_mode = ft.ThemeMode.LIGHT
    show_search_page()


ft.app(target=main, view=ft.AppView.FLET_APP)
