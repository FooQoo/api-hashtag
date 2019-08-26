from rest_framework import serializers
from .models import Word, Biterm, CoOccurrence, Hashtag, HashtagTask


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('word_id', 'char_string', )

    def create(self, validated_data):
        word = Word.objects.filter(
            char_string=validated_data['char_string']).first()
        if word is None:
            word = Word.objects.create(
                char_string=validated_data['char_string'])
        return word


class BitermSerializer(serializers.ModelSerializer):
    word_i = WordSerializer()
    word_j = WordSerializer()

    class Meta:
        model = Biterm
        fields = ('biterm_id', 'word_i', 'word_j')

    def create(self, validated_data):
        if validated_data['word_i']['char_string'] < validated_data['word_j']['char_string']:
            word_i_str, word_j_str = validated_data['word_i'][
                'char_string'], validated_data['word_j']['char_string']
        elif validated_data['word_i']['char_string'] > validated_data['word_j']['char_string']:
            word_i_str, word_j_str = validated_data['word_j'][
                'char_string'], validated_data['word_i']['char_string']
        else:
            return Biterm()

        biterm = Biterm.objects.filter(
            word_i__char_string=word_i_str, word_j__char_string=word_j_str).first()

        if biterm is None:
            word_i = Word.objects.filter(
                char_string=word_i_str).first()
            word_j = Word.objects.filter(
                char_string=word_j_str).first()

            if word_i is None:
                word_i = Word.objects.create(
                    char_string=word_i_str)
            if word_j is None:
                word_j = Word.objects.create(
                    char_string=word_j_str)

            biterm = Biterm.objects.create(
                word_i=word_i, word_j=word_j)

        return biterm


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ('tag_id', 'name',)

    def create(self, validated_data):
        tag = Hashtag.objects.filter(name=validated_data['name']).first()
        if tag is None:
            tag = Hashtag.objects.create(name=validated_data['name'])
        return tag


class CoOccurrenceSerializer(serializers.ModelSerializer):
    biterm = BitermSerializer()
    hashtag = HashtagSerializer()

    class Meta:
        model = CoOccurrence
        fields = ('id', 'biterm', 'hashtag', 'frequency')

    def create(self, validated_data):
        hashtag = Hashtag.objects.filter(
            name=validated_data['hashtag']['name']).first()
        biterm = Biterm.objects.filter(word_i__char_string=validated_data['biterm']['word_i']['char_string'],
                                       word_j__char_string=validated_data['biterm']['word_j']['char_string']
                                       ).first()

        if hashtag is None:
            hashtag = Hashtag.objects.create(
                name=validated_data['hashtag']['name'])
        if biterm is None:
            word_i = Word.objects.create(
                char_string=validated_data['biterm']['word_i']['char_string'])
            word_j = Word.objects.create(
                char_string=validated_data['biterm']['word_j']['char_string'])
            biterm = Biterm.objects.create(
                word_i=word_i, word_j=word_j)

        coOccurrance = CoOccurrence.objects.filter(
            hashtag=hashtag, biterm=biterm).first()

        if coOccurrance is None:
            coOccurrance = CoOccurrence.objects.create(
                hashtag=hashtag, biterm=biterm, frequency=1)
        else:
            coOccurrance.frequency += 1

        return coOccurrance


class HashtagTaskSerializer(serializers.ModelSerializer):
    hashtag = HashtagSerializer()

    class Meta:
        model = HashtagTask
        read_only_fields = ('updated_at', 'created_at')
        fields = ('task_id', 'hashtag', 'status')

    def create(self, validated_data):
        tag_data = validated_data['hashtag']
        tag = Hashtag.objects.filter(name=tag_data['name']).first()
        task = HashtagTask.objects.create(hashtag=tag)
        return task
