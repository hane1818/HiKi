from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from diary.models import Diary

User = get_user_model()

def image_upload_to(instance, filename):
    return 'image/{date}-{filename}'.format(
        date=str(instance.pub_date.date()),
        filename=filename,
        )

class Image(models.Model):
    """User upload images.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=0,
    )
    diary = models.ForeignKey(
        Diary,
        on_delete=models.CASCADE,
        default=0,
        null=True, blank=True,
    )
    img = models.ImageField(
        upload_to=image_upload_to,
    )
    title = models.CharField(
        max_length=20, null=True, blank=True,
    )
    description = models.CharField(
        max_length=80, null=True, blank=True,
    )
    pub_date = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )

    def __str__(self):
        return str(self.img)

    def delete(self, *args, **kwargs):
        super(Image, self).delete(*args, **kwargs)
        storage, path = self.img.storage, self.img.path
        storage.delete(path)
