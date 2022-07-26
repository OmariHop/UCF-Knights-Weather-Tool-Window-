import tweepy 


apiKey = "HAMhYljqGFEnGeAuSX8WC82wW"
apiKeySecret = "Kg7RhJeq3iHzJtyX4n2HiXfiPNDoDVSP1T7jn4XTrbm3n5VlpS"
accessSecretToken = "oFKkJRwXYfSn5DQZ8kFWGIdCoOX5efPEKIGQPrVEILQF3"
accessToken = "1459343145867620353-BgWKfCDR6gauwPU5h9tBJXdhvZi20s"

authenticator = tweepy.OAuthHandler(apiKey, apiKeySecret)
authenticator.set_access_token(accessToken, accessSecretToken)

api = tweepy.API(authenticator, wait_on_rate_limit=True)


user = api.get_user("UCF")
user_tweets = api.user_timeline(user_id = user.id)

for tweets in user_tweets:
    if not tweets.favorited:
        api.create_favorite(tweets.id)

