from django.urls import path
from fotoblog.views import page_views, post_detail_views


app_name = "fotoblog"

urlpatterns = [
    path("", page_views, name="home_views"),
    path("<slug:page_slug>/", page_views, name="page_views"),
    path("<slug:page_slug>/<slug:post_slug>", page_views, name="page_views"),
    path("<slug:page_slug>/<slug:post_slug>/<int:post_id>",
         post_detail_views,
         name="post_details"),
]
