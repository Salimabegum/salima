from django.urls import path
from . import views
urlpatterns = [
			path('product_field/',views.product_field,name='product_field'),
			path('homepage/',views.homepage,name='homepage'),
			path('homepage1/<id>',views.homepage1,name='homepage1'),
			path('User_field/',views.User_field,name='User_field'),
			path('homepage2/',views.homepage2,name='homepage2'),
			path('destroy/<id>/',views.destroy,name='destroy'),
			path('dest/<id>/',views.dest,name='dest'),
			path('buy_user/<id>/',views.buy_user,name='buy_user'),
			path('homepage3/<id>',views.homepage3,name='homepage3'),
			path('single/<id>',views.single,name='single'),

		]