from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Properties

import pyautogui as pu


# Create your views here.
# Only logged in superuser can see this view
class UavCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Properties
    template_name = "create.html"
    fields=['id','model','brand','weight','category']
    login_url = 'login'  #if not authenticated redirect to login page

    # only superuser is allowed to see this view.
    def test_func(self):
        return self.request.user.is_superuser

    # url to redirect after successfully creation
    def get_success_url(self):
         #Displaying message of successful creation of new employee
         pu.alert(text='New Uav Created Successfully',title='Create',button='OK')
         return reverse_lazy('uav-list')


# Only logged in superuser can see this view
class UavListView(LoginRequiredMixin,UserPassesTestMixin,ListView):

    model = Properties
    template_name = 'show.html'
    context_object_name = 'uavs'
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
            return Properties.objects.filter(model=query)

        else:
            return Properties.objects.all()

    def get_context_data(self, **kwargs):
        context = super(UavListView, self).get_context_data(**kwargs)
        uavs = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(uavs, self.paginate_by)
        try:
            uavs = paginator.page(page)
        except PageNotAnInteger:
            uavs = paginator.page(1)
        except EmptyPage:
            uavs = paginator.page(paginator.num_pages)
        context['uavs'] = uavs
        return context



# Only logged in superuser can see this view
class UavDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):

    model = Properties
    template_name = 'detail.html'
    login_url = 'login' #if not authenticated redirect to login page

    # only superuser is allowed to see this view.
    def test_func(self):
        return self.request.user.is_superuser
   

# Only logged in superuser can see this view
class UavUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Properties
    template_name = 'update.html'
    # specify the fields
    fields = ['id',
                  'model',
                  'brand',
                  'weight',
                  'category']
    login_url = 'login' #if not authenticated redirect to login page

    # only superuser is allowed to see this view.
    def test_func(self):
        return self.request.user.is_superuser

    # updating details
    # url to redirect after successfully updation
    def get_success_url(self):
         # Displaying message of successful updation of  employee
         pu.alert(text='Uav Info Updated Successfully', title='Update', button='OK')
         return reverse_lazy('uav-list')



# Only logged in superuser can see this view
class UavDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Properties
    template_name = 'delete.html'
    login_url = 'login' #if not authenticated redirect to login page

    # only superuser is allowed to see this view.
    def test_func(self):
        return self.request.user.is_superuser

    # url to redirect after successfully deletion
    def get_success_url(self):
        # Displaying message of successful deletion of employee
         pu.alert(text='Uav Deleted Successfully', title='Delete', button='OK')
         return reverse_lazy('uav-list')










