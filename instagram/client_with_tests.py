import pytest
from unittest.mock import patch, Mock, MagicMock
from hamcrest import assert_that, equal_to, is_, has_items


class Media:

    # def __init__(self, id=None, **kwargs):
    #     self.id = id

    id = None


class InstagramAPI:

    def __init__(self, access_token, client_secret):
        pass

    def user_recent_media(self, user_id, count=10):
        return [], None

    def media_comments(media_id):
        return []


def fun():
    api = InstagramAPI(access_token='YOUR_ACCESS_TOKEN', client_secret='YOUR_CLIENT_SECRET')
    recent_media, next_ = api.user_recent_media(user_id='concept_club')
    return recent_media


def fun2():
    api = InstagramAPI(access_token='YOUR_ACCESS_TOKEN', client_secret='YOUR_CLIENT_SECRET')
    recent_media, next_ = api.user_recent_media(user_id='concept_club')
    media_id = recent_media[0].id # XXX
    return api.media_comments(media_id)


@pytest.mark.xfail
@patch('instagram.client_with_tests.InstagramAPI', autospec=True)
def test_how_to_mock_intagram_api_mock(mock_instagram):
    api = InstagramAPI(access_token='YOUR_ACCESS_TOKEN', client_secret='YOUR_CLIENT_SECRET')
    assert_that(api, is_(InstagramAPI))


@patch('instagram.client_with_tests.InstagramAPI', autospec=True)
def test_how_to_mock_user_recent_media(mock_instagram):

    mock_instagram.return_value = Mock()
    mock_instagram_obj = mock_instagram.return_value

    mock_instagram_obj.user_recent_media.return_value = \
        ([MagicMock(id=id_) for id_ in range(0,10)], None)

    recent_media = fun()
    assert_that(len(recent_media), equal_to(10))


@patch('instagram.client_with_tests.InstagramAPI', autospec=True)
def test_how_to_mock_media_comments(mock_instagram):
    mock_instagram.return_value = Mock()
    mock_instagram_obj = mock_instagram.return_value

    mock_instagram_obj.user_recent_media.return_value = ([MagicMock(id=123)], None)

    # def side_effect(media_id):
    #     if media_id == 123:
    #         pass

    mock_instagram_obj.media_comments.return_value = ['foo', 'bar', 'baz']
    # mock_instagram_obj.media_comments.side_effect = side_effect
        
    comments = fun2()

    mock_instagram_obj.media_comments.assert_called_once_with(123)

    assert_that(comments, has_items(is_('foo'), is_('bar'), is_('baz')))
