# -*- coding: utf-8 -*-

u"""
.. module:: urls
"""

from django.conf.urls import url

from apps.volontulo import views
from apps.volontulo.views import auth as auth_views
from apps.volontulo.views import offers as offers_views
from apps.volontulo.views import organizations as orgs_views

# pylint: disable=invalid-name
handler404 = 'apps.volontulo.views.page_not_found'
handler500 = 'apps.volontulo.views.server_error'


urlpatterns = [  # pylint: disable=invalid-name
    # homepage:
    url(r'^$', views.homepage, name='homepage'),

    # login and loggged user space:
    url(r'^login$', auth_views.login, name='login'),
    url(r'^logout$', auth_views.logout, name='logout'),
    url(r'^register$', auth_views.Register.as_view(), name='register'),
    url(
        r'^activate/(?P<uuid>[-0-9A-Za-z]+)$',
        auth_views.activate,
        name='activate'
    ),
    url(r'^password-reset$', auth_views.password_reset, name='password_reset'),
    url(
        r'^password-reset/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)$',
        auth_views.password_reset_confirm,
        name='password_reset_confirm'
    ),
    url(r'^me$', views.logged_user_profile, name='logged_user_profile'),
    # me/edit
    # me/settings

    # offers' namesapce:
    url(r'^offers$', offers_views.OffersList.as_view(), name='offers_list'),
    url(
        r'^offers/create$',
        offers_views.OffersCreate.as_view(),
        name='offers_create'
    ),
    url(
        r'^offers/reorder/(?P<id_>[0-9]+)?$',
        offers_views.OffersReorder.as_view(),
        name='offers_reorder'
    ),
    url(
        r'^offers/archived$',
        offers_views.OffersArchived.as_view(),
        name='offers_archived'
    ),
    url(
        r'^offers/(?P<slug>[\w-]+)/(?P<id_>[0-9]+)$',
        offers_views.OffersView.as_view(),
        name='offers_view'
    ),
    url(
        r'^offers/(?P<slug>[\w-]+)/(?P<id_>[0-9]+)/edit$',
        offers_views.OffersEdit.as_view(),
        name='offers_edit'
    ),
    url(
        r'^offers/(?P<slug>[\w-]+)/(?P<id_>[0-9]+)/join$',
        offers_views.OffersJoin.as_view(),
        name='offers_join'
    ),
    # offers/filter

    # users' namesapce:
    # users
    # users/filter
    # users/slug-id
    # users/slug-id/contact

    # organizations' namespace:
    url(
        r'^organizations$',
        orgs_views.organizations_list,
        name='organizations_list'
    ),
    url(
        r'^organizations/create$',
        orgs_views.OrganizationsCreate.as_view(),
        name='organizations_create',
    ),
    url(
        r'^organizations/(?P<slug>[\w-]+)/(?P<id_>[0-9]+)$',
        orgs_views.organization_view,
        name='organization_view'
    ),
    url(
        r'^organizations/(?P<slug>[\w-]+)/(?P<id_>[0-9]+)/edit$',
        orgs_views.organization_form,
        name='organization_form'
    ),
    # organizations/filter
    # organizations/<slug>/<id>/contact

    # others:
    url(
        r'^pages/(?P<template_name>[\w-]+)$',
        views.static_pages,
        name='static_page'
    ),
    url(
        r'^contact$',
        views.contact_form,
        name='contact_form'
    ),
    url(
        r'^office$',
        views.office_info,
        name='officee'
    ),
]
