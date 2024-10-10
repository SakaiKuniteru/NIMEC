from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from community.models import CommunityModels
from community.forms import CommunityForms
from news.models import News, Content, TextStyle
from news.forms import NewsForm, ContentForm
from tranning.forms import TranningForm
from tranning.models import Tranning
from library.forms import BookForm
from library.models import Book
from django.contrib.auth.models import User

def admin(request):
    return render(request, 'admin_nimec/admin.html')

def user_list(request):
    users = CommunityModels.objects.all()
    return render(request, 'admin_nimec/user/user_list.html', {'users': users})

def add_user(request):
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
            'object_type': '',
            'password': '',
            'confirmPassword': ''
        }

        if not firstName:
            error_messages['firstName'] = "Họ không được để trống!"
        if not lastName:
            error_messages['lastName'] = "Tên không được để trống!"
        if not email:
            error_messages['email'] = "Email không được để trống!"
        else:
            if CommunityModels.objects.filter(email=email).exists():
                error_messages['email'] = "Email đã tồn tại!"
        if not phoneNumber:
            error_messages['phoneNumber'] = "Số điện thoại không được để trống!"
        else:
            if CommunityModels.objects.filter(phone_number=phoneNumber).exists():
                error_messages['phoneNumber'] = "Số điện thoại đã tồn tại!"
        if not password:
            error_messages['password'] = "Mật khẩu không được để trống!"
        else:
            if len(password) < 8 or len(password) > 16:
                if len(password) < 8:
                    error_messages['password'] = "Mật khẩu tối thiểu 8 ký tự!"
                elif len(password) > 16:
                    error_messages['password'] = "Mật khẩu tối đa 16 ký tự!"
            if password != confirmPassword:
                error_messages['confirmPassword'] = "Mật khẩu không khớp!"
        if not object_type:
            error_messages['object_type'] = "Vui lòng chọn!"

        if any(error_messages.values()):
            return render(request, 'admin_nimec/user/add_user.html', {
                'input_data': request.POST,
                'error_messages': error_messages
            })

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

        messages.success(request, "")
        return redirect('user_list')

    return render(request, 'admin_nimec/user/add_user.html')

def edit_user(request, user_id):
    user = get_object_or_404(CommunityModels, id=user_id)
    
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.phone_number = request.POST.get('phone_number')
        user.object = request.POST.get('object')
        user.save()
        
        return redirect('user_list')
    
    return render(request, 'admin_nimec/user/edit_user.html', {'user': user})

def delete_user(request, user_id):
    user = get_object_or_404(CommunityModels, id=user_id)
    user.delete()
    return redirect('user_list')

def course_list(request):
    courses = Tranning.objects.all()
    return render(request, 'admin_nimec/tranning/course_list.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        form = TranningForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm khóa học thành công.')
            return redirect('course_list')
        else:
            # Hiển thị thông báo lỗi nếu form không hợp lệ
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Lỗi tại {field}: {error}")
    else:
        form = TranningForm()
    
    return render(request, 'admin_nimec/tranning/add_course.html', {'form': form})

def edit_course(request, course_id):
    course = get_object_or_404(Tranning, id=course_id)
    
    if request.method == 'POST':
        form = TranningForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = TranningForm(instance=course)
    
    return render(request, 'admin_nimec/tranning/edit_course.html', {'form': form, 'course': course})

def delete_course(request, course_id):
    course = get_object_or_404(Tranning, id=course_id)
    course.delete()
    return redirect('course_list')

def newss_list(request):
    news_list = News.objects.all().order_by('-updated_at')
    return render(request, 'admin_nimec/news/news_list.html', {'news_list': news_list})

def add_news(request):
    if request.method == 'POST':
        news_form = NewsForm(request.POST)
        
        if news_form.is_valid():
            news = news_form.save()
            return redirect('newss_list')
            
    else:
        news_form = NewsForm()

    return render(request, 'admin_nimec/news/add_news.html', {'news_form': news_form})

def edit_news(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if request.method == 'POST':
        news_form = NewsForm(request.POST, instance=news)
        content_form = ContentForm(request.POST)
        
        if news_form.is_valid() and content_form.is_valid():
            news_form.save()
            content = content_form.save(commit=False)
            content.news = news
            content.save()
            
            return redirect('newss_list')
    else:
        news_form = NewsForm(instance=news)
        content_form = ContentForm()

    news_contents = news.contents.all()

    context = {
        'news_form': news_form,
        'content_form': content_form,
        'news_contents': news_contents,
        'news': news
    }
    return render(request, 'admin_nimec/news/edit_news.html', context)

def delete_news(request, news_id):
    news = get_object_or_404(News, id=news_id)
    news.delete()
    return redirect('newss_list')

def book_list(request):
    books = Book.objects.all()
    return render(request, "admin_nimec/library/book_list.html", {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '')
            return redirect('book_list')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Lỗi tại {field}: {error}")
    else:
        form = BookForm()
    return render(request, "admin_nimec/library/add_book.html", {'form' : form})

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'admin_nimec/library/edit_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')