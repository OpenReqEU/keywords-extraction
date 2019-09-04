# -*- coding: utf-8 -*-
#
# Date: 02/09/2019
# Filename: stemmer.py
# Partially copied from project called similar-related-requirements-recommender
# (https://github.com/OpenReqEU/similar-related-requirements-recommender)
# Changelog:
#   - Changed logger.info to logger.debug
#

import logging
import nltk
import os
from application.util import helper
from nltk.stem.porter import PorterStemmer


_logger = logging.getLogger(__name__)
nltk.data.path = [os.path.join(helper.APP_PATH, "corpora", "nltk_data")]


def porter_stemmer(posts):
    _logger.debug("Stemming for posts' tokens")
    porter = PorterStemmer()

    for post in posts:
        post.title_tokens = [porter.stem(word) for word in post.title_tokens]
        post.description_tokens = [porter.stem(word) for word in post.description_tokens]

