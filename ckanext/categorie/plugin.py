# encoding: utf-8

from ckan import plugins
from ckan.lib.plugins import DefaultTranslation


class CategoriePlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.ITranslation)
