# -*- coding: utf-8 -*-
#
# Date: 02/09/2019
# Filename: stopwords.py
# Partially copied from project called similar-related-requirements-recommender
# (https://github.com/OpenReqEU/similar-related-requirements-recommender)
# Changelog:
#   - Changed logger.info to logger.debug
#   - Added decoding from bytes to string when reading the stopwords file

import os
import logging
from application.util import helper


_logger = logging.getLogger(__name__)


def remove_stopwords(requirements, lang="en"):
    _logger.debug("Removing stop-words from requirement' tokens")
    stop_words_file_path = os.path.join(helper.APP_PATH, 'corpora', 'stopwords_' + lang)
    data_set_stop_words = set()
    if os.path.isfile(stop_words_file_path):
        with open(stop_words_file_path, 'rb') as f:
            for line in f:
                data_set_stop_words.add(line.strip().decode("utf-8"))

    stop_words = data_set_stop_words

    for requirement in requirements:
        requirement.title_tokens = list(filter(lambda t: t not in stop_words, requirement.title_tokens))
        requirement.description_tokens = list(filter(lambda t: t not in stop_words, requirement.description_tokens))

