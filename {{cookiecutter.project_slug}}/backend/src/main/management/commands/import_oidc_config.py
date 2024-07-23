from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
import os

class Command(BaseCommand):
    help = "Importa los catálogos desde archivos csv"

    def handle(self, *args, **options):
        from oidc_provider.models import Client, ResponseType
        try:
            # Inicia una transacción para asegurar la atomicidad
            with transaction.atomic():
                # Obtiene o crea el ResponseType, evitando duplicados
                response_type, created = ResponseType.objects.get_or_create(value='code')
                
                # Crea el cliente
                c = Client(name='nuxt', client_id=os.environ.get('OIDC_CLIENT_ID'), client_secret=os.environ.get('OIDC_CLIENT_SECRET'), redirect_uris=['http://localhost:3000/auth/oidc/callback'])
                c.save()
                
                # Añade el ResponseType al cliente
                c.response_types.add(response_type)
                
                self.stdout.write(self.style.SUCCESS('Cliente y ResponseType correctamente configurados.'))
        except ResponseType.DoesNotExist:
            self.stdout.write(self.style.ERROR('ResponseType "code" no existe.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al configurar el Cliente y ResponseType: {e}'))