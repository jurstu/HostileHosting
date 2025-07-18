from nicegui import ui, app

USERS = {
    'admin': 'secret123',
    'guest': 'password'
}

@ui.page('/login')
def login():
    with ui.card().classes('absolute-center'):
        ui.label('Login with NiceGUI')
        username_input = ui.input('Username')
        password_input = ui.input('Password', password=True)
        message = ui.label()

        def try_login():
            if USERS.get(username_input.value) == password_input.value:
                app.storage.user['username'] = username_input.value
                ui.navigate('/')
            else:
                message.text = 'Invalid username or password'

        ui.button('Login', on_click=try_login)

@ui.page('/')
def home():
    if 'username' not in app.storage.user:
        return ui.navigate('/login')

    user = app.storage.user['username']
    ui.label(f'Welcome, {user}!').classes('text-xl')
    ui.button('Logout', on_click=lambda: ui.navigate('/logout'))

@ui.page('/logout')
def logout():
    app.storage.user.clear()
    ui.label('You have been logged out.')
    ui.timer(1.5, lambda: ui.navigate('/login'))

# Required for session support
ui.run(storage_secret='your_super_secret_key_here')
