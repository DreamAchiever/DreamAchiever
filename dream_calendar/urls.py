from core import dream_core
from dream_calendar import views


urlpatterns = dream_core.UrlMaker.build_url(views)
