from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CommunityModels
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'community/home.html')

def register(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phoneNumber')
        object_type = request.POST.get('object')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')

        error_messages = {
            'firstName': '',
            'lastName': '',
            'email': '',
            'phoneNumber': '',
            'password': '',
            'confirmPassword': ''
        }

        if not firstName:
            error_messages['firstName'] = "Họ không được để trống."
        if not lastName:
            error_messages['lastName'] = "Tên không được để trống."
        if not email:
            error_messages['email'] = "Email không được để trống."
        else:
            if CommunityModels.objects.filter(email=email).exists():
                error_messages['email'] = "Email đã tồn tại!"
        if not phoneNumber:
            error_messages['phoneNumber'] = "Số điện thoại không được để trống."
        else:
            if CommunityModels.objects.filter(phone_number=phoneNumber).exists():
                error_messages['phoneNumber'] = "Số điện thoại đã tồn tại!"
        if not password:
            error_messages['password'] = "Mật khẩu không được để trống."
        else:
            if len(password) < 8 or len(password) > 16:
                if len(password) < 8:
                    error_messages['password'] = "Mật khẩu tối thiểu 8 ký tự."
                elif len(password) > 16:
                    error_messages['password'] = "Mật khẩu tối đa 16 ký tự."
            if password != confirmPassword:
                error_messages['confirmPassword'] = "Mật khẩu không khớp!"

        if any(error_messages.values()):
            return render(request, 'community/register.html', {
                'input_data': request.POST,
                'error_messages': error_messages
            })

        # Lưu thông tin vào model CommunityModels
        new_community = CommunityModels(
            first_name=firstName,
            last_name=lastName,
            email=email,
            phone_number=phoneNumber,
            object=object_type,
        )
        new_community.save()

        new_user = User.objects.create_user(
            username=email,
            password=password
        )
        new_user.first_name = firstName
        new_user.last_name = lastName
        new_user.save()

        messages.success(request, "Đăng ký thành công.")
        return redirect('login')

    return render(request, 'community/register.html')

def login_views(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')  # Chuyển hướng đến trang chính
        else:
            messages.error(request, "Đăng nhập không thành công. Vui lòng kiểm tra email và mật khẩu.")
            return render(request, 'community/login.html', {'email': email})

    return render(request, 'community/login.html')

def signout(request):
    logout(request)
    return redirect('/')

def homepage(request):
    return render(request, 'community/homepage.html')

def functions_duties(request):
    return render(request, 'community/introduction/functions_duties.html')

def institute_introduction(request):
    return render(request, 'community/introduction/institute_introduction.html')

def institute_leadership(request):
    return render(request, 'community/introduction/institute_leadership.html')

def organizational_structure(request):
    return render(request, 'community/introduction/organizational_structure.html')

def staff_organization(request):
    return render(request, 'community/introduction/structure/staff_organization.html')

def administrative(request):
    return render(request, 'community/introduction/structure/administrative.html')

def finance_accounting(request):
    return render(request, 'community/introduction/structure/finance_accounting.html')

def scientific_management(request):
    return render(request, 'community/introduction/structure/scientific_management.html')

def medical_equipment(request):
    return render(request, 'community/introduction/structure/medical_equipment.html')

def quality_assessment(request):
    return render(request, 'community/introduction/structure/quality_assessment.html')

def manufacturing_warranty(request):
    return render(request, 'community/introduction/structure/manufacturing_warranty.html')