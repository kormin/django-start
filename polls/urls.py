from django.conf.urls import url

from . import views

# https://docs.djangoproject.com/en/1.10/intro/tutorial03/#namespacing-url-names
app_name = 'polls'
urlpatterns = [
	# ex: /polls/
	# url(r'^$', views.index, name='index'),
	url(r'^$', views.IndexView.as_view(), name='index'),
	# ex: /polls/5/
	# changed from <question_id> to <pk>
	# url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	# ex: /polls/5/results/
	# url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	# ex: /polls/5/vote/
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]