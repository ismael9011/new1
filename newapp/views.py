from django.http import HttpResponse
from django.shortcuts import render
from .models import Review

#need to set up HTML file for this code to work. Not done yet.
# def home(request):
#     return render(
#         request,
#         'newapp/newapp.html',
#         {
#             name : Review.name,
#             date : Review.pub_date,
#             rating : Review.rating,
#             text : Review.text
#         }
#     )




def home(request):
    latest_reviews = Review.objects.order_by('-pub_date')
    output = ""
    for review in latest_reviews:
        name = review.name
        date = review.pub_date.strftime("%H:%M:%S")
        rating = str(review.rating)
        text = review.text
        complete = "Name: %s\nDate Posted: %s\nRating: %s\nReview: %s" % (
            name,
            date,
            rating,
            text,
        )
        #complete = "Name: " + name + "date posted: " + date + "rating: " + rating + "Review: " + text 
        output += complete
    return HttpResponse(output)
#     #return HttpResponse("Name: {review.name}<br>Rating: {review.rating}<br>Review: {review.text}<br> Posted: {review.pub_date} ")
     
    

#def index(request):
    review = Review.objects.all()
    output = "<br>".join([each_review.review_text for each_review in review])

    return HttpResponse(output)
