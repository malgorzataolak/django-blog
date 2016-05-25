from django.contrib import admin
from .models import Post
from .models import ArtistInfo

admin.site.register(Post)
admin.site.register(ArtistInfo)