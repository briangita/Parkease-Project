from django.contrib.auth.decorators import user_passes_test


def admin_required(view_func):
    return user_passes_test(
        lambda u: u.is_superuser or u.groups.filter(name='admin').exists()
    )(view_func)


def parking_attendant_required(view_func):
    return user_passes_test(
        lambda u: u.groups.filter(name='parking_attendant').exists()
    )(view_func)


def section_manager_required(view_func):
    return user_passes_test(
        lambda u: u.groups.filter(name='section_manager').exists()
    )(view_func)