import datetime

from django.test import TestCase


class MonsterModelTest(TestCase):

    def test_monster_content(self):
        self.assertEquals("Godzilla", "Godzilla")
