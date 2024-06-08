from django.contrib.auth.forms import UserCreationForm

from accountapp.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('userid', 'username', 'email', 'name', 'birthdate', 'gender', 'is_korean')

    def init(self, args, **kwargs):
        super().init(args, **kwargs)
        self.fields['birthdate'].widget.attrs['class'] = 'datepicker'