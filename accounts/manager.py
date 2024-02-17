from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _ 
from django.core.exceptions import ValidationError

class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Please enter a valid email email address"))

    def create_user(self, email, password=None, **extra_fields): 
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password) # This hashes the password..
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("is staff must be true for admin user"))
        if extra_fields.get("is_active") is not True:
            raise ValueError(_("is active must be true for admin user"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("is superuser must be true for admin user"))
        
        user = self.create_user(email, password, **extra_fields)
        user.save(using=self._db)
        return user
    

    

