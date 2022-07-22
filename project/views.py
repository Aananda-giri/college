from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == "GET":
        # get the nick name from the client side.
        search_term = request.GET.get("search_query", None)
        if search_term != None:
            # save to database
            pass
    return render(request, 'project/index.html')