from copy import deepcopy

from django.contrib import admin

from mezzanine.forms.admin import FormAdmin
from mezzanine.forms.models import Form
from mezzanine.galleries.admin import GalleryAdmin
from mezzanine.galleries.models import Gallery
from mezzanine.pages.admin import PageAdmin
from mezzanine.pages.models import RichTextPage
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost
#from .models import HomePage


# add the background image to page subclasses in the admin
page_fieldsets = deepcopy(PageAdmin.fieldsets)
page_fieldsets[0][1]["fields"].insert(1,"background")
page_fieldsets[0][1]["fields"].insert(1,"subheading")
page_fieldsets[0][1]["fields"].insert(1,"heading")
PageAdmin.fieldsets = page_fieldsets
GalleryAdmin.fieldsets = page_fieldsets

form_fieldsets = deepcopy(FormAdmin.fieldsets)
form_fieldsets[0][1]["fields"].insert(1,"background")
form_fieldsets[0][1]["fields"].insert(1,"subheading")
form_fieldsets[0][1]["fields"].insert(1,"heading")
FormAdmin.fieldsets = form_fieldsets

admin.site.unregister(Form)
admin.site.register(Form, FormAdmin)
admin.site.unregister(Gallery)
admin.site.register(Gallery, GalleryAdmin)
admin.site.unregister(RichTextPage)
admin.site.register(RichTextPage, PageAdmin)

#admin.site.register(HomePage, PageAdmin)

# blog
blog_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
blog_fieldsets[0][1]["fields"].insert(1, "subtitle")

class MyBlogPostAdmin(BlogPostAdmin):
    fieldsets = blog_fieldsets

admin.site.unregister(BlogPost)
admin.site.register(BlogPost, MyBlogPostAdmin)