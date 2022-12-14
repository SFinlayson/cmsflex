from django.db import models
from cms.models import CMSPlugin
from djangocms_attributes_field.fields import AttributesField


class Flexbox(CMSPlugin):
    """
    Flexbox with Flexitems
    """

    label = models.CharField(max_length=80)
    responsive = models.BooleanField(default=True)
    background_colour = models.CharField(max_length=30, blank=True, null=True)
    colour = models.CharField(max_length=30, blank=True, null=True)
    direction = models.CharField(max_length=80, blank=True, null=True)
    wrap = models.CharField(max_length=80, blank=True, null=True)
    justify_content = models.CharField(max_length=80, blank=True, null=True)
    align_items = models.CharField(max_length=80, blank=True, null=True)
    align_content = models.CharField(max_length=80, blank=True, null=True)
    gap = models.CharField(max_length=50, blank=True, null=True)
    attributes = AttributesField(
        verbose_name='Attributes',
        blank=True,
        excluded_keys=['href', 'target'],
    )
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.label


class FlexItem(CMSPlugin):
    """
    Flexbox item Plugin
    """
    label = models.CharField(
        max_length=80, null=True, blank=True
    )
    flex = models.CharField(max_length=50, null=True, blank=True)
    align_self = models.CharField(max_length=50, null=True, blank=True)
    attributes = AttributesField(
        verbose_name='Attributes',
        blank=True,
        excluded_keys=['href', 'target'],
    )
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.label
