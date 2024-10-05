import threading
import time
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver 
from django.db import transaction

# Django signals work synchronously 
@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
    print(f"\n\n ------ Question 1 Signal ------")
    print(f"Signal received for {instance.username}")
    time.sleep(2)
    print("Signal function completed \n\n")
    
    
    
# Django signals Using same thread
@receiver(post_save, sender=User)
def user_thread(sender, instance, **kwargs):
    print(f"------ Question 2 Signal ------")
    print(f"Main thread : {threading.current_thread().name} \n\n")
    
    

# Signals run in the same database transaction
@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
    if transaction.get_autocommit():
        print("Signal executed outside of transaction")
    else:
        print(f"------ Question 3 Signal ------")
        print("Signal executed within a transaction \n\n")