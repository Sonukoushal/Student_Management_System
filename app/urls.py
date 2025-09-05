from django.urls import path
from .views import StudentView,StudentAdd,GetOne,Update,studentpatch,StudentDelete

urlpatterns = [
    path("get/",StudentView.as_view(),name="get"),
    path("add/",StudentAdd.as_view(),name="add"),
    path("getone/<int:id>/",GetOne.as_view(),name="getone"),
    path("update/<int:id>/",Update.as_view(),name="update"),
    path("patch/<int:id>/",studentpatch.as_view(),name="patch"),
    path("delete/<int:id>/",StudentDelete.as_view(),name="delete")
]
