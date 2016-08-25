"""
Global nordlys config

@author: Krisztian Balog (krisztian.balog@uis.no)
"""

from os import path

NORDLYS_DIR = path.dirname(path.abspath(__file__))
DATA_DIR = path.dirname(path.dirname(path.abspath(__file__))) + "/data"
OUTPUT_DIR = path.dirname(path.dirname(path.abspath(__file__))) + "/data"

STATS_MENTION_ENTITY = DATA_DIR + "/mention_entity.tsv"
ENTITY_INLINKS = DATA_DIR + "/entity_inlinks.tsv"
ENTITY_PAIRS_INLINKS = DATA_DIR + "/entity_pairs_inlinks.tsv"

SNIPPETS = DATA_DIR + "/snippets.txt"
