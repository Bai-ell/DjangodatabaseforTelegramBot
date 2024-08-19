from django.urls import path
from .views import QuestionnaireCreateView, QuestionnaireListView, QuestionnaireDetailView

urlpatterns = [
    path('create/', QuestionnaireCreateView.as_view(), name='questionnaire-create'),
    path('list/', QuestionnaireListView.as_view(), name='questionnaire-list'),
    path('detail/<int:id>/', QuestionnaireDetailView.as_view(), name='questionnaire-detail'),
]
