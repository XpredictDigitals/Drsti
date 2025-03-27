from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Complaint

@login_required
def add_complaint(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        category = request.POST["category"]
        priority = request.POST["priority"]
        attachment = request.FILES.get("attachment", None)

        Complaint.objects.create(
            user=request.user,
            title=title,
            description=description,
            category=category,
            priority=priority,
            attachment=attachment,
        )
        return redirect("view_complaints")

    return render(request, "add_complaint.html")


def view_complaints(request):
    complaints = Complaint.objects.all().order_by('-created_at')  # Fetch all complaints, newest first
    return render(request, 'view_complaints.html', {'complaints': complaints})