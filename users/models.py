from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, UserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.auth import get_user_model


class User(AbstractBaseUser, PermissionsMixin):
    """ユーザーモデル"""

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email = models.EmailField("メールアドレス", blank=True)
    sns_icon_url = models.URLField("アイコン(SNS連携)", blank=True)
    is_staff = models.BooleanField("is_staff", default=False)
    is_active = models.BooleanField("is_active", default=True)
    date_joined = models.DateTimeField("date_joined", default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    DEFAULT_ICON_PATH = "images/default_icon.png"


class MyUserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, email, password, **extra_fields)


class MyUser(AbstractBaseUser):
    username = models.CharField(
        verbose_name='ユーザー名',
        max_length=255,
        unique=True,
    )
    email = models.EmailField("メールアドレス", blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField("is_staff", default=False)
    is_superuser = models.BooleanField("is_staff", default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def icon_url(self):
        # ユーザーのアイコン画像URLを返す
        # 1. SNS認証時にプロフィール画像を取得できた場合: sns_icon_url
        # 2. SNS認証時にプロフィール画像を取得できなかった場合: デフォルト画像

        if self.sns_icon_url:
            return self.sns_icon_url
        return staticfiles_storage.url("images/default_icon.png")


class Member(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    IS_RUN_CODE_CHOICES = (
        (1, '実行する'),
        (0, '停止する')
    )

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    user_info_class_number = models.PositiveSmallIntegerField(verbose_name="クラス番号")
    user_info_student_number = models.PositiveSmallIntegerField(verbose_name="出席番号")
    user_info_student_name = models.CharField(max_length=50, verbose_name="名前")
    user_info_body_temperature = models.CharField(max_length=10, verbose_name="体温")
    is_run_code = models.IntegerField(choices=IS_RUN_CODE_CHOICES, default=True, verbose_name="実行するか")
    user_info_created_at = models.DateTimeField(default=timezone.now)
    user_info_updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user_info_student_name

    class Meta:
        verbose_name_plural = 'ユーザー情報'
