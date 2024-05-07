"""Test security headers"""

def test_csp(create_app_setup):
    """Response header should cold contain this Content-Security-Policyheader"""
    response = create_app_setup.get('/requests')
    assert response.headers.get('Content-Security-Policy') == "sandbox; default-src 'self'; frame-ancestors 'none'"

def test_hsts(create_app_setup):
    """Response header should cold contain this Strict-Transport-Security header"""
    response = create_app_setup.get('/requests')
    assert response.headers.get('Strict-Transport-Security') == 'max-age=31536000; includeSubDomains'

def test_nosniff(create_app_setup):
    """Response header should cold contain this X-Content-Type-Options header"""
    response = create_app_setup.get('/requests')
    assert response.headers.get('X-Content-Type-Options') == 'nosniff'

def test_x_frame(create_app_setup):
    """Response header should cold contain this X-Frame-Options header"""
    response = create_app_setup.get('/requests')
    assert response.headers.get('X-Frame-Options') == 'DENY'