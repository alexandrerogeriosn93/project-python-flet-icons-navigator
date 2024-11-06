import flet as ft


def main(page: ft.Page):
    def show_search_page(event=None):
        page.clean()

        search_bar = ft.TextField(prefix_icon=ft.icons.SEARCH, hint_text="Pesquisar")
        layout = ft.Column(expand=True, controls=[search_bar])

        page.add(layout)

    show_search_page()


ft.app(target=main, view=ft.AppView.FLET_APP)
