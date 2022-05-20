class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # print("new user being created...")
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# user_1 = User()  # here is where the print statement gets triggered in the class.
# user_1.id = "001"
user_1 = User("001","gogulan")
# user_1.username = "gogulan"

# print(user_1.username)
# print(user_1.id)
# print(user_1.username)
# print(user_1.followers)

# user_2 = User()
# user_2.id = "002"
# user_2.name = "jack"
user_2 = User("002", "jack")


user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)