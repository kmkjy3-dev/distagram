from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Photo, Comment
from .forms import CommentForm


def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos': photos})

@login_required
def photo_detail(request, pk):
    # 1. 사진 가져오기
    photo = get_object_or_404(Photo, pk=pk)
    
    # 2. 댓글 저장 로직 (POST 요청 시)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.photo = photo
            comment.author = request.user
            comment.save()
            return redirect('photo:photo_detail', pk=photo.pk)
    else:
        # 3. 페이지를 그냥 볼 때 (GET 요청 시) 빈 폼 생성
        form = CommentForm()
        
    # 4. 템플릿에 데이터 전달
    # 기존 detail.html에서 'object' 변수를 쓰고 있으므로 이름을 맞춰줍니다.
    return render(request, 'photo/detail.html', {
        'object': photo, 
        'form': form
    })
@login_required
def comment_like(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user in comment.like_users.all():
        comment.like_users.remove(request.user) # 이미 눌렀으면 취소
    else:
        comment.like_users.add(request.user) # 안 눌렀으면 추가
        comment.dislike_users.remove(request.user) # 싫어요가 눌려있다면 해제
    return redirect('photo:photo_detail', pk=comment.photo.id)
@login_required
def comment_dislike(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user in comment.dislike_users.all():
        comment.dislike_users.remove(request.user)
    else:
        comment.dislike_users.add(request.user)
        comment.like_users.remove(request.user) # 좋아요가 눌려있다면 해제
    return redirect('photo:photo_detail', pk=comment.photo.id)

class Photouploadview(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'
    
    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form': form})
        
class photodeleteview(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'

class photoupdateview(UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'
    