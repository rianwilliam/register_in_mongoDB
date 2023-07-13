import flet as ft
from typing import Type

def create_text_field(label: str) -> Type[ft.TextField]:
    return ft.TextField(label=label)

def create_button(btn_text: str) -> Type[ft.ElevatedButton]:
    return ft.ElevatedButton(text=btn_text)
