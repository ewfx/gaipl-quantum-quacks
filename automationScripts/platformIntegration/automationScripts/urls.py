from django.urls import path
from .views import UpdateGitHubView, ProcessDataView

urlpatterns = [
    path('update-github/', UpdateGitHubView.as_view(), name='update_github'),
    path('process-data/', ProcessDataView.as_view(), name='process_data'),
]