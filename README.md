# Python_API_Test
Tests:

1. Successfully make api requests to omdbapi from within tests.

2.  Create a test that performs a search by imdbId.
a. Verify the response header has the expected content-type.
b. Verify the response time is less than 30 milliseconds. 

3. Create a test that performs a search on a search word.

a. Verify all titles are a relevant match.
b. Verify all keys included for all records in the response.
c. Verify year matches correct format.
d. Add a test that verifies none of the poster links on page 1 are broken.
e. 
e. Add a test that verifies there are no duplicate records.

4. Add an assertion to test response with no api key to ensure the response at runtime matches what is currently displayed with the api key missing.

5. Add an assertion to test response with invalid api key to ensure the response at runtime matches what is currently displayed.

NOTES from testing:
1. This is an open web service that does not allow adding or deleting records. 
   For this reason, I have not added tests for POST, UPDATE/ PUT or DELETE.
 
 
