from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MemberInfoForm

@login_required
def add_member_info(request):
    if request.method == 'POST':
        form = MemberInfoForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MemberInfoForm(user=request.user)
    return render(request, 'member/add_member_info.html', {'form': form})
