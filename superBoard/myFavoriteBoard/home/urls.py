from django.urls import path
from . import views

# Las vistas de acceso al aplicativo son las siguientes:
# http://localhost:8000/taskBoard/  Pagina del perfil admin
# http://localhost:8000/profile/    Pagina de ejemplo perfil consultor

urlpatterns = [
    path('home/', views.home),
    path('taskBoard/', views.taskBoard),
    path('taskBoardForm/', views.taskBoardForm),
    path('manyTaskBoardForm/', views.manyTaskBoardForm),
    path('storeActivity/', views.storeActivity),
    path('storeActivityBlock/', views.storeActivityBlock),
    path('updateStatusAct/', views.updateStatusAct),
    path('taskList/', views.consultTaskList),
    path('statistics/', views.statistics),
    path('consultGreenActivities/', views.consultGreenActivities),

    path('profile/', views.profile),
    path('storeBonus/', views.storeBonus),
    path('bonusList/', views.consultBonusList),
    path('storeAvatarSettings/', views.storeAvatarSettings),
    path('advancePanel/', views.advancePanel),
    path('consultAdvance/', views.consultAdvance)
]