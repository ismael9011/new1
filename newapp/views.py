from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Review, Properties


# view gets request and returns HTTPresponse or HTML rendered in the folder 'templates'

# get request for home page, appends fields to models to then use in home.html in the folder 'templates', then render home.html
def home(request):
    latest_reviews = Review.objects.order_by('-pub_date')
    # IMPORTANT: get all properties in the properties model
    try:
        properties = Properties.objects.all()
    except Properties.DoesNotExist:
        properties = None

    return render(request, 'home.html', {'latest_reviews': latest_reviews, 'properties': properties})

def property_detail(request, property_id):
    # Get the property with the specified property_id from the database
    property_instance = get_object_or_404(Properties, id=property_id)
    
    # Get the reviews associated with the property using the reverse relationship
    reviews = property_instance.review_set.all()

    # Pass the property_instance to the template for rendering
    return render(request, 'property_detail.html', {'property': property_instance, 'reviews': reviews})

#def index(request):
    review = Review.objects.all()
    output = "<br>".join([each_review.review_text for each_review in review])

    return HttpResponse(output)

