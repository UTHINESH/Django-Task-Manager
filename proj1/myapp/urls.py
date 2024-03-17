from django.urls import path
from . import views

urlpatterns=[


    # HOME PAGE

    path('',views.home,name=""),
    
# ----------------DJANGO ADMIN USER OPERATIONS-------------------------#


    # REGISTER A USER

    path('register',views.register,name='register'),

    #LOGIN  A USER

    path('my-login',views.my_login,name='my-login'),

    # DASHBOARD PAGE

    path('dashboard',views.dashboard,name='dashboard'),

    # CREATE TASK

    path('create-task',views.createTask,name='create-task'),

    # READ TASK

    path('view-tasks',views.viewTask,name='view-tasks'),

    # UPDATE TASK

    path('update-task/<str:pk>/',views.updateTask,name='update-task'),

    # DELETE TASK

    path('delete-task/<str:pk>/',views.deleteTask,name='delete-task'),


    # LOGOUT A USER

    path('user-logout',views.user_logout,name='user-logout'),

]

