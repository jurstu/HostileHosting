from nicegui import ui
from fastapi import Request  # ✅ Import FastAPI's Request

SECRET_PASSWORD = 'opensesame'

def show_protected_content(r):
    with ui.card():
        ui.label('🎉 Welcome! You entered the correct password.')
        #ui.button('Logout', on_click=lambda: logout_user())

def show_password_form(r):
    password_input = ui.input('Enter Password', password=True)

    def try_login():
        nonlocal r
        if password_input.value == SECRET_PASSWORD:
            r.cookies.set('authenticated', 'yes')
            ui.open('/', new_tab=False)
        else:
            ui.notify('Wrong password!', type='negative')

    ui.button('Submit', on_click=try_login)

#def logout_user():
#    request.cookies.clear('authenticated')
#    request.open('/', new_tab=False)

@ui.page('/')
def main_page(request: Request):  # ✅ Annotate properly with FastAPI Request
    if request.cookies.get('authenticated') == 'yes':
        show_protected_content(request)
    else:
        show_password_form(request)

ui.run()
