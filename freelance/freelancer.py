# # import json
# # import os



# # def freelancer_menu():
# #     while True:
# #         print(
# #             "Press 1 to see job posts \nPress 2 to search job posts by title\nPress 3 to see the result of your proposal\nPress 4 to logout")
# #         freelancer_option = int(input())

# #         if freelancer_option == 1:
# #             if os.path.exists("./posts.txt"):
# #                 with open("./posts.txt", "r") as f:
# #                     for post in f:
# #                         print(post)
# #                     choice = input("Send a request for the job you want by its id: ")
# #             else:
# #                 print("no posts available")
# #         elif freelancer_option == 2:
# #             keyword = input("Enter a title keyword to search for: ")
# #             with open("./posts.txt", "r") as f:
# #                 for post in f:
# #                     if keyword in post.split(',')[0]:
# #                         print(post)

# #         elif freelancer_option == 3:
# #             print("Displaying the result of your proposal")

# #         elif freelancer_option == 4:
# #             break
# #         else:
# #             print("Invalid option. Please enter a valid option.")








# # freelancer.py

# class Freelancer:
#     def __init__(self, user_id, name, email, password, phone_number, national_id):
#         self.user_id = user_id
#         self.name = name
#         self.email = email
#         self.password = password
#         self.phone_number = phone_number
#         self.national_id = national_id
#         self.proposals = []

#     def search_job_posts(self, title, job_posts):
#         return [job_post for job_post in job_posts if title.lower() in job_post.title.lower()]

#     def send_proposal(self, job_post, skill_name):
#         proposal = proposal(self, job_post, skill_name)
#         self.proposals.append(proposal)
#         return proposal





# freelancer.py

from proposal import Proposal

class Freelancer:
    def __init__(self, user_id, name, email, password, phone_number, national_id, **kwargs):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.national_id = national_id
        self.proposals = []

    def search_job_posts(self, title, job_posts):
        return [job_post for job_post in job_posts if title.lower() in job_post.title.lower()]

    def send_proposal(self, job_post, skill_name):
        proposal = Proposal(self, job_post, skill_name)
        self.proposals.append(proposal)
        return proposal
