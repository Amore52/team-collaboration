from django.contrib import admin
from .models import Service, Specialist, Salon, WorkingHour, Appointment, Payment, Notification, SalonManager


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('category', 'price', 'duration', 'description')
    search_fields = ('category',)

class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('name', 'biography')
    search_fields = ('name',)

class SalonAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'phone_number')
    search_fields = ('name',)

class WorkingHourAdmin(admin.ModelAdmin):
    list_display = ('specialist', 'days_of_week', 'open_time', 'close_time')
    search_fields = ('specialist__name', 'days_of_week')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'service', 'start_session', 'end_session')
    list_display_links = ('client_name',)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'price_amount', 'payment_method', 'payment_date', 'status')
    search_fields = ('appointment__client_name', 'payment_method')
    list_filter = ('payment_date', 'status')

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'message', 'send_at', 'status')
    search_fields = ('appointment__client_name', 'message')
    list_filter = ('send_at', 'status')

class SalonManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    search_fields = ('name',)


admin.site.register(Service, ServiceAdmin)
admin.site.register(Specialist, SpecialistAdmin)
admin.site.register(Salon, SalonAdmin)
admin.site.register(WorkingHour, WorkingHourAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(SalonManager, SalonManagerAdmin)
