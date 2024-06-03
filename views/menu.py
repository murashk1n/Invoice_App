import flet as ft
from flet_route import Params, Basket
from flet import *
from views.app_bar import AppBar

def page_menu(page: ft.Page, params: Params, basket: Basket):
    images = ft.Row(expand=1, wrap=False, scroll="always")
    
    images.controls.append(
        Container(
            ft.Image(
                src="img\customer.jpg",
                width=200,
                height=200,
                fit=ft.ImageFit.FIT_HEIGHT,
                border_radius=ft.border_radius.all(10),
                tooltip="Customers",
            ), 
            on_click=lambda _:page.go('/page_all_customers')
        )
    )
    images.controls.append(
        Container(
            ft.Image(
                src="img\companies.jpg",
                width=200,
                height=200,
                fit=ft.ImageFit.FIT_HEIGHT,
                border_radius=ft.border_radius.all(10),
                tooltip="Companies",
            ), on_click=lambda _:page.go('/page_all_companies')
        )
    )
    images.controls.append(
        Container(
            ft.Image(
                src="img\invoice.png",
                width=200,
                height=200,
                fit=ft.ImageFit.FIT_HEIGHT,
                border_radius=ft.border_radius.all(10),
                tooltip="Invoices",
            ), on_click=lambda _:page.go('/page_all_invoices')
        )
    )
    images.controls.append(
        Container(
            ft.Image(
                src="img\data.jpg",
                width=200,
                height=200,
                fit=ft.ImageFit.FIT_HEIGHT,
                border_radius=ft.border_radius.all(10),
                tooltip="Data",
            ), on_click=lambda _:page.go('/page_all_services')
        )
    )

    return ft.View(
        "/page_menu",
        
       controls=[
            AppBar().build(),
            Text("Menu",size=30,weight="bold"),
            images,
        ],
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        spacing=26
    )