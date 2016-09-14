from dynamic_preferences.types import *
from dynamic_preferences.registries import user_preferences_registry, global_preferences_registry

admin = Section('admin')

@global_preferences_registry.register
class SiteTitle(BooleanPreference):
    section = admin
    name = 'registro_usuarios'
    verbose_name = "Creación de usuarios disponible"
    default = False