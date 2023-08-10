class Twitter:

    def __init__(self):
        self.followed_by = dict()
        self.user_feed = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follow(userId, userId)
        for user in self.followed_by[userId]:
            self.user_feed[user].append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = 0
        i = len(self.user_feed[userId]) - 1
        ans = list()
        while i > -1 and feed < 10:
            if self.user_feed[userId][0] in self.followed_by[userId]:
                ans.append(self.user_feed[userId][1])
                feed += 1
            i -= 1
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        
        if followerId not in self.followed_by:
            self.followed_by[followerId] = set({followerId})
        if followeeId not in self.followed_by:
            self.followed_by[followeeId] = set({followeeId})
        
        self.followed_by[followeeId].add(followerId)
        
        if followerId not in self.user_feed:
            self.user_feed[followerId] = list()
        if followeeId not in self.user_feed:
            self.user_feed[followeeId] = list()

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followeeId in self.followed_by:
                if followerId in self.followed_by[followeeId]:
                    self.followed_by[followeeId].remove(followerId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
