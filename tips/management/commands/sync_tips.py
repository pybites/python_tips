import sys

import requests

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from tips.models import Tip

PYBITES = 'pybites'
TIPS_PAGE = 'https://codechalleng.es/api/tips'


class Command(BaseCommand):
    """Quick and dirty, using bs4 from last article:
       https://github.com/pybites/blog_code/blob/master/tips/tips.py

       About django-admin commands:
       https://docs.djangoproject.com/en/2.1/howto/custom-management-commands/
    """
    help = 'Script to insert pybites tips from platform'

    def handle(self, *args, **options):
        try:
            user = User.objects.get(username=PYBITES)
        except User.DoesNotExist:
            error = 'Cannot run this without SU pybites'
            sys.exit(error)

        resp = requests.get(TIPS_PAGE)
        resp.raise_for_status()

        new_tips_created = 0
        for row in resp.json():
            _, created = Tip.objects.get_or_create(
                tip=row["tip"],
                code=row["code"],
                link=row["link"],
                user=user,
                approved=True,
                share_link=row["share_link"])

            if created:
                new_tips_created += 1

        print(f'Done: {new_tips_created} tips imported')
