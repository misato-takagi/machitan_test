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
    #予約のURL
    path('booking/<int:pk>/<int:year>/<int:month>/<int:day>/<int:hour>',views.BookingView.as_view(),name='booking'),
    #予約完了URL
    path('thanks/',views.ThanksView.as_view(),name='thanks'),
    #スタッフ専用ページ
    path('mypage/<int:year>/<int:month>/<int:day>/',views.MypageView.as_view(),name='mypage'),
    #スタッフが休日設定できるページ
    path('mypage/holiday/<int:year>/<int:month>/<int:day>/<int:hour>',views.Holiday,name='holiday'),
    #予約をキャンセルするページ
    path('mypage/delete/<int:year>/<int:month>/<int:day>/<int:hour>',views.Delete,name='delete'),



]