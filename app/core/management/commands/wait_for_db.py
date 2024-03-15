# django가 DB연결에 실패했을때 재시도하도록 만드는 로직
from django.core.management.base import BaseCommand
from django.db import connections
import time
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg20pError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for DB connection...")

        is_db_connected = None
        while not is_db_connected:
            try:
                is_db_connected = connections["default"]
            except (OperationalError, Psycopg20pError):
                self.stdout.write("Retrying DB connection...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Successfully Successfully Successfully "))
