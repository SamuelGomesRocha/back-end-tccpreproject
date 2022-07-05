class Tweet:

    def __init__(self, id, qtd_likes, verify_rt_comment, verify_mentions, mentioned_user, verify_reply,
                 destinatary_id, destinatary_screen_name, hashtags, text):
        self.id = id
        self.qtd_likes = qtd_likes
        self.verify_rt_comment = verify_rt_comment
        self.verify_mentions = verify_mentions
        self.mentioned_user = mentioned_user
        self.verify_reply = verify_reply
        self.destinatary_id = destinatary_id
        self.destinatary_screen_name = destinatary_screen_name
        self.hashtags = hashtags
        self.text = text
