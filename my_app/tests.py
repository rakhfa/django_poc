import datetime

from django.test import TestCase


class MonsterModelTest(TestCase):

    def test_monster_content(self):
        self.assertEquals("Godzilla", "Godzilla")

    def test_monster_content2(self):
        self.assertEquals("Godzilla", "Godzillaa")
