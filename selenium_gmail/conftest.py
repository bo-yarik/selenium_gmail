import pytest

from fixture.application import Application


@pytest.fixture(scope='session', params=['Chrome'])
def app(request):
    fixture = Application(request.param)
    fixture.session.login(login='Testuserforwisebits1@gmail.com', password='WiseBits1')

    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
