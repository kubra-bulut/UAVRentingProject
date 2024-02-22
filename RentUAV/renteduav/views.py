
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic.edit import CreateView,  UpdateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import  RentedUavs

import pyautogui as pu


# Create your views here.
# Only logged in superuser can see this view
class RentedUavCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = RentedUavs
    template_name = "createrented.html"
    fields=['id','uav','date','member']
    login_url = 'login'  #if not authenticated redirect to login page

    # only superuser is allowed to see this view.
    def test_func(self):
        return self.request.user.is_superuser

    # url to redirect after successfully creation
    def get_success_url(self):
         #Displaying message of successful creation of new employee
         pu.alert(text='New Uav Created Successfully',title='Create',button='OK')
         return reverse_lazy('renteduav-list')


# Only logged in superuser can see this view
class RentedUavListView(LoginRequiredMixin,UserPassesTestMixin,ListView):

    model = RentedUavs
    template_name = 'showrented.html'
    context_object_name = 'renteduav'
    paginate_by = 5
    login_url = 'login' #if not authenticated redirect to login page

    # only superuser is allowed to see this view.
    def test_func(self):
        return self.request.user.is_superuser


    def get_queryset(self):  # new

        if self.request.method == "GET":
            query = self.request.GET.get('search')  # your input name is 'search'
            print('Search word:' + str(query))
        if query:
            return RentedUavs.objects.filter(uav=query)

        else:
            return RentedUavs.objects.all()

    def get_context_data(self, **kwargs):
        context = super(RentedUavListView, self).get_context_data(**kwargs)
        renteduavs = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(renteduavs, self.paginate_by)
        try:
            renteduavs = paginator.page(page)
        except PageNotAnInteger:
            renteduavs = paginator.page(1)
        except EmptyPage:
            renteduavs = paginator.page(paginator.num_pages)
        context['renteduavs'] = renteduavs
        return context



# Only logged in superuser can see this view
class RentedUavUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = RentedUavs
    template_name = 'updaterented.html'
    # specify the fields
    fields = ['id',
                  'uav',
                  'date',
                  'member']
    login_url = 'login' #if not authenticated redirect to login page

    # only superuser is allowed to see this view.
    def test_func(self):
        return self.request.user.is_superuser

    # updating details
    # url to redirect after successfully updation
    def get_success_url(self):
         # Displaying message of successful updation of  employee
         pu.alert(text='Uav Info Updated Successfully', title='Update', button='OK')
         return reverse_lazy('renteduav-list')














