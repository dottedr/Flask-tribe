"""
Testing book requests endpoints
run: python -m pytest tests/funtional/test_book_requests.py
"""


def test_get_all_requests(create_app_setup):
    """
    GIVEN flask server is running
    WHEN sending a GET request to /requests
    THEN server response status is 200
    """
    all_requests = create_app_setup.get('/requests')
    assert all_requests.status_code == 200