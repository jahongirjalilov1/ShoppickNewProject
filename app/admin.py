from django.contrib import admin
from django.contrib.admin import ModelAdmin, AdminSite
from django.forms import ModelForm
from django.utils.html import format_html

# Register your models here.
from app.models import Category, Product, Women, Men

admin.site.site_header = "My site"
admin.site.site_title = "Admin"
admin.site.index_title = "My site"

#-------------------------------------

class ProductAdminSite(AdminSite):
    site_header = "UMSRA Events Admin"
    site_title = "UMSRA Events Admin Portal"
    index_title = "Welcome to UMSRA Researcher Events Portal"
product_admin_site = ProductAdminSite(name='product_admin')
product_admin_site.register(Product)

#-------------------------------------

class WomenAdminSite(AdminSite):
    site_header = "UMSRA Events Admin"
    site_title = "UMSRA Events Admin Portal"
    index_title = "Welcome to UMSRA Researcher Events Portal"
women_admin_site = WomenAdminSite(name='women_admin')
women_admin_site.register(Women)

#-------------------------------------

class MenAdminSite(AdminSite):
    site_header = "UMSRA Events Admin"
    site_title = "UMSRA Events Admin Portal"
    index_title = "Welcome to UMSRA Researcher Events Portal"
Men_admin_site = MenAdminSite(name='women_admin')
Men_admin_site.register(Men)

#-----------------------------------

class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['image'].help_text = 'Product image'
        self.fields['title'].help_text = 'Product title'
        self.fields['text'].help_text = 'Product description'
        self.fields['price'].help_text = 'Product price'
        self.fields['category'].help_text = 'Product category'

    class Meta:
        model = Product
        exclude = ()

#-----------------------------------

class MenForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MenForm, self).__init__(*args, **kwargs)
        self.fields['image'].help_text = 'Men image'
        self.fields['title'].help_text = 'Men title'
        self.fields['text'].help_text = 'Men description'
        self.fields['price'].help_text = 'Men price'
        self.fields['category'].help_text = 'Men category'

    class Meta:
        model = Men
        exclude = ()

#-----------------------------------

class WomenForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(WomenForm, self).__init__(*args, **kwargs)
        self.fields['image'].help_text = 'Women image'
        self.fields['title'].help_text = 'Women title'
        self.fields['text'].help_text = 'Women description'
        self.fields['price'].help_text = 'Women price'
        self.fields['category'].help_text = 'Women category'

    class Meta:
        model = Women
        exclude = ()

#-----------------------------------

MAX_OBJECTS = 5
@admin.register(Product)
class ProductAdmin(ModelAdmin):
    form = ProductForm
    list_display = ['image_tag', 'title', 'price', 'text', 'color']
    list_filter = ('title', 'price', 'text')
    # list_per_page = 5

    def image_tag(self, obj):
        return format_html('<img src="{}" width= "70"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return True
        return super().has_add_permission(request)

#-----------------------------------
@admin.register(Women)
class WomenAdmin(ModelAdmin):
    form = WomenForm
    list_display = ['image_tag', 'title', 'price', 'text', 'color']
    list_filter = ('title', 'price', 'text')
    # list_per_page = 5

    def image_tag(self, obj):
        return format_html('<img src="{}" width= "70"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return True
        return super().has_add_permission(request)

#-----------------------------------

@admin.register(Men)
class MenAdmin(ModelAdmin):
    form = MenForm
    list_display = ['image_tag', 'title', 'price', 'text', 'color']
    list_filter = ('title', 'price', 'text')
    # list_per_page = 5

    def image_tag(self, obj):
        return format_html('<img src="{}" width= "70"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return True
        return super().has_add_permission(request)

#--------------------------------

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)



