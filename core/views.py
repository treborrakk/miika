from django.shortcuts import render, get_object_or_404 , redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import LookupSerializers
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


from .forms import SubjectForm
from .models import Subject, LookupType, Lookup

from django.conf import settings
# from .models import *

# def home(request):
#     return render(request, 'core/home.html', {'title': 'About'})

def check_group(user):
    # First check if the user belongs to the group
    if user.groups.filter(name='miika_admin').exists():
        return True
# @login_required
# @user_passes_test(check_group, login_url='/post/error403/')

class check_group_mixin(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.groups.filter(name='miika_admin').exists():
            return True


@login_required
def home(request):
    context = {'subjects': Subject.objects.all()}
    return render(request, 'core/home.html', context)

    # if not request.user.is_authenticated:
    #     print("not valid")
    #     # return render(request, 'users/login.html')
    #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    # else:
    #     # context = {'subjects': Subject.objects.all()}
    #     return render(request, 'core/home.html', context)



# def about(request):
#     return render(request, 'core/about.html', {'title': 'About'})

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'core/class_subject_list.html', {
        'subjects': subjects
    })



@user_passes_test(check_group, login_url='/core/error403/')

def delete_subject(request, pk):
    if request.method == 'POST':
        subject = Subject.objects.get(pk=pk)
        subject.delete()
    return redirect('subject_list')

def edit_subject(request, id):
    subject = Subject.objects.get(id=id)
    form = SubjectForm(instance=subject)
    context = {
        'subject': subject,
        'form': form,
    }
    return render(request, 'core/edit_subject.html', context=context)

# def update_subject(request, id):
#     subject = Subject.objects.get(id=id)
#     # form = TestForm(instance=deliveryreceipt)
#     form = SubjectForm(request.POST, instance = subject)
#     if form.is_valid():
#         form.save()
#         # rmc 11/08/2021 - Start
#         created_updated(Subject, request)
#         # rmc 11/08/2021 - End
#         return redirect("/core")
#     else:
#         messages.error(request, "Error")
#         print(messages.error(request, "Error"))
#         return render(request, 'core/pagedisplayerror.html', {'form': form})
#     return render(request, 'core/edit_subject.html', {'subject': subject})

def update_subject(request, id):
    subject = Subject.objects.get(id=id)
    if request.method=='POST':
        form = SubjectForm(request.POST, request.FILES, instance = subject)
        if form.is_valid():
            form.save()
             # rmc 11/08/2021 - Start
            created_updated(Subject, request)
            # rmc 11/08/2021 - End
            return redirect("/core")
        else:
            messages.error(request, "Error")
            print(messages.error(request, "Error"))
            return render(request, 'core/pagedisplayerror.html', {'form': form})
    else:
         form = SubjectForm(instance=subject)
    return render(request, 'core/edit_subject.html', {'subject': subject})

def created_updated(model, request):
    obj = model.objects.latest('pk')
    print(obj.created_by)
    if obj.created_by is None:
        obj.created_by = request.user
        # obj.dispatcher = request.user
    obj.updated_by = request.user
    obj.save()

def error403(request):
    return render(request, "core/error403.html", {'title':'error403'})

class SubjectListView(ListView):
    model = Subject
    template_name = 'core/class_subject_list.html'
    context_object_name = 'subjects'


# @login_required
# @method_decorator(login_required, name='dispatch')
# @user_passes_test(check_group, login_url='/core/error403/')

# def upload_book(request):
#     if request.method == 'POST':
#         form = SubjectForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('class_subject_list')
#     else:
#         form = SubjectForm()
#     return render(request, 'core/upload_subject.html', {
#         'form': form
#     })


# class UploadSubjectView(LoginRequiredMixin,CreateView):
@method_decorator(login_required, name='dispatch')
class UploadSubjectView(check_group_mixin, CreateView):
    model = Subject
    form_class = SubjectForm
    success_url = reverse_lazy('core-home')
    template_name = 'core/upload_subject.html'



class LookupAPIView(generics.ListAPIView):
    serializer_class = LookupSerializers

    def get_queryset(self):
        queryset = Lookup.objects.all()
        src_key = self.request.query_params.get('lookup_type', None)
        print('what is the value of src_key')
        print(src_key)
        if src_key is not None:
            # queryset = queryset.filter(sono=src_key).order_by('drno').last()
            # queryset = queryset.filter(sono=src_key).order_by('drno')
            # queryset = queryset.filter(lookup_type=src_key,active="Yes").order_by('sequence').reverse()[:1]
            queryset = queryset.filter(lookup_type=src_key, active="Yes").order_by('sequence')
        print(queryset)
        return queryset

# RMC 0927
# from .models import Post

#
# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'core/home.html', context)
#
#
# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     ordering = ['-date_posted']
#     paginate_by = 5
#
#
# class UserPostListView(ListView):
#     model = Post
#     template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     paginate_by = 5
#
#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Post.objects.filter(author=user).order_by('-date_posted')
#
#
# class PostDetailView(DetailView):
#     model = Post
#
#
# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ['title', 'content']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#
# class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Post
#     fields = ['title', 'content']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False
#
#
# class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Post
#     success_url = '/'
#
#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False
#
#
# def about(request):
#     return render(request, 'core/about.html', {'title': 'About'})
#
# RMC 0927