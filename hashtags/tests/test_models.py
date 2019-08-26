from django.test import TestCase
from hashtags.models import Word, Biterm, Hashtag, CoOccurrence


class HashtagModelTests(TestCase):
    def test_create(self):
        tag = Hashtag()
        tag.name = "maven"
        tag.save()
        saved_tag = Hashtag.objects.all()
        self.assertEqual(saved_tag.count(), 1)
        self.assertEqual(saved_tag[0].name, "maven")


class WordModelTests(TestCase):
    def test_create(self):
        word = Word()
        word.char_string = "maven"
        word.save()
        saved_word = Word.objects.all()
        self.assertEqual(saved_word.count(), 1)
        self.assertEqual(saved_word[0].char_string, "maven")


class BitermModelTests(TestCase):
    def test_create(self):
        word_i, word_j = Word(), Word()
        word_i.char_string, word_j.char_string = "spring", "java"
        word_i.save()
        word_j.save()
        biterm = Biterm()
        biterm.word_i, biterm.word_j = word_i, word_j
        biterm.save()
        saved_biterm = Biterm.objects.all()
        self.assertEqual(saved_biterm.count(), 1)
        self.assertEqual(saved_biterm[0].word_i.char_string,
                         "spring")
        self.assertEqual(saved_biterm[0].word_j.char_string, "java")


class CoOccuranceModelTests(TestCase):
    def test_create(self):
        word_i, word_j = Word(), Word()
        word_i.char_string, word_j.char_string = "spring", "java"
        word_i.save()
        word_j.save()
        biterm = Biterm()
        biterm.word_i, biterm.word_j = word_i, word_j
        biterm.save()

        tag = Hashtag()
        tag.name = "maven"
        tag.save()
        cooccurrence = CoOccurrence()
        cooccurrence.hashtag = tag
        cooccurrence.biterm = biterm
        cooccurrence.frequency = 1
        cooccurrence.save()

        saved_cooccurence = CoOccurrence.objects.all()
        self.assertEqual(saved_cooccurence.count(), 1)
        self.assertEqual(saved_cooccurence[0].hashtag.name, tag.name)
        self.assertEqual(
            saved_cooccurence[0].biterm.word_i.char_string, biterm.word_i.char_string)
        self.assertEqual(
            saved_cooccurence[0].biterm.word_j.char_string, biterm.word_j.char_string)
        self.assertEqual(saved_cooccurence[0].frequency, 1)
