class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Ben")
user_2 = User("002", "Claire")

print(user_1.username.followers)
print(user_2.username)
user_1.follower(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)