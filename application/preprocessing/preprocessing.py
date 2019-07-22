# -*- coding: utf-8 -*-

import logging
import os
import csv
from application.entities.requirement import Requirement
from application.util import helper
from functools import reduce
from application.preprocessing import tokenizer
from application.preprocessing import filters
from application.preprocessing import stopwords
from application.preprocessing import stemmer


_logger = logging.getLogger(__name__)


def _to_lower_case(requirements):
    _logger.info("Lower case requirement title and description")
    for requirement in requirements:
        assert(isinstance(requirement, Requirement))
        requirement.title = requirement.title.lower()
        requirement.description = requirement.description.lower()


def _remove_english_abbreviations(requirements):
    _logger.info("Remove abbreviations")
    for requirement in requirements:
        requirement.title = requirement.title.replace('e.g.', '')
        requirement.title = requirement.title.replace('i.e.', '')
        requirement.title = requirement.title.replace('in order to', '')
        requirement.description = requirement.description.replace('e.g.', '')
        requirement.description = requirement.description.replace('i.e.', '')
        requirement.description = requirement.description.replace('in order to', '')


def preprocess_requirements(requirements, enable_stemming=False):
    lang = 'en'
    _to_lower_case(requirements)
    _remove_english_abbreviations(requirements)

    all_requirement_titles = list(map(lambda requirement: requirement.title, requirements))
    important_key_words = tokenizer.key_words_for_tokenization(all_requirement_titles)
    _logger.info("Number of key words {} (altogether)".format(len(important_key_words)))
    tokenizer.tokenize_requirements(requirements, important_key_words, lang=lang)
    n_tokens = reduce(lambda x, y: x + y, map(lambda t: len(list(t.title_tokens)) + len(list(t.description_tokens)), requirements))
    filters.filter_tokens(requirements, important_key_words)
    stopwords.remove_stopwords(requirements, lang=lang)

    if enable_stemming is True:
        _logger.warning("Stemming enabled!")
        stemmer.porter_stemmer(requirements)

    n_filtered_tokens = n_tokens - reduce(lambda x, y: x + y, map(lambda t: len(list(t.title_tokens)) + len(list(t.description_tokens)), requirements))
    if n_tokens > 0:
        _logger.info("Removed {} ({}%) of {} tokens (altogether)".format(n_filtered_tokens,
                     round(float(n_filtered_tokens) / n_tokens * 100.0, 2), n_tokens))
    return requirements

