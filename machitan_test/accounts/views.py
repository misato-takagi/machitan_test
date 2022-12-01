from django.shortcuts import render
from django.views import View
from accounts.models import CustomUser
from accounts.forms import ProfileForm

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id = request.user.id)

        return render(request, 'accounts/profile.html',{
            'user_data' : user_data,
        })

class ProfileEditView(View):
    def get(self,request, *args, **kwargs):
        user_data = CustomUser.objects.get(id = request.user.id)
        form = ProfileForm(
            request.POST or None,
            initial={
                'first_name':user_data.first_name,
                'last_name':user_data.last_name,
                'department':user_data.department,

            }
        )

        return render(request, 'accounts/profile_edit.html',{
            'form': form
        })
        
    def post(self,request,*args,**kwarg):
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            user_data = CustomUser.objects.get(id = request.user.id)
            
        