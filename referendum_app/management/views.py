from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Idea

class IdeaListView(ListView):
    model = Idea
    template_name = 'idea_list.html'
    context_object_name = 'ideas'
    ordering = ['-created_at']
    paginate_by = 5

class IdeaDetailView(DetailView):
    model = Idea
    template_name = 'idea_detail.html'

class IdeaCreateView(CreateView):
    model = Idea
    fields = ['title', 'content', 'author']
    template_name = 'idea_form.html'
    success_url = reverse_lazy('idea-list')

class IdeaUpdateView(UpdateView):
    model = Idea
    fields = ['title', 'content']
    template_name = 'idea_form.html'
    success_url = reverse_lazy('idea-list')

class IdeaDeleteView(DeleteView):
    model = Idea
    template_name = 'idea_confirm_delete.html'
    success_url = reverse_lazy('idea-list')
    