import time
import flet as ft
from src.checks.email_verification import verify_email
from src.repostitory.register_collection import get_collection
from src.widgets.widgets import create_button, create_text_field

collection = get_collection()

def main(page = ft.Page, ) -> None:
    page.title = "Cadastro em flet"

    def success_msg() -> None:
        msg = ft.Text("Cadastro realizado com sucesso!",
                      color =  ft.colors.GREEN_400)
        grid.controls.append(msg)
        grid.update()
        time.sleep(4)
        grid.controls.pop()
        grid.update()

    def clean_fields() -> None:
        first_name.value = ""
        last_name.value = ""
        email.value = ""
        page.update()

    def email_validation(e) -> None:
        valid_email = verify_email(email.value)
        if valid_email:
            subscribe_btn.disabled = False
            subscribe_btn.update()
        else:
            subscribe_btn.disabled = True
            subscribe_btn.update()
            valid_email = []

    def subscribe(e) -> None:
        collection.insert_one(
            {
                "Nome": first_name.value,
                "Sobrenome": last_name.value,
                "Email": email.value
            }
        )
        subscribe_btn.disabled = True
        clean_fields()
        success_msg()

    first_name = create_text_field(label="Insira seu primeiro nome")
    last_name = create_text_field(label="Insira seu último nome")

    email = create_text_field(label="Insira seu email")
    email.on_change = email_validation

    subscribe_btn = create_button(btn_text="Cadastrar")
    subscribe_btn.disabled = True
    subscribe_btn.on_click = subscribe

    grid = ft.Column([
        first_name, last_name, email,subscribe_btn
    ])

    page.add(grid)
