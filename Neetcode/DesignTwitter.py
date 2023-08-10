class Twitter:

    def __init__(self):
        self.userFollows = dict()
        self.userPosts = dict()
        self.postTime = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follow(userId, userId)
        self.userPosts[userId].append((self.postTime, tweetId))
        self.postTime -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follow(userId, userId)
        posts = list()
        for user in self.userFollows[userId]:
            for post in self.userPosts[user]:
                posts.append(post)
        heapq.heapify(posts)
        feed = list()
        while posts and len(feed) < 10:
            feed.append(heapq.heappop(posts)[1])
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        
        if followerId not in self.userFollows:
            self.userFollows[followerId] = set({followerId})
            self.userPosts[followerId] = list()

        if followeeId not in self.userFollows:
            self.userFollows[followeeId] = set({followeeId})
            self.userPosts[followeeId] = list()
        
        self.userFollows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        if followerId != followeeId:
            if followerId in self.userFollows:
                if followeeId in self.userFollows[followerId]:
                    self.userFollows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
