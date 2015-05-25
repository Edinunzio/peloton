from django.http import JsonResponse
import json
import urllib2


def merge(request):

    def get_current_stream_item(stream_name):
        _req = urllib2.Request('https://api.pelotoncycle.com/quiz/next/'+stream_name)
        _req.add_header('Content-Type', 'application/json')
        con = urllib2.urlopen(_req)
        response = con.read()
        con.close()
        content = json.loads(response)
        return content

    def merge_streams(stream1, stream2):
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
