from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import api_views

app_name = "api"

urlpatterns = [
    path("public-data/", api_views.PublicDataListAPIView.as_view(), name="public-data"),
    path("public-data/members/", api_views.PublicDataMembers.as_view()),
    path(
        "public-data/sources-by-member/",
        api_views.PublicDataSourcesByUserAPIView.as_view(),
    ),
    path(
        "public-data/members-by-source/",
        api_views.PublicDataUsersBySourceAPIView.as_view(),
        name="members-by-source",
    ),
    path(
        "public-data/datatypes/",
        api_views.PublicDataTypesListAPIView.as_view(),
        name="datatypes",
    ),
    path(
        "public-data/projects/",
        api_views.PublicProjectsListAPIView.as_view(),
        name="projects",
    ),
]


urlpatterns = format_suffix_patterns(urlpatterns)
