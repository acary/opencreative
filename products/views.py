import datetime
from django.core.mail import send_mail, get_connection
from django.shortcuts import get_object_or_404,render, redirect
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import path, include, reverse
from urllib.parse import urlencode
from django.contrib.auth.decorators import login_required
from .models import Product, Offer
from django.utils import timezone
from .forms import SelectionForm
import requests

def products(request):
    products = Product.objects.all().order_by('-votes_total')
    context = {
        "products": products,
    }
    return render(request, 'products/home.html', context)

def product_category(request, category):
    products = Product.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-pub_date'
    )
    context = {
        "category": category,
        "products": products,
    }
    return render(request, "products/product_category.html", context)

def brand(request, contributor):

    # Get offers from contributor, if any
    offer = Offer.objects.filter(
        contributor__username__contains=contributor
    )

    # Get Products associated with contributor
    products = Product.objects.filter(
        contributor__username__contains=contributor
    ).order_by(
        '-pub_date'
    )
    context = {
        # "category": category,
        "products": products,
        "contributor": contributor,
        "offer": offer,
    }
    return render(request, "products/brand.html", context)

def brand_product_category(request, contributor, category):
    products = Product.objects.filter(
        contributor__username__contains=contributor,
        categories__name__contains=category
    ).order_by(
        '-pub_date'
    )
    context = {
        "contributor": contributor,
        "category": category,
        "products": products,
    }
    return render(request, "products/brand_product_category.html", context)

def brand_landing(request, contributor):
    offer = Offer.objects.filter(
        contributor__username__contains=contributor
    ).order_by(
        'priority'
    )
    context = {
        # "category": category,
        "offer": offer,
        "contributor": contributor,
    }
    return render(request, "products/brand_landing.html", context)

def brand_select(request, contributor):

    offer = Offer.objects.filter(
        contributor__username__contains=contributor
    ).order_by(
        'priority'
    )

    # TODO: PASS OFFER AS PARAMETER TO REVIEW
    current_offer = offer[0].id
    print(current_offer)

    form = SelectionForm()

    context = {
        "offer": offer,
        "contributor": contributor,
        "form": form,
    }
    return render(request, "products/brand_select.html", context)

def brand_review(request, contributor):

    def send_order():
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        con = get_connection(EMAIL_BACKEND)
        send_mail(
            "Subject",              # Subject
            "Message",              # Message
            "andy@andycary.com",    # From
            ["info@andycary.com"],  # To
            fail_silently=False,
            connection=con
        )

    # TODO: GET OFFER DIRECTLY
    # offer = Offer.objects.filter(
    #     pk=1
    # )

    offer = Offer.objects.filter(
        contributor__username__contains=contributor
    ).order_by(
        'priority'
    )

    form = SelectionForm()
    # form_data = request.session.pop('data', {"product_type": "energy"})
    # product_type = form_data.get("product_type")
    # product_size = form_data.get("product_size")

    if request.method == 'POST':
        now = datetime.datetime.now()

        form = SelectionForm(request.POST)

        if form.is_valid():

            product_type=form.cleaned_data["product_type"]
            product_size=form.cleaned_data["product_size"]
            product_freq=form.cleaned_data["product_freq"]

            data={
                'timestamp': now,
                'product_type': product_type,
                'product_size': product_size[0],
                'product_freq': product_freq[0],
            }
            print(data)
            send_order()

    if request.method == 'GET':
        context = {
            "offer": offer,
            "contributor": contributor,
        }
        return render(request, "products/brand_landing.html", context)

    context = {
        "offer": offer,
        "contributor": contributor,
        "form": form,
    }
    return render(request, "products/brand_review.html", context)

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.contributor = request.user
            product.save()
            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'products/create.html',{'error': 'All fields are required'})
    else:
        return render(request, 'products/create.html')

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html',{'product': product})

@login_required(login_url="/accounts/sign_up")
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/products/' + str(product.id))
