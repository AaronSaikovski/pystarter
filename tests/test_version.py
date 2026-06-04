from pystarter.version import APP_NAME, VERSION, __version__


def test_version():
    assert VERSION == "1.0.0"
    assert __version__ == "1.0.0"


def test_app_name():
    assert APP_NAME == "pystarter"
