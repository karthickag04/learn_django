
from django.contrib import admin

# Customize admin site
admin.site.login_template = 'ecart/login.html'
admin.site.site_header = 'ECart Administration'  # Changes header text
admin.site.site_title = 'ECart Admin Portal'     # Changes browser tab title
admin.site.index_title = 'ECart Admin Dashboard'  # Changes index page title
