from django.shortcuts import render
from main.models import ProductCategory,Product,Page
Page.page_direction = 0
Page.check_woman = False
Page.check_man = False
def pag(request,a):
    if request.method == 'POST':
        items = []
        if 'pre' in request.POST:
            Page.page_direction-=1
            if Page.check_man:
                l = 0
                for prod in Product.objects.filter(category=a,gender='man'):
                    l += 1
                    if l > Page.page_direction * 8 + 8:
                        l = 0
                        break
                    elif l <= 8 * Page.page_direction + 8 and (l > Page.page_direction * 8):
                        items = items + [prod]
                    else:
                        continue
            elif Page.check_woman:
                l = 0
                for prod in Product.objects.filter(category=a, gender='woman'):
                    l += 1
                    if l > Page.page_direction * 8 + 8:
                        l = 0
                        break
                    elif l <= 8 * Page.page_direction + 8 and (l > Page.page_direction * 8):
                        items = items + [prod]
                    else:
                        continue
            else:
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
            if Page.check_man:
                l = 0
                for prod in Product.objects.filter(category=a, gender='man'):
                    l += 1
                    if l > Page.page_direction * 8 + 8:
                        l = 0
                        break
                    elif l <= 8 * Page.page_direction + 8 and (l > Page.page_direction * 8):
                        items = items + [prod]
                    else:
                        continue
            elif Page.check_woman:
                l = 0
                for prod in Product.objects.filter(category=a, gender='woman'):
                    l += 1
                    if l > Page.page_direction * 8 + 8:
                        l = 0
                        break
                    elif l <= 8 * Page.page_direction + 8 and (l > Page.page_direction * 8):
                        items = items + [prod]
                    else:
                        continue
            else:
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
            if Page.check_man:
                for item in Product.objects.filter(name__icontains=search_name,category=a,gender='man'):
                    items = items + [item]
                if len(items) == 0:
                    Page.check_quality = False
                else:
                    Page.check_quality = True
            elif Page.check_woman:
                for item in Product.objects.filter(name__icontains=search_name,category=a,gender='woman'):
                    items = items + [item]
                if len(items) == 0:
                    Page.check_quality = False
                else:
                    Page.check_quality = True
            else:
                for item in Product.objects.filter(name__icontains=search_name,category=a):
                    items = items + [item]
                if len(items) == 0:
                    Page.check_quality = False
                else:
                    Page.check_quality = True
        elif 'man' in request.POST:
            Page.check_man = True
            Page.check_woman = False
            items =[]
            l = Page.page_direction * 8
            for prod in Product.objects.filter(category=a,gender='man'):
                l += 1
                if l <= 8 * Page.page_direction + 8:
                    items = items + [prod]
                else:
                    break
        elif 'woman' in request.POST:
            Page.check_man = False
            Page.check_woman = True
            items =[]
            l = Page.page_direction * 8
            for prod in Product.objects.filter(category=a,gender='woman'):
                l += 1
                if l <= 8 * Page.page_direction + 8:
                    items = items + [prod]
                else:
                    break

    else:
        items = []
        l = Page.page_direction*8
        for prod in Product.objects.filter(category=a):
            l += 1
            if l <= 8 * Page.page_direction + 8:
                items = items + [prod]
            else:
                break
    if Page.check_man:
        if items[-1].id == Product.objects.filter(category=a,gender='man').last().id:
            check_last = False
        else:
            check_last = True
    elif Page.check_woman:
        if items[-1].id == Product.objects.filter(category=a,gender='woman').last().id:
            check_last = False
        else:
            check_last = True
    else:
        if items[-1].name == Product.objects.filter(category=a).last().name:
            check_last = False
        else:
            check_last = True
    context ={
        'products': items,
        'pre': Page.page_direction,
        'check': Page.check_quality,
        'check_last': check_last,
    }
    return context
def index(request):
    Page.page_direction = 0
    context = {
        'url':Page.url
    }
    return render(request, 'main/index.html',context)
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