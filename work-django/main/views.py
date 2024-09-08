from django.shortcuts import render
from main.models import ProductCategory,Product,Page
from django.utils.text import slugify
Page.page_direction = 0
Page.check_woman = False
Page.check_man = False
def unloading_base(a,page):
    items = list(Product.objects.filter(category=a))
    if len(items) == 0:
        Page.check_quality = False
    else:
        items = items[page * 8:(page + 1) * 8]
        return items
def unloading_gender(a,gen,page):
    items = list(Product.objects.filter(category=a,gender=gen))
    if len(items) == 0:
        Page.check_quality = False
    else:
        items = items[page*8:(page+1)*8]
        return items
def unloading_searchname(a,page,search):
    items = list(Product.objects.filter(category=a, name__icontains=search))
    if len(items) == 0:
        Page.check_quality = False
    else:
        items = items[page * 8:(page + 1) * 8]
        return items
def unloading_searchname_gender(a,page,search,gen):
    items = list(Product.objects.filter(category=a, name__icontains=search,gender=gen))
    if len(items) == 0:
        Page.check_quality = False
    else:
        items = items[page * 8:(page + 1) * 8]
        return items

def pag(request,a):
    items = []
    if request.method == 'POST':
        if 'pre' in request.POST:
            Page.page_direction-=1
            if Page.check_man:
                items=unloading_gender(a,'man',Page.page_direction)
            elif Page.check_woman:
                items=unloading_gender(a, 'woman', Page.page_direction)
            else:
                items=unloading_base(a,Page.page_direction)
        elif 'next' in request.POST:
            Page.page_direction+=1
            if Page.check_man:
                items=unloading_gender(a, 'man', Page.page_direction)
            elif Page.check_woman:
                items=unloading_gender(a, 'woman', Page.page_direction)
            else:
                unloading_base(a, Page.page_direction)
        elif 'search-name' in request.POST:
            Page.search_name = request.POST.get('search-str',1)
            if Page.check_man:
                items=unloading_searchname_gender(a,Page.page_direction,Page.search_name,'man')
            elif Page.check_woman:
                items=unloading_searchname_gender(a, Page.page_direction, Page.search_name, 'woman')
            else:
               items=unloading_searchname(a,Page.page_direction, Page.search_name)
        elif 'man' in request.POST:
            Page.check_man = True
            Page.check_woman = False
            Page.page_direction = 0
            items=unloading_gender(a,'man',Page.page_direction)
        elif 'woman' in request.POST:
            Page.check_man = False
            Page.check_woman = True
            Page.page_direction = 0
            items=unloading_gender(a,'woman',Page.page_direction)

    else:
        items=unloading_base(a,Page.page_direction)
    if Page.check_quality == True:
        if Page.check_man:
            if Page.search_name != ' ':
                if items[-1].id == Product.objects.filter(name__icontains=Page.search_name, category=a,gender='man').last().id:
                    check_last = False
                else:
                    check_last = True
            else:
                if items[-1].id == Product.objects.filter(category=a, gender='man').last().id:
                    check_last = False
                else:
                    check_last = True
        elif Page.check_woman:
            if Page.search_name != ' ':
                if items[-1].id == Product.objects.filter(name__icontains=Page.search_name,category=a,gender='woman').last().id:
                    check_last = False
                else:
                    check_last = True
            else:
                if items[-1].id == Product.objects.filter(category=a,gender='woman').last().id:
                    check_last = False
                else:
                    check_last = True
        else:
            if Page.search_name !=' ':
                if items[-1].id == Product.objects.filter(category=a,name__icontains=Page.search_name).last().id:
                    check_last = False
                else:
                    check_last = True
            else:
                if items[-1].id == Product.objects.filter(category=a).last().id:
                    check_last = False
                else:
                    check_last = True
    else:
        check_last = False
    context ={
        'products': items,
        'pre': Page.page_direction,
        'check': Page.check_quality,
        'check_last': check_last,
    }
    return context
def index(request):
    Page.page_direction = 0
    Page.check_woman = False
    Page.check_man = False
    Page.search_name = ' '
    Page.check_quality = True
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
def product(request,category,id):
    Page.page_direction = 0
    context = {
        'product':Product.objects.get(id=id),

    }
    return render(request, 'main/prodcard.html', context)