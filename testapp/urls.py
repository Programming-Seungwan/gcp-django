from django.urls import path
from testapp.views import BoardsListClassView, BoardsListFunctionView


urlpatterns = [
    path('cbvList', BoardsListClassView.as_view(), name="cbv"),
    path('fbvList', BoardsListFunctionView, name="fbv")
]