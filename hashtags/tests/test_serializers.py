from django.test import TestCase
from hashtags.serializers import WordSerializer, BitermSerializer, CoOccurrenceSerializer, HashtagSerializer
from hashtags.models import Word, Biterm, CoOccurrence, Hashtag


class WordSerializerTest(TestCase):
    fixtures = ['db_init.json']

    def setUp(self):
        self.serializer = WordSerializer()

    def test_create(self):
        validated_data = {'char_string': 'python'}

        word = self.serializer.create(validated_data)
        words = Word.objects.all()
        self.assertEqual(word.char_string, validated_data['char_string'])
        self.assertEqual(len(words), 3)

    def test_create_duplicate(self):
        validated_data = {'char_string': 'maven'}

        word = self.serializer.create(validated_data)
        words = Word.objects.all()
        self.assertEqual(word.char_string, validated_data['char_string'])
        self.assertEqual(len(words), 2)


class BitermSerializerTest(TestCase):
    fixtures = ['db_init.json']

    def setUp(self):
        self.serializer = BitermSerializer()

    def test_create(self):
        validated_data = {'word_i': {'char_string': 'conda'},
                          'word_j': {'char_string': 'python'}}

        biterm = self.serializer.create(validated_data)
        biterms = Biterm.objects.all()
        words = Word.objects.all()
        self.assertEqual(biterm.word_i.char_string,
                         validated_data['word_i']['char_string'])
        self.assertEqual(biterm.word_j.char_string,
                         validated_data['word_j']['char_string'])
        self.assertEqual(len(words), 4)
        self.assertEqual(len(biterms), 2)

    def test_create_duplicate_biterm(self):
        validated_data = {'word_i': {'char_string': 'java'},
                          'word_j': {'char_string': 'maven'}}

        biterm = self.serializer.create(validated_data)
        biterms = Biterm.objects.all()
        words = Word.objects.all()

        self.assertEqual(biterm.word_i.char_string,
                         validated_data['word_i']['char_string'])
        self.assertEqual(biterm.word_j.char_string,
                         validated_data['word_j']['char_string'])
        self.assertEqual(len(words), 2)
        self.assertEqual(len(biterms), 1)


class HashtagSerializerTest(TestCase):
    fixtures = ['db_init.json']

    def setUp(self):
        self.serializer = HashtagSerializer()

    def test_create(self):
        validated_data = {'name': 'python'}

        hashtag = self.serializer.create(validated_data)
        hashtags = Hashtag.objects.all()
        self.assertEqual(hashtag.name, validated_data['name'])
        self.assertEqual(len(hashtags), 2)

    def test_create_duplicate(self):
        validated_data = {'name': 'spring'}

        hashtag = self.serializer.create(validated_data)
        hashtags = Hashtag.objects.all()
        self.assertEqual(hashtag.name, validated_data['name'])
        self.assertEqual(len(hashtags), 1)


class CoOccurrenceSerializerTest(TestCase):
    fixtures = ['db_init.json']

    def setUp(self):
        self.serializer = CoOccurrenceSerializer()

    def test_create(self):
        validated_data = {'biterm': {'word_i': {'char_string': 'java'},
                                     'word_j': {'char_string': 'maven'}}, 'hashtag': {'name': 'lombok'}}

        coOccurrence = self.serializer.create(validated_data)
        coOccurrences = CoOccurrence.objects.all()
        self.assertEqual(coOccurrence.biterm.word_i.char_string,
                         validated_data['biterm']['word_i']['char_string'])
        self.assertEqual(coOccurrence.biterm.word_j.char_string,
                         validated_data['biterm']['word_j']['char_string'])
        self.assertEqual(coOccurrence.hashtag.name,
                         validated_data['hashtag']['name'])
        self.assertEqual(len(coOccurrences), 2)
        self.assertEqual(coOccurrences[0].frequency, 1)

    def test_duplicate_create(self):
        validated_data = {'biterm': {'word_i': {'char_string': 'java'},
                                     'word_j': {'char_string': 'maven'}}, 'hashtag': {'name': 'spring'}}

        coOccurrence = self.serializer.create(validated_data)
        coOccurrences = CoOccurrence.objects.all()
        self.assertEqual(coOccurrence.biterm.word_i.char_string,
                         validated_data['biterm']['word_i']['char_string'])
        self.assertEqual(coOccurrence.biterm.word_j.char_string,
                         validated_data['biterm']['word_j']['char_string'])
        self.assertEqual(coOccurrence.hashtag.name,
                         validated_data['hashtag']['name'])
        self.assertEqual(len(coOccurrences), 1)
        self.assertEqual(coOccurrences[0].frequency, 1)
