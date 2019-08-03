from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from exercises.models import Student


def create_permission():
    ct = ContentType.objects.get_for_model(Student)
    permission = Permission.objects.update(
        codename='add_student_notice',
        name='Can add notice for students',
        content_type=ct
    )


if __name__ == "__main__":
    create_permission()
