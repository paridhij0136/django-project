from django.shortcuts import render, redirect
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render (request, "index.html")

def register(request):

    if request.method == 'POST':
        # Get all form fields
        name = request.user.username
        email = request.user.email
        admission_number = request.POST.get('admission_number')
        branch = request.POST.get('branch')
        year = request.POST.get('year')
        contact_number = request.POST.get('contact_number')
        component_name = request.POST.get('component_name')
        componentissue_date = request.POST.get('componentissue_date')
        componentdue_date = request.POST.get('componentdue_date')
        faculty_referred = request.POST.get('faculty_referred')

        if not email.endswith("@mes.student.ac.in"):
            return render(request, "furm.html", {
                'error': 'Only MES email IDs are allowed.'
            })
        

        # Save to database
        Student.objects.create(
            name=name,
            email=email,
            admission_number=admission_number,
            branch=branch,
            year=year,
            contact_number=contact_number,
            component_name=component_name,
            componentissue_date=componentissue_date,
            componentdue_date=componentdue_date,
            faculty_referred=faculty_referred
        )

        return render(request, "furm.html", {'success': True})

    return render(request, "furm.html")

def login_page(request):
    return render(request, "login.html")


def signup_page(request):
    return render(request, "signup.html")

def signup_view(request):

    if request.method == "POST":

        print(request.POST)

        username = request.POST["username"]

        email = request.POST["email"]

        password = request.POST["password"]

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        if User.objects.filter(email=email).exists():
         return render(
        request,
        "signup.html",
        {"error": "An account with this email already exists."}
    )
        return redirect("/login.html/")

    return render(request, "signup.html")


    
def login_user(request):
    print(request.user.username)
    print(request.user.email)   

    if request.method == "POST":

        email = request.POST["email"]

        password = request.POST["password"]

        try:
            user_obj = User.objects.get(email=email)

            user = authenticate(
                request,
                username=user_obj.username,
                password=password
            )

            if user is not None:
                login(request, user)
                return redirect("/furm.html/")

            return render(
                request,
                "login.html",
                {"error": "Incorrect password."}
            )

        except User.DoesNotExist:

            return render(
                request,
                "login.html",
                {"error": "No account found with this email, kindly Register."}
            )

    return render(request, "login.html")