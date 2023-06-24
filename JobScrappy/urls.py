from django.urls import path
from JobScrappy import views
from JobScrappy.models import Users

home_list_view = views.HomeListView.as_view(
    queryset=Users.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="user_list",
    template_name="JobScrappy/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("submit/", views.submitsuccess, name="submit"),
]