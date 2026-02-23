import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogsite.settings') # আপনার প্রোজেক্টের নাম ঠিক আছে কি না দেখে নিন
django.setup()

User = get_user_model()
username = 'admin' # আপনার ইউজারনেম
email = 'admin@example.com' # আপনার ইমেইল
password = 'shakil_pass_123' # আপনার কঠিন একটি পাসওয়ার্ড

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f'Superuser "{username}" created successfully!')
else:
    print(f'Superuser "{username}" already exists.')