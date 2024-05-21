import flet as ft
from flet import *
from flet_route import Routing, path
from views.home import Home
from views.page_reg import page_reg
from views.page_auth import page_auth
from views.page_all_customers import page_all_customers
from views.page_all_services import page_all_services
from views.page_all_invoices import page_all_invoices
from views.page_invoice_details import page_invoice_details
from views.page_all_companies import page_all_companies 
from views.page_invoice_line import page_invoice_line
from views.cabinet import page_cabinet

def main(page: ft.Page):

    app_routes = [
        
        path(url="/", clear= True,view=Home),
        path(url="/page_reg",clear= True, view=page_reg),
        path(url="/page_auth",clear= True, view=page_auth),
        path(url="/page_all_customers",clear= True, view=page_all_customers),
        path(url="/page_all_services",clear= True, view=page_all_services),
        path(url="/page_all_invoices",clear= True, view=page_all_invoices),
        path(url="/page_cabinet",clear= True, view=page_cabinet),
        path(url="/page_invoice_details",clear= True, view=page_invoice_details),
        path(url="/page_all_companies",clear= True, view=page_all_companies),
        path(url="/page_invoice_line",clear= True, view=page_invoice_line),
    ]
    
    Routing(page=page, app_routes=app_routes)
    
    page.go(page.route)
    
if __name__ == '__main__':
    ft.app(target=main)
