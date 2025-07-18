from nicegui import ui, app

# 👇 In-memory user database (use hashed passwords in real life!)
USERS = {
    'alice': 'pass123',
    'bob': 'hunter2',
}

def check_login():
    return app.storage.user.get('authenticated', False)

def require_login():
    if not app.storage.user.get('authenticated', False):
        ui.navigate.to('/login')
        return False
    return True

@ui.page('/login')
def login_page():
    with ui.card().classes('absolute-center'):
        ui.label('Login')
        username = ui.input('Username')
        password = ui.input('Password', password=True)

        def try_login():
            if USERS.get(username.value) == password.value:
                app.storage.user['authenticated'] = True
                app.storage.user['username'] = username.value
                ui.navigate.to('/')
            else:
                ui.notify('Invalid credentials', type='negative')

        ui.button('Log In', on_click=try_login)

@ui.page('/')
def main_page():
    if not require_login():
        return  # stop rendering further if not logged in
    with ui.row():
        ui.label(f"Hello, {app.storage.user['username']}!")
        ui.button('Logout', on_click=logout)

def logout():
    app.storage.user.clear()
    ui.navigate.to('/login')

ui.run(storage_secret='your_ultra_secret_key')

