# -*- coding: utf-8 -*-
#
# Date: 02/09/2019
# Filename: requirement.py
# Partially copied from project called similar-related-requirements-recommender
# (https://github.com/OpenReqEU/similar-related-requirements-recommender)
# Changelog:
#   - Removed unused methods
#       - replace_german_umlaut
#       - merge_two_dicts
#       - setup_logging
#       - make_dir_if_not_exists
#       - error
#       - is_complete_data_set
#       - cache_exists_for_preprocessed_tags_and_posts
#       - write_preprocessed_tags_and_posts_to_cache
#       - load_preprocessed_tags_and_posts_from_cache
#       - compute_hash_of_file
#       - clear_tag_predictions_for_posts
#       - add_coloring_to_emit_windows
#       - add_coloring_to_emit_ansi
#

import os


SRC_PATH = os.path.join(os.path.realpath(os.path.dirname(__file__)), "..")
APP_PATH = SRC_PATH
LOG_PATH = os.path.join(APP_PATH, "logs")
CACHE_PATH = os.path.join(APP_PATH, "temp", "cache")
HAC_CACHE_PATH = os.path.join(APP_PATH, "temp", "hac")


def is_int_or_float(str_value):
    value = int_or_float_from_string(str_value)
    return value is not None and isinstance(value, (int, float))


def int_or_float_from_string(str_value):
    assert(isinstance(str_value, str))
    try:
        value = int(str_value)
    except ValueError:
        try:
            value = float(str_value)
        except ValueError:
            value = None
    return value


class ExitCode(object):
    SUCCESS = 0
    FAILED = 1


def _cache_file_paths(cached_file_name_prefix):
    cached_tags_file_path = os.path.join(CACHE_PATH, cached_file_name_prefix + "_tags.pickle")
    cached_posts_file_path = os.path.join(CACHE_PATH, cached_file_name_prefix + "_posts.pickle")
    return cached_tags_file_path, cached_posts_file_path
