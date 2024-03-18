from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """사용자 모델 관리자로, 사용자 생성 및 관리를 처리합니다."""

    def create_user(self, email, password=None, **extra_fields):
        """이메일, 비밀번호 및 추가 필드를 사용하여 새로운 사용자를 생성하고 반환합니다.

        이메일이 제공되지 않을 경우 ValueError를 발생시킵니다.
        """
        if not email:
            raise ValueError("사용자는 이메일 주소를 가져야 합니다")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """시스템 내 개별 사용자를 나타내는 사용자 모델입니다."""

    email = models.EmailField(max_length=255, unique=True)
    nickname = models.CharField(max_length=255)
    is_business = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        """사용자의 문자열 표현을 반환합니다."""
        return f"email: {self.email}, nickname: {self.nickname}"
