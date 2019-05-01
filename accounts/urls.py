from django.conf.urls import url

from .views import UsernameSearchFormView
from .views import AjaxLoadAccountPostsView
from .views import AjaxLoadAllAccountPostsView
from .views import AjaxLoadAccountHistoryView
from .views import ImagesBacklinkView
from .views import ImagesBacklinkViewDetail
from .views import AjaxLoadPostsImagesView
from .views import PepperView
from .views import TrainingGrounds

# urls here are for loading all of the different python views
urlpatterns = [
    url(
        r'^username_search_form/',
        UsernameSearchFormView.as_view(),
        name='username_search_form',
    ),

    url(
        r'^ax_load_account_posts/',
        AjaxLoadAccountPostsView.as_view(),
        name='ax_load_account_posts',
    ),

    url(
        r'^ax_load_all_account_posts/',
        AjaxLoadAllAccountPostsView.as_view(),
        name='ax_load_all_account_posts',
    ),

    url(
        r'^ax_load_account_history/',
        AjaxLoadAccountHistoryView.as_view(),
        name='ax_load_account_history',
    ),

    url(
        r'^images_backlink/$',
        ImagesBacklinkView.as_view(),
        name='images_backlink',
    ),

    url(
        r'^images_backlink/(?P<username>[-\w.@]+)/$',
        ImagesBacklinkViewDetail.as_view(),
        name='images_backlink_detail',
    ),

    url(
        r'^ax_load_posts_images/',
        AjaxLoadPostsImagesView.as_view(),
        name='ax_load_posts_images',
    ),

    url(
        r'^papa-pepper-selfie-contest-1/',
        PepperView.as_view(),
        name='pepper_selfie_contest',
    ),

    url(
        r'^training_grounds/',
        TrainingGrounds.as_view(),
        name='training_grounds',
    ),
]
