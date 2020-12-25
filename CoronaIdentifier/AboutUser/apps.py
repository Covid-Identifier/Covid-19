from django.apps import AppConfig


class AboutUserConfig(AppConfig):
    name = 'AboutUser'

    def ready(self):
        import AboutUser.signals