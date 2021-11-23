from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Vendor(models.Model):
    user = models.ForeignKey("registration.CustomUser", null=True, blank=True, verbose_name=_("user"), on_delete=models.CASCADE)
    company_name = models.CharField(_("Company name"), max_length=50)
    contact_name = models.CharField(_("Contact name"), max_length=50)
    address = models.CharField(_("Address"), max_length=150)
    zip_code = models.CharField(_("Zip Code"), max_length=20)
    document_1 = models.ForeignKey("file.File", related_name="vendor_document_1", null=True, blank=True, verbose_name=_("File 1"), on_delete=models.CASCADE)
    document_2 = models.ForeignKey("file.File", related_name="vendor_document_2", null=True, blank=True, verbose_name=_("File 2"), on_delete=models.CASCADE)
    document_3 = models.ForeignKey("file.File", related_name="vendor_document_3", null=True, blank=True, verbose_name=_("File 3"), on_delete=models.CASCADE)
    class Meta:
        verbose_name = _("vendor")
        verbose_name_plural = _("vendors")

    def __str__(self):
        return self.company_name

