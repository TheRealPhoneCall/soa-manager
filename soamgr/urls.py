from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^100-index$', views.index, name='index'),
    url(r'^110-home$', views.home, name='home'),
    # 200: adviser's pages
    url(r'^200-adviser-main$', views.home, name='adviser-main'),
    url(r'^210-adviser-order-soa$', views.home, name='adviser-order-soa'),
    url(r'^220-adviser-review-oa$', views.home, name='adviser-review-oa'),
    url(r'^230-adviser-buy-credit$', views.home, name='adviser-buy-credit'),
    url(r'^240-adviser-preferences$', views.home, name='adviser-preferences'),
    url(r'^300-manage-advisers$', views.home, name='manage-advisers'),
    # 400: QPP's pages
    url(r'^400-qpp-main$', views.home, name='qpp-main'),
    url(r'^410-qpp-create-oa$', views.home, name='qpp-create-oa'),
    url(r'^420-qpp-manage-paraplanners$', views.home, name='qpp-manage-paraplanners'),
    url(r'^430-qpp-manage-users$', views.home, name='qpp-manage-users'),
    url(r'^440-qpp-manage-system$', views.home, name='qpp-manage-system'),
    # 600: paraplanner's pages
    url(r'^600-paraplanner-main$', views.home, name='paraplanner-main'),
    url(r'^610-paraplanner-claim-job$', views.home, name='paraplanner-claim-job'),
    url(r'^620-paraplanner-job-status$', views.home, name='paraplanner-job-status'),
    url(r'^630-paraplanner-profile$', views.home, name='paraplanner-profile'),
    url(r'^640-paraplanner-notes$', views.home, name='paraplanner-notes'),
    # 900: legal
    url(r'^900-license-information$', views.home, name='license-information'),
    url(r'^910-legal-agreements$', views.home, name='legal-agreements'),
    url(r'^920-terms-of-use$', views.home, name='terms-of-use'),
    url(r'^930-privacy-policy$', views.home, name='privacy-policy'),
    # 1100: reference pages
    url(r'^1100-order-soa$', views.home, name='ref-order-soa'),
    url(r'^1110-completed-soas$', views.home, name='ref-completed-soas'),
    url(r'^1120-manage-advisers$', views.home, name='ref-manage-advisers'),
    url(r'^1130-credit-use-history$', views.home, name='ref-credit-use-history'),
    url(r'^1140-credit-purchase$', views.home, name='ref-credit-purchase'),
]
