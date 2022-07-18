from dash.testing.application_runners import import_app

def test_bbaaa001(dash_duo):
    app = import_app("dash_test.app")
    dash_duo.start_server(app)

    assert dash_duo.find_element("h1").text == "Pink Morsel - Soul Foods"
    assert dash_duo.wait_for_element("#header", timeout=10)
    assert dash_duo.wait_for_element("#indicator-graphic", timeout=10)
    assert dash_duo.wait_for_element("#category", timeout=10)

    assert dash_duo.get_logs() == [], "Browser console should contain no error"

    return None
