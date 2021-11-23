from django.db import models
from django.utils.translation import ugettext_lazy as _

class Client(models.Model):
    user = models.OneToOneField("registration.CustomUser", verbose_name=_("User"), on_delete=models.CASCADE, null=True, blank=True)
    profile_image = models.ForeignKey("file.File", related_name="profile_image", null=True, blank=True, verbose_name=_("Profile Image"), on_delete=models.CASCADE)
    document_1 = models.ForeignKey("file.File", related_name="client_document_1", null=True, blank=True,verbose_name=_("File 1"), on_delete=models.CASCADE)
    document_2 = models.ForeignKey("file.File", related_name="client_document_2", null=True, blank=True, verbose_name=_("File 2"), on_delete=models.CASCADE)
    document_3 = models.ForeignKey("file.File", related_name="client_document_3", null=True, blank=True, verbose_name=_("File 3"), on_delete=models.CASCADE)
    class Meta:
        verbose_name = _("client")
        verbose_name_plural = _("clients")

