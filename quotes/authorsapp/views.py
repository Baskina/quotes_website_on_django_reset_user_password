from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from authorsapp.models import Author
from authorsapp.forms import AuthorForm


def main(request):
    return render(request, 'authorsapp/index.html')


@login_required()
def addAuthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quotesapp:main')
        else:
            return render(request, 'authorsapp/addAuthor.html', {'form': form})

    return render(request, 'authorsapp/addAuthor.html', {'form': AuthorForm()})


def getAuthor(request, author_id):
    return render(request, 'authorsapp/index.html', context={'author': Author.objects.get(id=author_id)})
