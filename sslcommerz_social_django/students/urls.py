from django.urls import path
from .views import Index, AddStudent, EditStudent, DeleteStudent


app_name = "students"
urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("add-student/", AddStudent.as_view(), name="add-student"),
    path("edit-student/<int:pk>/", EditStudent.as_view(), name="edit-student"),
    path("delete-student/<int:pk>/", DeleteStudent.as_view(), name="delete-student"),
]
