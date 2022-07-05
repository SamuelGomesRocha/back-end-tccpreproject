import tweepy as tw
import pandas as pd
import json


auth = tw.OAuthHandler("<consumer_key>", "<consumer_secret>")
auth.set_access_token("<token_key>", "<token_secret>")
api = tw.API(auth)

def getProfileTweets(query):
    print("Olha a query: "+query)
    cursor_tweets = api.user_timeline(screen_name="@"+query, count=20, include_rts=True)
    tweets = []
    for tweet in cursor_tweets:
       tweets.append(tweet._json)
    interactions = []
    for j in tweets:
        #j = i._json
        interactions = interactions + [
            {'id': j.get('id'), 'qtd_likes': j.get('favorite_count'), 'verify_rt_comment': j.get('retweet_count'),
             'verify_mentions': verifyMentions(j), 'mentioned_user': getMentions(j),
             'verify_reply': verifyReply(j),
             'destinatary_id': j.get('in_reply_to_user_id'), 'destinatary_screen_name': getDestinatary(j),
             'hashtags': getHashtags(j), 'text': (j.get('text')).lower()}]
    return interactions;

#Verifica que existem menções
def verifyMentions(j):
 verifyMentions = False
 if (j.get('entities').get('user_mentions')):
    verifyMentions = True
 return verifyMentions


def getMentions(j):
 if verifyMentions(j):
  destinataries_list = []
  detailed_destinataries_list = j.get('entities').get('user_mentions')
  for d in detailed_destinataries_list:
    destinataries_list.append(d['screen_name'])
  return destinataries_list
 return ''


def getDestinatary(j):
  if(j.get('in_reply_to_screen_name')):
    return j.get('in_reply_to_screen_name')
  return ''

def verifyReply(j):
  if(getDestinatary(j) != ''):
    return True
  return False

#Obtém as hashtags contidas num tweet
def getHashtags(j):
  if j.get('entities').get('hashtags'):
    hashtags_list = []
    detailed_hashtags_list = j.get('entities').get('hashtags')
    for h in detailed_hashtags_list:
      hashtags_list.append(('#'+h['text']).lower())
    return hashtags_list
  return ''

def obtemTrendTopics():
    trend_topics = []
    BRAZIL_WOE_ID = 23424768
    brazilian_trends = api.get_place_trends(BRAZIL_WOE_ID)
    trends = json.loads(json.dumps(brazilian_trends, indent=1))
    for trend in trends[0]['trends']:
        trend_topics.append({'trend': trend['name']})
    return trend_topics

def obtemTrendTopicsELinks():
    trend_topics = []
    BRAZIL_WOE_ID = 23424768
    brazilian_trends = api.get_place_trends(BRAZIL_WOE_ID)
    trends = json.loads(json.dumps(brazilian_trends, indent=1))
    for trend in trends[0]['trends']:
        trend_topics.append({'trend': trend['name'], 'link': trend['url'], 'qtd': trend['tweet_volume']})
    return trend_topics