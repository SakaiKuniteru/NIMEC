from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_migrate)
def create_admin_user(sender, **kwargs):
    if sender.name == 'admin_nimec':
        if not User.objects.filter(username='ttdt').exists():
            User.objects.create_superuser('ttdt', 'nimec40pm@moh.gov.vn', '!nimec40PM')

        if not User.objects.filter(username='ttdt01').exists():
            User.objects.create_superuser('ttdt01', 'nimec40pm@moh.gov.vn', '@nimec40PM')

        if not User.objects.filter(username='ttdt02').exists():
            User.objects.create_superuser('ttdt02', 'nimec40pm@moh.gov.vn', '@nimec40PM')
