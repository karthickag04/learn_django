from django.contrib import admin
from django.utils.html import format_html
from students.models import StudentProfile, AssignmentSubmission

# Register your models here.


@admin.register(AssignmentSubmission)
class AssignmentSubmissionAdmin(admin.ModelAdmin):
    list_display = ['student', 'lecture', 'submitted_at', 'video_download', 'audio_download']
    list_filter = ['submitted_at', 'lecture__teacher', 'lecture']
    search_fields = ['student__username', 'lecture__title', 'student__first_name', 'student__last_name']
    readonly_fields = ['submitted_at']
    
    def video_download(self, obj):
        if obj.video_answer:
            return format_html(
                '<a href="{}" download class="btn btn-sm btn-primary">Download Video</a>',
                obj.video_answer.url
            )
        return "No video"
    video_download.short_description = "Video Answer"
    
    def audio_download(self, obj):
        if obj.audio_answer:
            return format_html(
                '<a href="{}" download class="btn btn-sm btn-success">Download Audio</a>',
                obj.audio_answer.url
            )
        return "No audio"
    audio_download.short_description = "Audio Answer"


admin.site.register(StudentProfile)