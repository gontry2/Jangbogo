from django.urls import path
from jangbogo.views import users_views

app_name = 'users'

urlpatterns = [
    path('login/', users_views.logIn, name="logIn"), #회원로그인
    path('logout/', users_views.logOut, name="logOut"), #로그아웃
    path('signup/', users_views.signUp, name="signUp"), #회원가입
    path('login_register/', users_views.loginRegister, name="loginRegister"), #화면이동
    path('<int:user_id>/', users_views.userInfo, name="userInfo"), #회원정보 조회
    path('<int:user_id>/user_update', users_views.userUpdate, name="userUpdate"), #회원정보 수정
    path('<int:user_id>/user_delete', users_views.userDelete, name="userDelete"), #회원탈퇴
    path('<int:user_id>/has_product/', users_views.hasProduct, name="hasProduct"), #구매,보유 목록 조회
    path('<int:user_id>/add_product/', users_views.addProduct, name="addProduct"), #구매,보유 목록 추가
    path('<int:user_id>/<int:product_id>/delete_product/', users_views.deleteProduct, name="deleteProduct"), #구매,보유 목록 삭제
    path('<int:user_id>/notice_board/', users_views.noticeBoard, name="noticeBoard"), #종합정보 조회 화면 이동
]
