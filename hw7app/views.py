from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Product
from .forms import ProductSearchForm

def product_search(request):
    form = ProductSearchForm(request.GET)
    query = form['query'].value()

    products = Product.objects.filter(title__icontains=query) | Product.objects.filter(description__icontains=query)

    paginator = Paginator(products, 10)  # Показывать 10 продуктов на странице

    page = request.GET.get('page')
    try:
        paged_products = paginator.page(page)
    except PageNotAnInteger:
        paged_products = paginator.page(1)
    except EmptyPage:
        paged_products = paginator.page(paginator.num_pages)

    context = {
        'form': form,
        'products': paged_products,
    }

    return render(request, 'product_search.html', context)

