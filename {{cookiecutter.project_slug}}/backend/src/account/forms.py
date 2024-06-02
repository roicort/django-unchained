from unfold.forms import AdminPasswordChangeForm as BaseAdminPasswordChangeForm
from unfold.forms import UserChangeForm as BaseUserChangeForm
from unfold.forms import UserCreationForm as BaseUserCreationForm

from .models import User


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')  # Añade 'email' aquí

class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = User
        fields = "__all__"

class AdminPasswordChangeForm(BaseAdminPasswordChangeForm):
    class Meta:
        model = User
        fields = "__all__"