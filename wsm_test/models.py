from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.fields import StreamField
from wagtail.models import Page

from wagtail_svgmap.blocks import ImageMapBlock


class TestPage(Page):
    template = 'page.html'

    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('imagemap', ImageMapBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
