from instagram.client import InstagramAPI


def fun():
    api = InstagramAPI(access_token='YOUR_ACCESS_TOKEN', client_secret='YOUR_CLIENT_SECRET')
    # import pdb; pdb.set_trace()
    recent_media, next_ = api.user_recent_media(user_id='concept_club')
    return recent_media


def fun2():
    api = InstagramAPI(access_token='YOUR_ACCESS_TOKEN', client_secret='YOUR_CLIENT_SECRET')
    recent_media, next_ = api.user_recent_media(user_id='concept_club')
    media_id = recent_media[0].id # XXX
    return api.media_comments(media_id)


