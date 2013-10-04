from base import RoviApi


class SearchApi(RoviApi):
    """
    Searches titles or names in Rovi Cloud Services and returns results in
    order of popularity and similarity to the search query.

    http://prod-doc.rovicorp.com/mashery/index.php/Search-api/v2.1/search
    """

    def __init__(self, key, secret):
        super(SearchApi, self).__init__('search', 'v2.1', key, secret)

    def make_request(self, endpoint, entitiy_type, query, params=None):
        """
        Performs the API request. Most methods are a wrapper around this one.
        """
        if params is None:
            params = {}

        params['entitytype'] = entitiy_type
        params['query'] = query
        params['country'] = 'US'
        params['language'] = 'en'

        return super(SearchApi, self).make_request('%s/search' % endpoint,
                                                   params)

    def music_search(self, entitiy_type, query, **kwargs):
        """
        Search the music database

        Where ``entitiy_type`` is a comma separated list of:

        ``song``
            songs

        ``album``
            albums

        ``composition``
            compositions

        ``artist``
            people working in music
        """
        return self.make_request('music', entitiy_type, query, kwargs)

    def amg_video_search(self, entitiy_type, query, **kwargs):
        """
        Search the Movies and TV database

        Where ``entitiy_type`` is a comma separated list of:

        ``movie``
            Movies

        ``tvseries``
            TV series

        ``credit``
            people working in TV or movies
        """
        return self.make_request('amgvideo', entitiy_type, query, kwargs)

    def video_search(self, entitiy_type, query, **kwargs):
        """
        Search the TV schedule database

        Where ``entitiy_type`` is a comma separated list of:

        ``movie``
            Movie

        ``tvseries``
            TV series

        ``episode``
            Episode titles

        ``onetimeonly``
            TV programs

        ``credit``
            People working in TV or movies
        """
        return self.make_request('video', entitiy_type, query, kwargs)
