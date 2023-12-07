
# from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View
from .models import Fooditems
from .form import AddFoodItems
from django.views import generic

# Create your views here.

# this code is in generic views which works the same as code above

class foodhome(generic.ListView):
    model = Fooditems
    context_object_name = "itemModel"
    template_name = "fooditems/index.html"
    
    def get_queryset(self):
        return Fooditems.objects.filter(user = self.request.user)
        # return Fooditems.objects.all().values()
 


class addItems(generic.CreateView):
    model = Fooditems
    template_name = "fooditems/Additems.html"
    form_class = AddFoodItems
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return "/fooditems"
    
    
    
class deleteItems(generic.DeleteView):
    model = Fooditems
    success_url = '/fooditems'
    
    def get_object(self):
        id = self.request.POST.get('id')
        # id = self.kwargs.get('pk')
        return Fooditems.objects.get(id=id)
    
    
class editItems(View):
    def get(self, request, id):
        model = Fooditems.objects.get(id=id)
        fm = AddFoodItems(instance=model)
        return render(request, 'fooditems/Edititems.html',{'form': fm})
      
    def post(self, request, id):
        model = Fooditems.objects.get(id=id)
        fm = AddFoodItems(request.POST, instance=model)
        
        if fm.is_valid():
            fm.save()
            return redirect('foodhome')

# class getUser(generic.ListView):
#     model = CustomUser
#     context_object_name = "userModel"
#     template_name = "fooditems/index.html"

#     def get_queryset(self):
#         return CustomUser.objects.all().values()
    
# class addUser(generic.CreateView):
#     model = CustomUser
#     template_name = "users/userform.html"
#     form_class = uForm
    
#     def get_success_url(self):
#         return "/fooditems"

# @login_required(login_url='')
# class foodhome(View):
#      def get(self, request):
#          itemModel = Fooditems.objects.all().values()
#          return render(request, 'fooditems/index.html', {'itemModel': itemModel})
     
# class addItems(View):
#     # pass
#     def get(self, request):
#         fm = AddFoodItems
#         return render(request, 'fooditems/Additems.html', {'form': fm})
    
#     def post(self, request):
#         fm = AddFoodItems(request.POST)
#         if fm.is_valid():
#             fm.save()
#             return redirect('foodhome')
#         else:
#             return render(request, 'fooditems/Additems.html', {"form":fm})

# class deleteItems(View):
#     def post(self, request):
#         data = request.POST
#         id = data.get('id')
#         model = Fooditems.objects.get(id=id)
#         print(model, ' Successfully deleted!!')
#         model.delete()
#         return redirect('foodhome')