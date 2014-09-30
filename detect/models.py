from django.db import models
import string, textract, nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from collections import Counter

class Organization(models.Model):
    name = models.CharField(max_length=100)

class Word(models.Model):
    stem = models.CharField(max_length=100)
    display = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        stemmer = PorterStemmer()
        self.stem = stemmer.stem(self.display)
        super(Word, self).save(*args, **kwargs)

class Document(models.Model):
    total_word_count = models.PositiveIntegerField()
    word_counts = models.ManyToManyField(Word, through='WordCount')
    source_file = models.FileField(upload_to='documents')

    def save(self, *args, **kwargs):
        super(Document, self).save(*args, **kwargs)
        text = textract.process(self.source_file.url)
        filtered_stems = self.get_filtered_stems(text)
        self.total_word_count = len(filtered_stems)
        self.count_target_words(filtered_stems)
        super(Document, self).save(*args, **kwargs)

    def get_filtered_stems(self, raw_text):
        punctuation_stripped = raw_text.translate(None, string.punctuation)
        word_list = nltk.word_tokenize(punctuation_stripped)

        stemmer = PorterStemmer()
        return [stemmer.stem(w) for w in word_list if not w in stopwords.words('english')] 

    def count_target_words(self, filtered_stems):
        counts = Counter(filtered_stems)
        for wrd in Word.objects.all():
            if counts[wrd.stem] > 0:
                #print '{:<20}{:<5}'.format(wrd.display, counts[wrd.stem])
                wc = WordCount.objects.create(word=wrd, count=counts[wrd.stem], document=self)

class WordCount(models.Model):
    document = models.ForeignKey(Document)
    word = models.ForeignKey(Word)
    count = models.PositiveIntegerField()