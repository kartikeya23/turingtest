from django.shortcuts import render
from django.utils import timezone
from accounts.models import School
from django.contrib.auth.models import User
from django.core import serializers

# Create your views here.

def dashboard(request):
    return render(request,'dashboard/dashboard.html')

def level(request):
    if request.method == "POST":
        print(request.POST['answer'])
        User = request.user
        if request.POST['answer'] == 'Increase':
            User.school.level = User.school.level + 1
            User.school.time = timezone.now()
            # print(timezone.now())
            User.school.save()
    return render(request,'dashboard/level.html')

def leaderboard(request):
    # all_users = User.objects.filter(is_staff=False)
    # final_list = []
    # # print(all_users[0])
    # for user in all_users:
    #     print(all_users)
    #     if len(final_list) != 0:
    #         print("qewfuwefh")
    #         print(final_list)
    #         for sorted_user in final_list:
    #             if user.school.level > sorted_user.school.level:
    #                 index = final_list.index(sorted_user)
    #                 final_list.insert(index, user)
    #             elif user.school.level == sorted_user.school.level:
    #                 pass
    #     else:
    #         print('aefjwiefji')
    #         final_list.append(all_users[0])
    #
    # print(final_list)



    return render(request, 'dashboard/leaderboard.html')
