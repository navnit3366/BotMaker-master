from django.core.management.base import BaseCommand
from . import start_bot


class Command(BaseCommand):
    help = "Start bot"

    def add_arguments(self, parser):
        parser.add_argument("bot_id", nargs='?', type=int)
        parser.add_argument('--port', help="Set Bot Runner Port (default: 5555)", default=5555, type=int)

    def handle(self, *args, **options):
        if options['bot_id'] is None:
            self.stdout.write("Error. Bot id is required!")
            return
        self.stdout.write("Sending command....")
        resp = start_bot(options['bot_id'], options['port'])
        print(resp)
