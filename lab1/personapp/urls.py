from django.urls import include, path
from rest_framework import routers
from personapp import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('persons', views.Persons.as_view()),
    path('persons/<int:pk>', views.Persons.as_view()),
]
