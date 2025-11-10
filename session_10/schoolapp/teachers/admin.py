from django.contrib import admin
from django.utils.html import format_html
from teachers.models import Feedback, Lecture

# Register your models here.


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ['title', 'teacher', 'uploaded_at', 'video_download', 'audio_download']
    list_filter = ['uploaded_at', 'teacher']
    search_fields = ['title', 'description', 'teacher__username']
    readonly_fields = ['uploaded_at']
    
    def video_download(self, obj):
        if obj.video:
            return format_html(
                '<a href="{}" download class="btn btn-sm btn-primary">Download Video</a>',
                obj.video.url
            )
        return "No video"
    video_download.short_description = "Video"
    
    def audio_download(self, obj):
        if obj.audio:
            return format_html(
                '<a href="{}" download class="btn btn-sm btn-success">Download Audio</a>',
                obj.audio.url
            )
        return "No audio"
    audio_download.short_description = "Audio"


admin.site.register(Feedback)  # Register your Feedback model here