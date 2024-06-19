from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.firstname = data.get("firstname")
        user.lastname = data.get("lastname")
        user.email = data.get("email")
        user.phone = data.get("phone")
        user.department = data.get("department")
        user.save()
        return user
