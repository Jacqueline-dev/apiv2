from typing import Any, Dict, List

import tweepy

from src.connection import trends_collection
from src.secrets import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET
from src.constantes import BRAZIL_WOE_ID


def _get_trends(woe_id: int) -> List[Dict[str, Any]]:
    """Get treending topics from Twitter API.

    Args:
        woe_id (int): Identifier of location.

    Returns:
        List[Dict[str, Any]]: Trends list.
    """

    auth = tweepy.OAuth1UserHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)

    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    trends = api.trends_place(woe_id)

    print(trends)

    return trends[0]["trends"]


def get_trends_from_mongo() -> List[Dict[str, Any]]:
    trends = trends_collection.find({})
    return list(trends)


def save_trands() -> None:
    trends = _get_trends(woe_id=BRAZIL_WOE_ID)
    trends_collection.insert_many(trends)
