# Peloton Back End Test Task

## Web Service Background:
* Consumes 2 separate streams of increasing integers
* Can be queried to return the updated current element of the merged list
* Merged lists maintain increasing order

## App Requirements:
* Ability to query server with `http://localhost:8000/quiz/merge?stream1=<stream_name_1>&stream2=<stream_name_2>`
* Communicate with Peloton server endpoint for consuming streams of data with `https://api.pelotoncycle.com/quiz/next/<stream_name>`

### Notes:
* Standard django 1.8 deployment
* No additional site-packages to install
* 8000 was chosen for the default port for a django project
