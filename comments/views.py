from django.shortcuts import render, redirect
from comments.forms import CommentForm
from comments.models import Comments


def reviews_view(request):
    reviews = Comments.objects.filter(status=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            reviews = form.save(commit=False)
            reviews.user_id = request.user
            reviews.save()

            return redirect('reviews:reviews_list')
    else:
        form = CommentForm()

    return render(request, 'comments/reviews_list.html', {'form': form, 'reviews': reviews})
