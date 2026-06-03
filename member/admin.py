

# Register your models here.
from django.contrib import admin
from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'first_name',
        'last_name',
        'phone',
        'email',
        'gender',
        'blood_group',
        'joined_at',
        'is_active'
    ]

    search_fields = [
        'first_name',
        'middle_name',
        'last_name',
        'email',
        'phone'
    ]

    list_filter = [
        'gender',
        'blood_group',
        'is_active',
        'joined_at'
    ]


    ordering = [
        '-joined_at'
    ]

    readonly_fields = [
        'created_at',
        'updated_at'
    ]

    fieldsets = (

        ('Personal Information', {
            'fields': (
                'first_name',
                'middle_name',
                'last_name',
                'dob',
                'gender',
            )
        }),

        ('Contact Information', {
            'fields': (
                'phone',
                'email',
                'address',
                'emergency_contact_phone'
            )
        }),

        ('Health Information', {
            'fields': (
                'height_cm',
                'weight_kg',
                'medical_conditions',
                'blood_group'
            )
        }),

        ('Membership Details', {
            'fields': (
                'joined_at',
                'is_active'
            )
        }),

        ('Time Stamp', {
            'fields': (
                'created_at',
                'updated_at'
            )
        }),
    )