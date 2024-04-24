from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MemberInfoForm
from .models import MemberInfo

@login_required
def add_info(request):
    if request.method == 'POST':
        form = MemberInfoForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MemberInfoForm(user=request.user)
    return render(request, 'member/add_info.html', {'form': form})

@login_required
def stats(request):
    member = MemberInfo.objects.get(memberid=request.user)
    bmr = member.calculate_bmr()
    tdee = member.calculate_tdee()
    bmi = member.calculate_bmi()
    context = {
        'member': member,
        'bmr': bmr,
        'tdee': tdee,
        'bmi': bmi,
    }
    return render(request, 'member/stats.html', context)