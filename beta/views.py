from django.shortcuts import render
from .models import MainData, FeedData, BData
from .forms import MainForm, FeedForm, WordSel
from django.views import View
from django.http import HttpResponseRedirect
#from django.http import HttpResponseRedirect, http

# Create your views here.

class Search(View):
    def get(self, req):
        form = MainForm()
        return render(req, 'beta/index.html', {
            'form': form
        })

    def post(self, req):
        global form
        form = MainForm(req.POST, req.FILES)
        if form.is_valid():
            global word
            word = form.cleaned_data['query'].strip().lower()
            #word.lower()
            print(word)
            spe_words = MainData.objects.get(word=word)
            definition = spe_words.definition
            #return HttpRequest()
        return render(req, 'beta/index.html', {
            'form': form,
            'def': definition,
            'word': word
        })
    

class Feedback(View):
    def get(self, req):
        form = FeedForm()
        return render(req, 'beta/feedback.html', {
            'feedform': form
        })
    
    def post(self, req):
        global form
        form = FeedForm(req.POST)
        if form.is_valid():
            data = FeedData(feedstored=form.cleaned_data['feedbox'], related_word=word)
            data.save()
            return HttpResponseRedirect('/success')
        return render(req, 'beta/feedback.html', {
            'feedform': form
        })

def success(req):
    return render(req, 'beta/success.html')
            

def xreport(req):
    reports = FeedData.objects.all()
    return render(req, 'beta/xreport.html', {
        'reports': reports,
    })    

def browse(req):
    entries = MainData.objects.all().order_by('word')
    return render(req, 'beta/browse.html', {
        'entries': entries,
    })


class Comment(View):
    def get(self, req):
        form = WordSel()
        return render(req, 'beta/comment.html', {
            'form': form,
        })
    
    def post(self, req):
        global form
        form = WordSel(req.POST)
        if form.is_valid():
            global choice
            choice = form.cleaned_data['wordchoice']
            global com
            com = form.cleaned_data['comment']
            data = BData(choice=form.cleaned_data['wordchoice'], comment=form.cleaned_data['comment'])
            data.save()
            return HttpResponseRedirect('/success')
        return render(req, 'beta/comment.html', {
            'form': form,
            'choice': choice,
            'com': com
        })

def breport(req):
    breports = BData.objects.all()
    #full_report = f'{choice} ||| {com}'
    return render(req, 'beta/breport.html', {
        'breports': breports 
    })    



