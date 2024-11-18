import os
from serpapi import GoogleSearch
from util import *


def main(entry):
    """
    receives single list entry from google-scholar data file
    returns list of sources to cite
    """

    # get api key (serp api key to access google scholar)
    # api_key = os.environ.get("GOOGLE_SCHOLAR_API_KEY", "")
    # print("GOOGLE_SCHOLAR_API_KEY:", api_key)
    # print("GOOGLE_SCHOLAR_API_KEY:", os.getenv('GOOGLE_SCHOLAR_API_KEY'))
    api_key = "ba06687d1ba3f435a9f46211b0ae5465e585a6d9b6237e093075cf8c617abaf6"
    if not api_key:
        raise Exception('No "GOOGLE_SCHOLAR_API_KEY" env var')

    # serp api properties
    params = {
        "engine": "google_scholar_author",
        "api_key": api_key,
        "num": 100,  # max allowed
    }

    # get id from entry
    _id = get_safe(entry, "gsid", "")
    if not _id:
        raise Exception('No "gsid" key')

    # query api
    @log_cache
    @cache.memoize(name=__file__, expire=1 * (60 * 60 * 24))
    def query(_id):
        params["author_id"] = _id
        return get_safe(GoogleSearch(params).get_dict(), "articles", [])

    response = query(_id)

    # list of sources to return
    sources = []

    # go through response and format sources
    for work in response:
        # create source
        year = get_safe(work, "year", "")
        source = {
            "id": get_safe(work, "citation_id", ""),
            # api does not provide Manubot-citeable id, so keep citation details
            "title": get_safe(work, "title", ""),
            "authors": list(map(str.strip, get_safe(work, "authors", "").split(","))),
            "publisher": get_safe(work, "publication", ""),
            "date": (year + "-01-01") if year else "",
            "link": get_safe(work, "link", ""),
        }

        # copy fields from entry to source
        source.update(entry)

        # add source to list
        sources.append(source)

    return sources
