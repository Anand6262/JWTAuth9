from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView #JWT(JSON Web Token)##We have already written many classes in //simplejwt// library. This is the beauty of JWT!!
from rest_framework_simplejwt.views import TokenRefreshView #JWT
from rest_framework_simplejwt.views import TokenVerifyView #JWT

#Creating Router Object
router=DefaultRouter()

#Register StudentViewSet with Router
router.register('stucreate', views.StudentModelViewSet, basename='student') #(IP/stucreste/) is our path to run this API
#We can write anything in the place of //student//, //router//, //stucreate//

urlpatterns = [
    path('',include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')), #For Login button in UI
    path('gettoken/', TokenObtainPairView.as_view(), name='Token_Obtain_Pair'), #To get 2 tokens i.e.(access token) and (refresh token)  ##we can write anything in the place of //name='Token_Obtain_Pair'//
    path('refreshtoken/', TokenRefreshView.as_view(), name='Token_Refresh'), #To refresh a expired token  ##we can write anything in the place of //name='Token_Refresh'//
    path('verifytoken/', TokenVerifyView.as_view(), name='Token_Verify'), #To verify token  ##we can write anything in the place of //name='Token_Verify'//
]

#1)Command to get token[(i)ACCESS TOKEN, (ii)REFRESH TOKEN]
#(http POST http://127.0.0.1:8000/gettoken/ username="Superuser" password="admin")

#2)Command to verify token
#(http POST http://127.0.0.1:8000/verifytoken/ token="LINK OF THE ACCESS TOKEN")

#3)Command to refresh token
#(http post http://127.0.0.1:8000/refreshtoken/ refresh="LINK OF THE REFRESH TOKEN to get a new ACCESS TOKEN")