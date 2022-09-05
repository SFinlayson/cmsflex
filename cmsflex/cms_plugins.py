from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from .models import Flexbox, FlexItem
from .forms import FlexForm


@plugin_pool.register_plugin
class FlexboxPlugin(CMSPluginBase):
    model = Flexbox
    module = "Page"
    name = "Flexbox"
    render_template = "cms/plugins/flexbox.html"
    allow_children = True
    child_classes = ["FlexItemPlugin"]
    form = FlexForm

    def save_model(self, request, obj, form, change):
        response = super().save_model(
            request, obj, form, change
        )
        for _ in range(int(form.cleaned_data['create'])):
            col = FlexItem(
                parent=obj,
                placeholder=obj.placeholder,
                language=obj.language,
                position=CMSPlugin.objects.filter(parent=obj).count(),
                class_name=f"{obj.class_name}_item",
                plugin_type=FlexItemPlugin.__name__
            )
            col.save()
        return response


@plugin_pool.register_plugin
class FlexItemPlugin(CMSPluginBase):
    model = FlexItem
    module = "Flexbox"
    name = "FlexItem"
    render_template = "cms/plugins/flexboxitem.html"
    parent_classes = ["FlexboxPlugin"]
    allow_children = True
