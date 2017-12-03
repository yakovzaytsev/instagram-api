# import pytest
from hamcrest import assert_that, equal_to_ignoring_case  # XXX
from instagram import client


def test_get_authorize_url():
    CONFIG = {
        'client_id': '<client_id>',
        'client_secret': '<client_secret>',
        'redirect_uri': 'http://localhost:8515/oauth_callback'
    }        
    unauthenticated_api = client.InstagramAPI(**CONFIG)
    url = unauthenticated_api.get_authorize_url(
        scope=['basic', 'public_content', 'follower_list',
               'relationships', 'likes'])
        
    assert_that(url, equal_to_ignoring_case(f"https://api.instagram.com/oauth/authorize/?client_id={CONFIG['client_id']}&redirect_uri={CONFIG['redirect_uri']}&response_type=code&scope=basic+public_content+follower_list+relationships+likes"))

