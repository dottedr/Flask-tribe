"""
Testing book requests endpoints
run: python -m pytest tests/funtional/test_book_requests.py
"""
import pytest

def test_get_all_requests(create_app_setup):
    """
    GIVEN flask server is running
    WHEN sending a GET request to /requests
    THEN server response status is 200
    """
    all_requests = create_app_setup.get('/requests')
    assert all_requests.status_code == 200

@pytest.mark.xfail(reason='id does not exist')
def test_get_new_record(create_app_setup):
    "Test getting the new record"
    _id = 'somethingthatdeoesntexist'
    new_record = create_app_setup.get(f'/requests/{_id}')
    assert new_record.status_code == 200
