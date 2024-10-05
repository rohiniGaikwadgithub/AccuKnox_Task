from django.db import models

from django.contrib.auth.models import User
import threading
from django.db import transaction

def save_user():
    with transaction.atomic():
        user = User.objects.create(username="TestUser")
        
        print(f"------ Question 1 Caller------")
        print("User saved \n\n")
        
        print(f"------ Question 2 Caller ------")
        print(f"Main thread: {threading.current_thread().name} \n\n")
        
        
        print(f"------ Question 3 Caller ------")
        print("User saved inside transaction \n\n")
    