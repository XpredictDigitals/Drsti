from django.contrib.auth.decorators import login_required

def user_context(request):
    if request.user.is_authenticated:
        return {"logged_in_user": request.user.get_full_name() or request.user.username}
    return {"logged_in_user": None}
