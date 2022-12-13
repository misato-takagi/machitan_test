from django.urls import path
from app import views

urlpatterns = [
    path('',views.StoreView.as_view(),name='store'),
    #店舗を選んだらその店の情報とスタッフが出てくる
    path('store/<int:pk>',views.StaffView.as_view(),name='staff'),
    #日程を指定しない場合のURL
    path('calender/<int:pk>',views.CalenderView.as_view(),name='calender'),
    #日程を指定した場合のURL
    path('calender/<int:pk>/<int:year>/<int:month>/<int:day>',views.CalenderView.as_view(),name='calender'),


]