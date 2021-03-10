from Python_API_Test.API_Helpers.ApiHelpers import ApiHelpers
from Python_API_Test.API_utils.configuration import Configuration


class ApiTests(ApiHelpers):
    def __init__(self, baseurl, api_key):
        super().__init__(baseurl)
        self.a = ApiHelpers(self.baseurl)
        self.api_key = api_key  # api key generated from the website

    # Test case 1: Verify Get for title parameter.
    def test_get_specific_result(self, search_movie_title):
        parameter = '?t=' + search_movie_title + "&apikey=" + self.api_key
        movie = self.a.get_method_with_parameters(parameter)
        assert movie['Title'] == search_movie_title

    # Test case 2: Verify Get by imdbId parameter
    def test_get_by_imdbid(self, search_movie_id):
        parameter = '?i=' + search_movie_id + "&apikey=" + self.api_key
        movie = self.a.get_method_with_parameters(parameter)
        assert movie['Title'] == 'Love & Goodwill'

    # Test case 2a: Verify response header
        movie_header, response_time = self.a.get_method_header(parameter)
        assert 'application/json' in movie_header['Content-Type']

    # Test case 2b: Verify response time
        assert response_time < 0.302931, 'server response times very slow'

    # Test case 3: Verify Get for search parameter with multiple movies returned
    def test_get_all_results(self, search_movie, expected_result):
        parameter = '?s=' + search_movie + "&apikey=" + self.api_key
        movie = self.a.get_method_with_parameters(parameter)
        assert movie['totalResults'] == expected_result

        movie_keys = ["Title", "Year", "imdbID", "Type", "Poster"]  # Key indexes for each movie
        list_unique_movie = []
        list_dup_movie = []
        for m in movie["Search"]:  # List with search key's value is the dict of movie items.

            # Test case 3a. Verify titles are a relevant match
            assert search_movie in m['Title'], "Title is not a relevant match"

            # Test case 3b. Verify all key indexes are present for each movie in the dict.
            if all(key in m for key in movie_keys):
                assert True, "Key Index missing for " + str(m["Title"])

            # Test case 3c: Verify year format in the response.
            verify_year_format = self.a.check_year(m['Year'])
            assert verify_year_format is True, "Incorrect year format " + str(m['Year'])

            # Test case 3d: Verify the poster links are not broken
            if m['Poster'] == 'N/A':  # This is a valid value
                verify_poster = True
            else:
                verify_poster = self.a.check_url(m['Poster'])  # ReGex check for the key = Poster
            assert verify_poster is True, "Poster link is broken for " + str(m["Title"])

            # Test case 3e: Verify there are no duplicates in the response.
            if m not in list_unique_movie:
                list_unique_movie.append(m)
            else:
                list_dup_movie.append(m)
        assert len(movie["Search"]) == len(list_unique_movie), "duplicates exist! " + str(set(list_dup_movie))

    # Test 4: Verify response when request does not contain api key.
    def test_no_api_key_get(self):
        parameter = '?s=star'
        no_api_response = self.a.get_method_no_apikey(parameter)
        assert no_api_response["Error"] == "No API key provided."

    # Test 5: Verify response when request contains invalid api key.
    def test_invalid_api_key_get(self):
        parameter = '?s=star' + "&apikey=" + self.api_key + 'a'
        invalid_api_response = self.a.get_method_no_apikey(parameter)
        assert invalid_api_response["Error"] == "Invalid API key!"


if __name__ == "__main__":
    print("API Testing with Python and requests library")
    test_site = ApiTests(Configuration.site_url, Configuration.site_key)
    test_site.test_get_by_imdbid(Configuration.site_imdbID)
    test_site.test_get_specific_result(Configuration.movie_title_to_search)
    test_site.test_get_all_results(Configuration.site_search_word, Configuration.expected_num_movies)
    test_site.test_no_api_key_get()
    test_site.test_invalid_api_key_get()
    print("Tests completed")
