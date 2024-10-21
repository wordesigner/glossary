from django import forms

entry = [
    ('1', 'rejected freight'),
    ('fleet owner', 'fleet owner'),
    ('freight', 'freight'),
    ('cargo', 'rejected freight'),
    ('freight capacity', 'rejected freight'),
    ('spot prices', 'rejected freight'),
    ('electronic logistics marketplace', 'rejected freight'),
    ('load posting', 'rejected freight'),
    ('freight intelligence', 'rejected freight'),
    ('haulage company', 'rejected freight'),
    ('freight exchange', 'rejected freight'),
    ('freight procurement', 'rejected freight'),  
]

class MainForm(forms.Form):
    query = forms.CharField(label=False, max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Freight Quote'}), error_messages={
        'required': 'واژه مورد نظر را وارد کنید'
    })
    
class FeedForm(forms.Form):
    feedbox = forms.CharField(label='معنی پیشنهادی‌تان را بنویسید', max_length=100, widget=forms.Textarea)

class WordSel(forms.Form):
    wordchoice = forms.CharField(label='واژه انتخابی', widget=forms.Select(choices=entry))
    comment = forms.CharField(label='نظر شما', widget=forms.Textarea, max_length=100)

    #def __init__(self, *args, **kwargs):
    #    super(MainForm, self).__init__(*args, **kwargs)
    #    self.fields['query'].widget.attrs.update({'class': ''})


