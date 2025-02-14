from django.shortcuts import render
from django.views import generic
from .models import Memo, Tag
from django.urls import reverse_lazy
from .forms import SearchForm

class IndexView(generic.ListView):
    model = Memo
    template_name = 'memo/index.html'

class DetailView(generic.DetailView):
    model = Memo
    template_name = 'memo/detail.html'

class MemoCreateView(generic.CreateView):
    model = Memo
    template_name = 'memo/create.html'
    fields = '__all__'

class UpdateView(generic.UpdateView):
    model = Memo
    template_name = 'memo/create.html'
    fields = '__all__'

class DeleteView(generic.DeleteView):
    model = Memo
    template_name = 'memo/delete.html'
    success_url = reverse_lazy('memo:index')

class TagCreateView(generic.CreateView):
    model = Tag
    template_name = 'tag/create.html'
    fields = '__all__'
    success_url = reverse_lazy('memo:index')

def search(request):
    memo = None
    searchform = SearchForm(request.GET)
    
  # Formに正常なデータがあれば
    if searchform.is_valid():
        query = searchform.cleaned_data['words']   # queryにフォームが持っているデータを代入
        memo = Article.objects.filter(content__icontains=query)    # クエリを含むレコードをfilterメソッドで取り出し、articles変数に代入
        return render(request, 'memo/results.html', {'memos':memo,'searchform':searchform})