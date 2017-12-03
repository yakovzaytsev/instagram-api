class Media:

    # def __init__(self, id=None, **kwargs):
    #     self.id = id

    id = None


class InstagramAPI:

    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def user_recent_media(self, user_id, count=10):
        return [], None

    def media_comments(media_id):
        return []

    def get_authorize_url(self, scope):
        assert len(scope) >= 1
        url = f'https://api.instagram.com/oauth/authorize/?client_id={self.client_id}&redirect_uri={self.redirect_uri}&response_type=code&scope={scope[0]}'
        for s in scope[1:]:
            url += f'+{s}'
        return url
