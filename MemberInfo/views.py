from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MemberInfoForm
from .models import MemberInfo

@login_required
def addInfo(request):
    if request.method == 'POST':
        form = MemberInfoForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('MemberInfo:stats')
    else:
        form = MemberInfoForm(user=request.user)
    return render(request, 'member/addInfo.html', {'form': form})

@login_required
def stats(request):
    member = MemberInfo.objects.get(member=request.user)
    bmr = member.calculate_bmr()
    tdee = member.calculate_tdee()
    bmi = member.calculate_bmi()
    whatShouldIDo = member.whatShouldIDo()
    context = {
        'member': member,
        'bmr': bmr,
        'tdee': tdee,
        'bmi': bmi,
        'whatShouldIDo': whatShouldIDo,
    }
    return render(request, 'member/stats.html', context)