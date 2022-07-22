from django.shortcuts import render
from .models import Queries

# Create your views here.

def index(request):
    if request.method == "GET":
        # get the nick name from the client side.
        search_term = request.GET.get("search_query", None)
        if search_term != None:
            print(f'\n ------{search_term}------\n')
            try:
                for i in Queries.objects.raw('INSERT INTO project_queries(\'query\') values(\'%s\');' % search_term):
                    print(i)
            except:
                pass
            
            # save to database
        
    data = [i for i in Queries.objects.raw('SELECT * FROM project_queries')]
    print(data)
    return render(request, 'project/index.html', {'data': data})