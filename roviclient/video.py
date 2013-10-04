from base import RoviDataApi


class VideoApi(RoviDataApi):
    """
    Make requests to the Rovi Video API v1
    """

    def make_request(self, resource, params=None):
        """
        Performs the API request. Most methods are a wrapper around this one.
        """
        return super(VideoApi, self).make_request('video/%s' % resource, params)

    def _cosmoid_request(self, resource, cosmoid, **kwargs):
        """
        Maps to the Generic API method for requests who's only parameter is ``cosmoid``
        """

        params = {
            'cosmoid': cosmoid,
        }
        params.update(kwargs)

        return self.make_request(resource, params)

    def video_info(self, cosmoid, **kwargs):
        """
        Returns information about a movie, TV series, or TV program.

        Maps to the `info <http://prod-doc.rovicorp.com/mashery/index.php/V1.MetaData.VideoService.Video:Info>`_ API method.
        """

        return self._cosmoid_request('info', cosmoid, **kwargs)

    def season_info(self, cosmoid, season, **kwargs):
        """
        Returns information about a season of a TV series

        Maps to the `season info <http://prod-doc.rovicorp.com/mashery/index.php/V1.MetaData.VideoService.Video:Season>`_ API method.
        """

        resource = 'season/%d/info' % season
        return self._cosmoid_request(resource, cosmoid, **kwargs)

        params = {
            'cosmoid': cosmoid,
        }
        params.update(kwargs)

        return self.make_request(resource, params)

    def episode_info(self, cosmoid, season, episode, **kwargs):
        """
        Returns information about an episode in a television series

        Maps to the `episode info <http://prod-doc.rovicorp.com/mashery/index.php/V1.MetaData.VideoService.Video:SeasonEpisode>`_ API method.
        """

        resource = 'season/%d/episode/%d/info' % (season, episode)

        return self._cosmoid_request(resource, cosmoid, **kwargs)

    def awards(self, cosmoid, **kwargs):
        """
        Returns awards a program has been nominated for or won.

        Maps to the `awards <http://prod-doc.rovicorp.com/mashery/index.php/V1.MetaData.VideoService.Video:Awards>`_ API method.
        """

        return self._cosmoid_request('awards', cosmoid, **kwargs)

    def cast(self, cosmoid, **kwargs):
        """
        Returns information about cast members with links to images.

        Maps to the `cast <http://prod-doc.rovicorp.com/mashery/index.php/V1.MetaData.VideoService.Video:Cast>`_ API method.
        """

        return self._cosmoid_request('cast', cosmoid, **kwargs)

    def clip(self, cosmoid, **kwargs):
        """
        Returns data you can use to construct links to trailers and video clips.

        Maps to the `clip <http://prod-doc.rovicorp.com/mashery/index.php/V1.MetaData.VideoService.Video:VideoClips>`_ API method.
        """

        return self._cosmoid_request('clip', cosmoid, **kwargs)

    def crew(self, cosmoid, **kwargs):
        """
        Returns information about crew members with links to images.

        Maps to the `crew <http://prod-doc.rovicorp.com/mashery/index.php/V1.MetaData.VideoService.Video:Crew>`_ API method.
        """

        return self._cosmoid_request('crew', cosmoid, **kwargs)

    def event(self, cosmoid, **kwargs):
        """
        Returns information about a televised sporting event.

        Maps to the `event <http://prod-doc.rovicorp.com/mashery/index.php/V1.MetaData.VideoService.Video:Event>`_ API method.
        """

        return self._cosmoid_request('event', cosmoid, **kwargs)

    def images(self, cosmoid, **kwargs):
        """
        Returns movie and television program images.

        Maps to the `images <http://prod-doc.rovicorp.com/mashery/index.php/V1.MetaData.VideoService.Video:Images>`_ API method. See also:

        - `Image <http://prod-doc.rovicorp.com/mashery/index.php/V1.Metadata.Common:Image>`_
        - `ImageType <http://prod-doc.rovicorp.com/mashery/index.php/V9.Common:ImageType>`_
        - `ImageOrder <http://prod-doc.rovicorp.com/mashery/index.php/V9.Common:ImageOrder>`_
        - `ImageFormats <http://prod-doc.rovicorp.com/mashery/index.php/ImageFormats>`_
        """

        return self._cosmoid_request('images', cosmoid, **kwargs)

    def keywords(self, cosmoid, **kwargs):
        """
        Returns keywords that apply to a movie, TV series, or TV program.

        Maps to the `keywords <http://prod-doc.rovicorp.com/mashery/index.php/V1.MetaData.VideoService.Video:Keywords>`_ API method.
        """

        return self._cosmoid_request('keywords', cosmoid, **kwargs)

    def moods(self, cosmoid, **kwargs):
        """
        Returns terms that describe expressive characteristics of a movie or
        television program, along with weightings that reflect the relative
        strength of each term.

        Maps to the `moods <http://prod-doc.rovicorp.com/mashery/index.php/V1.MetaData.VideoService.Video:Moods>`_ API method.
        """

        return self._cosmoid_request('moods', cosmoid, **kwargs)

    def parental_ratings(self, cosmoid, **kwargs):
        """
        Returns the parental ratings for a movie or television program.

        Maps to the `parental ratings <http://prod-doc.rovicorp.com/mashery/index.php/V1.MetaData.VideoService.Video:ParentalRatings>`_ API method.
        """

        return self._cosmoid_request('parentalratings', cosmoid, **kwargs)

    def related(self, cosmoid, **kwargs):
        """
        Returns movies, series, seasons, and programs that have a relationship
        with a movie, series, season, or program specified in the request.

        Maps to the `related <http://prod-doc.rovicorp.com/mashery/index.php/V1.MetaData.VideoService.Video:Related>`_ API method.
        """

        return self._cosmoid_request('related', cosmoid, **kwargs)

    def review(self, cosmoid, **kwargs):
        """
        Returns a professional review of a movie or program.

        Maps to the `review <http://prod-doc.rovicorp.com/mashery/index.php/V1.MetaData.VideoService.Video:Review>`_ API method.
        """

        return self._cosmoid_request('review', cosmoid, **kwargs)

    def schedule(self, cosmoid, **kwargs):
        """
        Returns a list of recent and upcoming television broadcasts of a movie or program.

        Maps to the `schedule <http://prod-doc.rovicorp.com/mashery/index.php/V1.MetaData.VideoService.Video:Schedule>`_ API method.
        """

        return self._cosmoid_request('schedule', cosmoid, **kwargs)

    def seasons(self, cosmoid, **kwargs):
        """
        Returns links to information about seasons and episodes in a television
        series. An optional argument returns season information in the response
        instead of a link to the information.

        Maps to the `seasons <http://prod-doc.rovicorp.com/mashery/index.php/V1.MetaData.VideoService.Video:Seasons>`_ API method.
        """

        return self._cosmoid_request('seasons', cosmoid, **kwargs)

    def synopsis(self, cosmoid, **kwargs):
        """
        Returns the best available synopsis associated with a movie or program.

        Maps to the `synopsis <http://prod-doc.rovicorp.com/mashery/index.php/V1.MetaData.VideoService.Video:Synopsis>`_ API method.
        """

        return self._cosmoid_request('synopsis', cosmoid, **kwargs)

    def themes(self, cosmoid, **kwargs):
        """
        Returns a list of topics and circumstances that motivate or fit with a movie or program.

        Maps to the `themes <http://prod-doc.rovicorp.com/mashery/index.php/V1.MetaData.VideoService.Video:Themes>`_ API method.
        """

        return self._cosmoid_request('themes', cosmoid, **kwargs)

    def tones(self, cosmoid, **kwargs):
        """
        Returns feelings and attitudes that motivate or fit with a movie or
        program, along with weightings that reflect the relative strength of
        each term.

        Maps to the `tones <http://prod-doc.rovicorp.com/mashery/index.php/V1.MetaData.VideoService.Video:Tones>`_ API method.
        """

        return self._cosmoid_request('tones', cosmoid, **kwargs)
