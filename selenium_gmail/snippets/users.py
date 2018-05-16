from fixture.application import Application


def create_new_user(params, browser):
    user = Application(browser)
    user.session.login(login=params['login'], password=params['password'])
    user.wd.get('https://mail.google.com')
    return user
