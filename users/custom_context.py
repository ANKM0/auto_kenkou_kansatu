from django.http import HttpResponse
from .models import UserInfo


def is_exsist_data_in_userinfo(request: HttpResponse) -> bool:
    len_match_data = UserInfo.objects.filter(username=request.user).count()
    if len_match_data > 0:
        is_exsist_data_in_userinfo = True
    else:
        is_exsist_data_in_userinfo = False
    return {"is_exsist_data_in_userinfo": is_exsist_data_in_userinfo}
