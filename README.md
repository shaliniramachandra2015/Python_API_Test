# API Testing with Python and requests library

OMDBApi is an open web service that does not allow addition or deletion of records. 
For this reason, test cases for POST, UPDATE/ PUT or DELETE are not part of the project.

The test cases are a sample selection to showcase API Testing with Python.
While the priority of the use cases is taken into account, but coverage is not achieved at this time.

Tests:

1. Verify Api requests to omdbapi from within tests.

2. Test to verify search by imdbId.

    a. Verify the response header has the expected content-type.

    b. Verify the response time is less than 30 milliseconds. 

3. Test that performs a search on a search word.

    a. Verify all titles are a relevant match.

    b. Verify all keys included for all records in the response.

    c. Verify year matches correct format.

    d. Test that none of the poster links are broken.

    e. Test there are no duplicate records.

4. Test response with no api key.

5. Test response message with invalid api key.
