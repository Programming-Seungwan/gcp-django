from django.urls import path
from testapp.views import BoardsListClassView, BoardsFunctionView


urlPatterns = [
    path('cbvList', BoardsListClassView.as_view(), name="cbv"),
    path('fbvList', BoardsFunctionView, name="fbv")
]