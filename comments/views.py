from django.shortcuts import render, redirect
from comments.forms import CommentForm
from comments.models import Comments
from django.contrib import messages


def reviews_view(request):
    reviews = Comments.objects.filter(status=True).order_by('-date')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Отзыв отправлен на модерацию. Он появится позже')
            reviews = form.save(commit=False)
            reviews.user_id = request.user
            reviews.save()

            return redirect('reviews:reviews_list')
    else:
        form = CommentForm()

    return render(request, 'comments/reviews_list.html', {'form': form, 'reviews': reviews})
