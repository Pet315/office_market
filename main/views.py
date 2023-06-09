from django.http import HttpResponseNotFound
from django.shortcuts import render
from main.models import *
from SPARQLWrapper import SPARQLWrapper, JSON


def category(request):
    categories = Category.objects.all()
    user_profile = request.user
    # print(request.user.id)
    return render(request, 'categories.html', context={'categories': categories, 'user_profile': user_profile})


def product(request, id: int):
    if id > Category.objects.latest('id').id:
        return HttpResponseNotFound('Wrong number')
    user_profile = request.user
    products = Product.objects.filter(category_id=id)
    return render(request, 'products.html', context={'products': products, 'user_profile': user_profile})


def cart(request):
    user_profile = request.user
    return render(request, 'cart.html', context={'user_profile': user_profile})


def edit_cart_product(product_id, way, user_id):
    if product_id > len(Product.objects.filter()):
        return HttpResponseNotFound('Wrong number')

    product = Cart.objects.filter(product_id=product_id, user_id=user_id)

    if len(product) == 0:
        quantity = 0
    else:
        quantity = product[0].quantity
    product.delete()

    cart = Cart()
    cart.product_id = product_id
    if str(way) == '+':
        cart.quantity = quantity + 1
    else:
        cart.quantity = quantity - 1
    cart.user_id = user_id
    cart.save()


def add_to_cart(request, id: int):
    edit_cart_product(id, '+', request.user.id)
    return render(request, 'cart.html', context={'cart': Cart.objects.all()})


def delete_from_cart(request, id: int):
    edit_cart_product(id, '-', request.user.id)
    return render(request, 'cart.html', context={'cart': Cart.objects.all()})


def send_order(request):
    orders = Cart.objects.filter(user_id=request.user.id)
    print(orders)
    for ord in orders:
        order = Order()
        order.product_id, order.quantity, order.user_id, order.email = ord.product_id, ord.quantity, \
                                                                       ord.user_id, request.POST.get('email')
        order.save()
        ord.delete()
    return render(request, 'order.html')


def about(request):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    query = """
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        
        SELECT ?company ?label ?description ?foundingDate ?owner
        WHERE {
          ?company rdf:type dbo:Company ;
                   rdfs:label ?label ;
                   dbo:abstract ?description ;
                   dbo:foundingDate ?foundingDate ;
                   dbo:owner ?ownerResource .
          
          ?ownerResource foaf:name ?owner .
          
          FILTER (LANG(?label) = 'en' && LANG(?description) = 'en' && REGEX(STR(?label), "Staples", "i"))
        }
        LIMIT 1
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    content = {}
    for result in results["results"]["bindings"]:
        content = result
    print(content)
    name = content['label']['value']
    desc = content['description']['value']
    founded = content['foundingDate']['value']
    owner = content['owner']['value']
    return render(request, 'about.html', context={"name": name, 'desc': desc, 'founded': founded, 'owner': owner})


# {'company': {'type': 'uri', 'value': 'http://dbpedia.org/resource/Staples_Inc.'}, 'label': {'type': 'literal', 'xml:lang': 'en', 'value': 'Staples Inc.'}, 'description': {'type': 'literal', 'xml:lang': 'en', 'value': 'Staples Inc. is an American retail company headquartered in Framingham, Massachusetts, that offers products and services designed to support working and learning. The company opened its first store in Brighton, Massachusetts on May 1, 1986. By 1996, it had reached the Fortune 500, and it later acquired the office supplies company Quill Corporation. In 2014, in the wake of increasing competition from e-commerce market, Staples began to close some of its locations. In 2015, Staples announced its intent to acquire Office Depot and OfficeMax. However, the purchase was blocked under antitrust grounds due to the consolidation that would result. After the failed acquisition, Staples began to refocus its operations to downplay its brick-and-mortar outlets, and place more prominence on its B2B supply business. In 2017, after its sale to Sycamore Partners, the company was effectively split into three "independently managed and capitalized" entities sharing the Staples name, separating its U.S. retail operations, and Canadian retail operations, from the B2B business.'}, 'foundingDate': {'type': 'typed-literal', 'datatype': 'http://www.w3.org/2001/XMLSchema#date', 'value': '1986-05-01'}}

