from models import Trip,Place
from django.template.defaultfilters import slugify
from yelp.client import Client
from yelp.client import Search
from yelp.oauth1_authenticator import Oauth1Authenticator


def get_places(location=''):
    places=[]
    if location:
                places = Place.objects.filter(locationSlug = slugify(location))

    return places




def get_trip_list(max_results=0, starts_with=''):
        trip_list = []
        if starts_with:
                trip_list = Trip.objects.filter(title__contains= starts_with)

        if max_results > 0:
                if trip_list.count() > max_results:
                        trip_list = trip_list[:max_results]

        return trip_list

def get_places_names(places):
    p = []
    for place in places:
        p.append(place)
    return p


def get_rating(location ='', place=''):
    auth = Oauth1Authenticator(
        consumer_key="AcNjWSnQhcaCtzlsocii5g",
        consumer_secret="JoTx1Cw8i_fqn4JHFgA3T78ubHQ",
        token="cG9DZ7bYvHAHPtw9Clff8jCMKTHQu56p",
        token_secret="eD9yzfz34788kedMTMlpDWlh9Co"
    )

    client = Client(auth)
    params = {
        'term': place
    }

    response = Search(client).search(location, **params)

    if len(response.businesses) > 0:
        return response.businesses[0].rating
    return 'No ratings'