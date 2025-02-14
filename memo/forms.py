from django import forms
from .models import Memo

class SearchForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Memo.objects.all(),  # モデルの選択肢
        empty_label="全てのカテゴリ",  # 空の選択肢
        required=False
    )