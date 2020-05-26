import xadmin
from xadmin import views
from .models import EmailVerifyRecord,Banner

class BaseSetting(object):
    enabel_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = '即学就会IT课后台管理页面'
    site_footer = 'Powered By Bruce - 2020'
    # 收起菜单
    menu_style = "accordion"

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)


class EmailVerifyRecordAdmin(object):
    '''
        后台展示的内容
        后台可以搜索的内容
        后台过滤器可以使用的内容
    '''
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type']
    list_filter = ['code','email','send_type','send_time']

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)


class BannerAdmin(object):
    list_display = ['title','image','url','index','add_time']
    search_fields = ['title','image','url','index']
    list_filter = ['title','image','url','index','add_time']

xadmin.site.register(Banner,BannerAdmin)







