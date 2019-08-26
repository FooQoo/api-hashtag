from rest_framework import serializers
from .models import Word, Biterm, CoOccurrence, Hashtag, HashtagTask
from drf_writable_nested import WritableNestedModelSerializer


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

    def validate(self, data):
        if data['word_i']['char_string'] > data['word_j']['char_string']:
            raise serializers.ValidationError(
                'Biterm is not in dictionary order.')
        elif data['word_i']['char_string'] == data['word_j']['char_string']:
            raise serializers.ValidationError(
                'Biterm must consist of two different words.')

        return data

    def create(self, validated_data):
        word_i_str, word_j_str = validated_data['word_i']['char_string'], validated_data['word_j']['char_string']

        biterm = Biterm.objects.filter(
            word_i__char_string=word_i_str, word_j__char_string=word_j_str).first()

        if biterm is None:
            word_i = Word.objects.filter(
                char_string=word_i_str).first()
            word_j = Word.objects.filter(
                char_string=word_j_str).first()

            biterm_id = str(word_i.word_id)+str(word_j.word_id)
            biterm = Biterm.objects.create(biterm_id=biterm_id,
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
        fields = ('id', 'biterm', 'hashtag')

    def create(self, validated_data):
        hashtag = Hashtag.objects.filter(
            name=validated_data['hashtag']['name']).first()
        biterm = Biterm.objects.filter(word_i__char_string=validated_data['biterm']['word_i']['char_string'],
                                       word_j__char_string=validated_data['biterm']['word_j']['char_string']
                                       ).first()

        coOccurrance = CoOccurrence.objects.filter(
            hashtag=hashtag, biterm=biterm).first()

        if coOccurrance is None:
            coOccurrance = CoOccurrence.objects.create(
                hashtag=hashtag, biterm=biterm, frequency=1)
        else:
            coOccurrance.frequency += 1
            coOccurrance.save()

        return coOccurrance


class HashtagTaskSerializer(serializers.ModelSerializer):
    hashtag = HashtagSerializer()

    class Meta:
        model = HashtagTask
        read_only_fields = ('updated_at', 'created_at')
        fields = ('task_id', 'hashtag', 'status')

    def create(self, validated_data):
        tag_data = validated_data['hashtag']
        task = HashtagTask.objects.filter(
            hashtag__name=tag_data['name']).first()
        if task is None:
            tag = Hashtag.objects.filter(name=tag_data['name']).first()
            task = HashtagTask.objects.create(
                hashtag=tag)

        return task
