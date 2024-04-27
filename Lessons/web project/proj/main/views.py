from django.shortcuts import render
import datetime

# Create your views here.
def test(request):
    # print("test view")
    t = datetime.datetime.now()
    return render(request, "test.html", {"current_time":t})