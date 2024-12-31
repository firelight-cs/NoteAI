from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

# -------------------- all available summarizers in sumy  -----------------------

from sumy.summarizers.lsa import LsaSummarizer # good for long texts
from sumy.summarizers.kl import KLSummarizer # good for short texts
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.sum_basic import SumBasicSummarizer
from sumy.summarizers.reduction import ReductionSummarizer

# ------------------------------------------------------------------------------

class TextSummarizer:
    def __init__(self, language="russian", sentences_count=10):
        self.language = language
        self.sentences_count = sentences_count
        self.stemmer = Stemmer(self.language)
        self.summarizer = KLSummarizer(self.stemmer)
        self.summarizer.stop_words = get_stop_words(self.language)

    def summarize(self, parser):
        sentences_list = [str(sentence) for sentence in self.summarizer(parser.document, self.sentences_count)]
        return " ".join(sentences_list)

    def summarize_url(self, url):
        parser = HtmlParser.from_url(url, Tokenizer(self.language))
        return self.summarize(parser)
    
    def summarize_string(self, text):
        parser = PlaintextParser.from_string(text, Tokenizer(self.language))
        return self.summarize(parser)
    
    def summarize_file(self, file_path):
        parser = PlaintextParser.from_file(file_path, Tokenizer(self.language))
        return self.summarize(parser)