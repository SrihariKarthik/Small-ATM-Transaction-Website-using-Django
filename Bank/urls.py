from django.urls import path
from . import views
app_name = "Bank"
urlpatterns = [
    path('',views.BankHomePage.as_view(),name="Home"),
    path('Form',views.BankUserForm.as_view(),name="Form"),
    path('List',views.BankUserList.as_view(),name="List"),
    path('Detail/<int:pk>',views.BankDetail.as_view(),name="Detail"),
    path('Update/<int:pk>',views.BankUserUpdate.as_view(),name="Update"),
    path('Delete/<int:pk>',views.BankUserDelete.as_view(),name="Delete"),
    path('ATMw',views.ATMWithdraw,name="Withdraw"),
    path('ATMd',views.ATMDeposit,name="Deposit"),
    path('ThankYou',views.ThankYou,name="ThankYou"),
    path('SignUp',views.SignUp.as_view(),name='SignUp')
]
