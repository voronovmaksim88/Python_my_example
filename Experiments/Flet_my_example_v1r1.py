import flet as ft
import time


def main(page: ft.Page):
    # page.add(
    #     ft.Row(
    #         [
    #             ft.Text(value="Всем привет от нового модного фреймвоорка Flet",
    #                     color="green"),
    #             ft.IconButton(ft.icons.HOME)
    #         ],
    #         alignment=ft.MainAxisAlignment.CENTER
    #     ),
    #     ft.Row(
    #         [
    #             ft.Text(value="Всем привет от нового модного фреймвоорка Flet",
    #                     color="green"),
    #             ft.IconButton(ft.icons.HOME)
    #         ],
    #         alignment=ft.MainAxisAlignment.CENTER
    #     )
    # )

    t1 = ft.Text(value="Всем привет от нового модного фреймвока Flet", color="green")
    t2 = ft.Text(value="Он работает как на веб так и на десктоп", color="red")
    page.controls.append(t1)
    page.controls.append(t2)

    page.add(
        ft.Row(controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C")
        ])
    )

    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your name"),
            ft.ElevatedButton(text="Say my name!")
        ])
    )

    for i in range(5):
        page.controls.append(ft.Text(f"Line {i}"))
        page.update()
        time.sleep(0.5)

    def button_clicked(e):
        page.add(ft.Text("Clicked!"))

    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))

    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

    first_name = ft.TextField(label="First name", autofocus=True)
    last_name = ft.TextField(label="Last name")
    greetings = ft.Column()

    def btn_click(e):
        greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}!"))
        first_name.value = ""
        last_name.value = ""
        page.update()
        first_name.focus()

    page.add(
        first_name,
        last_name,
        ft.ElevatedButton("Say hello!", on_click=btn_click),
        greetings,
    )

    page.update()


ft.app(target=main, view=ft.WEB_BROWSER)
