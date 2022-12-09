from django.shortcuts import render,get_object_or_404
from django.views.generic import View
#ログインしていない場合はログインページへ進むように設定する
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Store,Staff

class StoreView(View):
    def get(self,request, *args, **kwargs):
        #Store情報を全て取得する
        store_data = Store.objects.all()

        return render(request, 'app/store.html',{
            'store_data':store_data
        })

class StaffView(View):
    def get(self,request, *args, **kwargs):
        store_data = get_object_or_404(Store,id = self.kwargs['pk'] )
        staff_data = Staff.objects.filter(store = store_data).select_related('user')

        return render(request, 'app/staff.html',{
            'store_data':store_data,
            'staff_data':staff_data,
        })