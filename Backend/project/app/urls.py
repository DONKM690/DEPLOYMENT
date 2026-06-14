from django.urls import path
from .views import (
    contact_create,
    contact_list,
    contact_detail,
    contact_update,
    contact_delete,
)

urlpatterns = [
    # CREATE
    path('contact/', contact_create),

    # READ ALL
    path('contacts/', contact_list),

    # READ ONE
    path('contacts/<int:pk>/', contact_detail),

    # UPDATE
    path('contacts/update/<int:pk>/', contact_update),

    # DELETE
    path('contacts/delete/<int:pk>/', contact_delete),
]