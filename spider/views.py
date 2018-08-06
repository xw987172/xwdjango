from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from datetime import datetime
import json
def hello(request):
    data = {}
    data["time"] = str(datetime.now())
    data["info"] = {
        "total":1000,
        "members":[
            {"name":"xw","age":18},
            {"name":"wx","age":18},
            {"name":"zs","age":20}
        ]
    }
    # return JsonResponse(data)
    func_name = request.GET["callback"]
    response = HttpResponse("%s(%s)" %(func_name,str(data)))
    # response["Access-Control-Allow-Origin"] = "*"
    # response["Access-Control-Allow-Methods"] = "POST,GET,OPTIONS"
    # response["Access-Control-Max-Age"] = "1000"
    # response["Access-Control-Allow-Headers"] = "*"
    return response

def test(response):
    return render("test.html")
