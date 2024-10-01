from django.shortcuts import render, redirect
from .models import Tranning
from datetime import datetime, timedelta

def tranning(request):
    trannings = Tranning.objects.all()
    return render(request, 'community/tranning/tranning.html', {'trannings': trannings})

def add_tranning(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course_code = request.POST.get('course_code')
        course_duration = request.POST.get('course_duration')
        schedule = request.POST.get('schedule')
        tuition_fee = request.POST.get('tuition_fee')
        target_audience = request.POST.get('target_audience')
        link = request.POST.get('link')
        image_tranning = request.FILES.get('image_tranning')  # Lấy ảnh khóa học
        full_name = request.POST.get('full_name')
        major = request.POST.get('major')
        image_lecturer = request.FILES.get('image_lecturer')  # Lấy ảnh giảng viên
        course_description = request.POST.get('course_description')
        detailed_description = request.POST.get('detailed_description')

        # Kiểm tra lỗi
        error_messages = {
            'course_name': '',
            'course_code': '',
            'course_duration': '',
            'schedule': '',
            'tuition_fee': '',
            'target_audience': '',
            'link': '',
            'image_tranning': '',
            'full_name': '',
            'major': '',
            'image_lecturer': '',
            'course_description': '',
            'detailed_description': '',
        }

        # Kiểm tra dữ liệu
        if not course_name:
            error_messages['course_name'] = "Tên khóa học không được để trống!"
        
        if not course_code:
            error_messages['course_code'] = "Mã khóa học không được để trống!"
        elif Tranning.objects.filter(course_code=course_code).exists():
            error_messages['course_code'] = "Mã khóa học đã tồn tại!"
           
        if not course_duration:
            error_messages['course_duration'] = "Thời lượng khóa học không được để trống!"
        
        if not schedule:
            error_messages['schedule'] = "Lịch học không được để trống!"
        else:
            # Chuyển schedule từ chuỗi sang datetime
            try:
                schedule_date = datetime.strptime(schedule, '%Y-%m-%d').date()
                today = datetime.today().date()
                min_date = today + timedelta(days=2)  # Ngày tối thiểu là hôm nay + 2 ngày
                if schedule_date < min_date:
                    error_messages['schedule'] = "Lịch học phải cách tối thiểu 2 ngày so với hôm nay!"
            except ValueError:
                error_messages['schedule'] = "Ngày học không hợp lệ!"

        if not tuition_fee:
            error_messages['tuition_fee'] = "Học phí không được để trống!"
        
        if not target_audience:
            error_messages['target_audience'] = "Đối tượng học không được để trống!"
        
        if not link:
            error_messages['link'] = "Link Zalo không được để trống!"
        
        if not image_tranning:
            error_messages['image_tranning'] = "Bạn phải tải lên ảnh khóa học!"
        
        if not full_name:
            error_messages['full_name'] = "Tên giảng viên không được để trống!"
        
        if not major:
            error_messages['major'] = "Chuyên ngành không được để trống!"
        
        if not image_lecturer:
            error_messages['image_lecturer'] = "Bạn phải tải lên ảnh giảng viên!"
        
        if not course_description:
            error_messages['course_description'] = "Mô tả giảng viên không được để trống!"
        
        if not detailed_description:
            error_messages['detailed_description'] = "Mô tả chi tiết khóa học không được để trống!"

        # Trả lại form nếu có lỗi
        if any(error_messages.values()):
            return render(request, 'community/tranning/add_tranning.html', {
                'input_data': request.POST,
                'error_messages': error_messages
            })

        # Tạo và lưu khóa học mới
        new_tranning = Tranning(
            course_name=course_name,
            course_code=course_code,
            course_duration=course_duration,
            schedule=schedule,
            tuition_fee=tuition_fee,
            target_audience=target_audience,
            link=link,
            image_tranning=image_tranning,
            full_name=full_name,
            major=major,
            image_lecturer=image_lecturer,
            course_description=course_description,
            detailed_description=detailed_description,
        )
        new_tranning.save()

        return redirect('tranning')  # Chuyển đến trang quản lý khóa học

    return render(request, 'community/tranning/add_tranning.html')

def tranning_detail(request, tranning_id):
    tranning = Tranning.objects.get(id=tranning_id)
    return render(request, 'community/tranning/tranning_detail.html', {'tranning': tranning})