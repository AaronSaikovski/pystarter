from pystarter.version import APP_NAME, VERSION, __version__


def test_version():
    assert VERSION == __version__


def test_app_name():
    assert APP_NAME == "pystarter"
