from django.contrib import admin
from django.urls import path, include
from pybo.views import base_views
from common import views as common_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', common_views.home, name='home'),  # 루트 URL → 홈화면
    
    path('pybo/', include('pybo.urls')),       # 기존 게시판 URL은 /pybo/ 로 진입
    path('common/', include('common.urls')),   # 로그인/회원가입 등
    
    # allauth
    path('accounts/', include('allauth.urls')),
]

handler404 = 'common.views.page_not_found'
# handler500 = 'common.views.Internal_Server_Error'
# 오류 발생