# noble-prizewinners
A Repo for a web application that can search a database of Noble prizewinners

# Requirements:
1. docker-compose needs to be installed and available to run.
2. pytest needs to needs to be installed and available to run (for testing only).

# Building and running the application:
To build and run the application (in the background) use:

  ./run.sh &

# Testing the application:
To test a running application use:
  ./test.sh

# Acessing the API:
Visit http://localhost:8000/search/name?q=Albert to search by name.
Visit http://localhost:8000/search/category?q=physics to search by category.
Visit http://localhost:8000/search/description?q=relativity to search by description.


# Supplemental Notes:
Unfortunately, in trying to add some more security to the application, I broke it and haven't been able to troubleshoot and fix it within the time limit.
