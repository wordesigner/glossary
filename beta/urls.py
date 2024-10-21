from django.urls import path
from . import views

urlpatterns = [
    path('', views.Search.as_view(), name='index'),
    path('feedback', views.Feedback.as_view(), name='feedback'),
    path('success', views.success, name='success'),
    path('xreport', views.xreport, name='xreport'),
    path('browse', views.browse, name='browse'),
    path('comment', views.Comment.as_view(), name='commentt'),
    path('breport', views.breport, name='breport')
]

