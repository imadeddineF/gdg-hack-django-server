from django.contrib.auth.models import BaseUserManager, GroupManager
from django.db import models
import re

class ProfileManager(BaseUserManager):

    def check_data(self, **extra_fields):
        from . import models
        for field in models.Profile.REQUIRED_FIELDS:
            if field not in extra_fields:
                raise Exception(f'FIELD {field} IS NOT SATISFIED')
            
    def validate_password(self, password):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$"
        if not re.match(pattern, password):
            raise Exception(f"Password error: \n# At least 8 characters"+
                            "Contains at least one uppercase letter\n"+
                            "Contains at least one lowercase letter\n"+
                            "Contains at least one digit\n"+
                            "Contains at least one special character (e.g., !@#$%^&*)") 

    def create_user(self, **extra_fields):
        self.check_data(**extra_fields)
        email = self.normalize_email(extra_fields['email'])
        password = extra_fields['password']
        # self.validate_password(password)
        extra_fields.pop('email')
        extra_fields.pop('password')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(**extra_fields)
