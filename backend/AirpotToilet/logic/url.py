from . import views
from django.urls import path

urlpatterns = [
    # STAFF API's
    path('insertstaff', views.createStaff),
    path('getstaff', views.getStaff),
    path('updatestaff/<Sid>/', views.updateStaff),
    path('deletestaff/<Sid>/', views.deleteStaff),

    # FEEDBACK API's
    path('insertfeedack', views.createFeedback),
    path('getfeedback', views.getFeedback),
    path('updatefeedback/<Fid>/', views.updateFeedback),
    path('deletefeedback/<Fid>/', views.deleteFeedback),

]