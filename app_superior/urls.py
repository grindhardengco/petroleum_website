from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('sell', views.sell),
    path('add_property', views.add_property),
    path('thank_property', views.thank_property),
    path('help', views.help),
    path('add_project', views.add_project),
    path('thank_project', views.thank_project),
    path('partner', views.partner),
    path('add_partner', views.add_partner),
    path('thank_partner', views.thank_partner),
    path('dashboard', views.dashboard),
    path('admin', views.admin),
    path('admin/property/<int:prop_id>', views.edit_prop),
    path('admin/update_prop/<int:prop_id>', views.update_prop)
]