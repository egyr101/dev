from django.shortcuts import render
def index(request):
    return render(request, 'main/index.html')
def sneakers(request):
    path = request.META['QUERY_STRING']
    return render(request, 'main/prodcatalog.html',{'pol': path}
                  )

def boots(request):
    return render(request, 'main/prodcatalog.html',)

def bags(request):
    return render(request, 'main/prodcatalog.html')

def perfumery(request):
    return render(request, 'main/prodcatalog.html')

def accessories(request):
    return render(request, 'main/prodcatalog.html')

def sunglasses(request):
    return render(request, 'main/prodcatalog.html')
def products(request):

    return render(request, 'main/prodcard.html' )