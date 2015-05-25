from django.http import JsonResponse
import json
import urllib2

"""
Peloton Back End Test Task

Web Service Background:
    - Consumes 2 separate streams of increasing integers
    - Can be queried to return the updated current element of the merged list
    - Merged lists maintain increasing order

App Requirements:
    - Ability to query server with
        http://localhost:8000/quiz/merge?stream1=<stream_name_1>&stream2=<stream_name_2>
    - Communicate with Peloton server endpoint for consuming streams of data
        https://api.pelotoncycle.com/quiz/next/<stream_name>

Notes:
    - Standard django 1.8 deployment
    - No additional site-packages to install
    - 8000 was chosen for the default port for a django project
    - Repo located at https://github.com/Edinunzio/peloton

"""


def merge(request):
    """
    View that returns results from merged streams
    :param request:
    :return:
        {
            "last": <previous merged stream value>
            "current": <current merged stream value>
        }
    """

    def get_current_stream_item(stream_name):
        """
        Retrieves stream info
        :param stream_name:
        :return:
            {
                "last": <last stream value>
                "current": <current stream value>
                "stream": <stream name>
            }
        """
        _req = urllib2.Request('https://api.pelotoncycle.com/quiz/next/'+stream_name)
        _req.add_header('Content-Type', 'application/json')
        con = urllib2.urlopen(_req)
        response = con.read()
        con.close()
        content = json.loads(response)
        return content

    def merge_streams(stream1, stream2):
        """
        Sorts "last" and "current" stream values and returns updated
        "last" and "current" values of the merged stream.

        http://localhost:8000/quiz/merge?stream1=<stream_name_1>&stream2=<stream_name_2>
        :param stream1:
        :param stream2:
        :return:
            {
                "last": 2,
                "current": 4,
            }
        """
        container = []
        content = {}
        s_1 = get_current_stream_item(stream1)
        s_2 = get_current_stream_item(stream2)
        container.append(s_1['last'])
        container.append(s_1['current'])
        container.append(s_2['last'])
        container.append(s_2['current'])
        container.sort(reverse=True)
        content['last'] = container[1]
        content['current'] = container[0]
        return content

    req = request.GET
    stream_1 = req['stream1']
    stream_2 = req['stream2']
    result = merge_streams(stream_1, stream_2)
    return JsonResponse(result)
