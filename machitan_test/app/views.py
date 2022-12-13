from django.shortcuts import render,get_object_or_404
from django.views.generic import View
#ログインしていない場合はログインページへ進むように設定する
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Store,Staff,Booking
from datetime import datetime, date, timedelta, time
from django.db.models import Q
from django.utils.timezone import localtime, make_aware


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

class CalenderView(View):
    def get(self,request, *args, **kwargs):
        staff_data = Staff.objects.filter(id = self.kwargs['pk']).select_related('user').select_related('store')[0]
        today = date.today()
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        if year and month and day:
            start_date = date(year=year,month=month,day=day)
        else:
            start_date = today
        days = [start_date + timedelta(days=day) for day in range(7)]
        start_day = days[0]
        end_day = days[-1]

        calender = {}
        for hour in range(10,21):
            row = {}
            for day in days:
                row[day] = True
                calender[hour] = row
            start_time = make_aware(datetime.combine(start_day, time(hour=10,minute=0,second=0)))
            end_time = make_aware(datetime.combine(end_day,time(hour=20, minute=15,second=0)))
            booking_data = Booking.objects.filter(staff= staff_data).exclude(Q(start__gt = end_time)| Q(end__lt = start_time ))
            for booking in booking_data:
                local_time = localtime(booking.start)
                booking_date = local_time.date()
                booking_hour = local_time.hour()
                if (booking_hour in calender) and (booking_date in calender[booking_hour]):
                    calender[booking_hour][booking_date] = False

            return render(request, 'app/calender.html',{
                'staff_data':staff_data,
                'calender':calender,
                'days': days,
                'start_day': start_day,
                'end_day': end_day,
                'before':days[0]- timedelta(days=7),
                'next': days[-1] + timedelta(days=1),
                'today' : today, 
            })
