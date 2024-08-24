from django.shortcuts import render
from main.models import ProductCategory,Product,Page
Page.page_direction = 0
def pag(request,a):
    if request.method == 'POST':
        items = []
        if 'pre' in request.POST:
            Page.page_direction-=1
            l = 0
            for prod in Product.objects.filter(category=a):
                l += 1
                if l > Page.page_direction * 8 + 8:
                    l = 0
                    break
                elif l <= 8 * Page.page_direction + 8 and (l > Page.page_direction * 8):
                    items = items + [prod]
                else:
                    continue
        elif 'next' in request.POST:
            Page.page_direction+=1
            l = 0
            for prod in Product.objects.filter(category=a):
                l += 1
                if l > Page.page_direction * 8 + 8:
                    l = 0
                    break
                elif l <= 8 * Page.page_direction + 8 and (l > Page.page_direction * 8):
                    items = items + [prod]
                else:
                    continue
        elif 'search-name' in request.POST:
            search_name = request.POST.get('search-str',1)
            for item in Product.objects.filter(name__icontains=search_name,category=a):
                items = items + [item]
            if len(items) == 0:
                Page.check_quality = False
            else:
                Page.check_quality = True

    else:
        items = []
        l = Page.page_direction*8
        for prod in Product.objects.filter(category=a):
            l += 1
            if l <= 8 * Page.page_direction + 8:
                items = items + [prod]
            else:
                break
    context ={
        'products': items,
        'pre': Page.page_direction,
        'check': Page.check_quality,
    }
    return context
def index(request):
    Page.page_direction = 0
    return render(request, 'main/index.html')
def sneakers(request):
    return render(request, 'main/prodcatalog.html',pag(request,2))

def boots(request):
    return render(request, 'main/prodcatalog.html',pag(request,1))

def bags(request):
    return render(request, 'main/prodcatalog.html',pag(request,3))

def perfumery(request):
    return render(request, 'main/prodcatalog.html',pag(request,4))

def accessories(request):
    return render(request, 'main/prodcatalog.html',pag(request,5))

def sunglasses(request):
    return render(request, 'main/prodcatalog.html',pag(request,6))
def product(request,category,name):
    context = {
        'product':Product.objects.get(name=name)
    }
    return render(request, 'main/prodcard.html', context)