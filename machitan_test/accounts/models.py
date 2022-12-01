from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager,PermissionsMixin
from django.utils import timezone


class UserManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        
        #username認証をしないため、フィールドから削除している
        email = self.normalize_email(email)
        user = self.model( email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    # def with_perm(
    #     self, perm, is_active=True, include_superusers=True, backend=None, obj=None
    # ):
    #     if backend is None:
    #         backends = auth._get_backends(return_tuples=True)
    #         if len(backends) == 1:
    #             backend, _ = backends[0]
    #         else:
    #             raise ValueError(
    #                 "You have multiple authentication backends configured and "
    #                 "therefore must provide the `backend` argument."
    #             )
    #     elif not isinstance(backend, str):
    #         raise TypeError(
    #             "backend must be a dotted import path string (got %r)." % backend
    #         )
    #     else:
    #         backend = auth.load_backend(backend)
    #     if hasattr(backend, "with_perm"):
    #         return backend.with_perm(
    #             perm,
    #             is_active=is_active,
    #             include_superusers=include_superusers,
    #             obj=obj,
    #         )
    #     return self.none()

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('メールアドレス',unique=True)
    first_name = models.CharField('姓', max_length=30)
    last_name = models.CharField('名', max_length=30)
    department = models.CharField('所属',max_length=30,blank=True)
    creaetd = models.DateField('入会日',default=timezone.now)
    
    is_staff = models.BooleanField(
        ('staff status'),
        default= False,
        help_text=('Designates whether the user can log into this admin site.'),
    )

    is_active = models.BooleanField(
        ("active"),
        default=True,
        help_text=(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    
    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ("user")
        verbose_name_plural = ("users")
        
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
