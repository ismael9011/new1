from django.http import HttpResponse
from django.shortcuts import render
from .models import Review, Properties

# view gets request and returns HTTPresponse or HTML rendered in the folder 'templates'

# get request for home page, appends fields to models to then use in home.html in the folder 'templates', then render home.html
def home(request):
    latest_reviews = Review.objects.order_by('-pub_date')
    # IMPORTANT: Assuming you want to display the first property in the template
    try:
        property = Properties.objects.first()
    except Properties.DoesNotExist:
        property = None

    return render(request, 'home.html', {'latest_reviews': latest_reviews, 'property': property})



#def index(request):
    review = Review.objects.all()
    output = "<br>".join([each_review.review_text for each_review in review])

    return HttpResponse(output)