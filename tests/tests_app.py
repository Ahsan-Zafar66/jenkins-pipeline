from app import app

def test_index_ok():
    client = app.test_client()
    r = client.get('/')
    assert r.status_code == 200
    assert r.get_json()['message'] == "Hello from CI/CD sample app"
