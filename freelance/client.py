# # import os
# # import json
# # import auth




# # def post(Title, job, description, required_skills):
# #     posts = []
# #     if os.path.exists("posts.txt"):
# #         with open("posts.txt", "r") as f:
# #             posts = json.load(f)

# #     posts_id = len(posts) + 1
# #     new_post = {"id": posts_id, "Title": Title, "job": job, "description": description,
# #                 "required_skills": required_skills}
# #     posts.append(new_post)

# #     with open("posts.txt", "w") as f:
# #         json.dump(posts, f,indent=2)
# # def client_menu(user):
# #     while True:
# #         client_option = int(input("press 1 to view your profile\npress 2 to add or delete job post\npress 3 to see registered freelancers\npress 0 to logout\n"))
# #         if client_option==1:
# #             with open('clients.txt', 'r') as f:
# #                 client = json.load(f)
# #                 user_id= user[0]
# #                 name = user[1]
# #                 email = user[2]
# #                 password = user[3]
# #                 print("Id:", user_id)
# #                 print("Name:", name)
# #                 print("Email:", email)
# #                 print("Password:", password)

# #         elif client_option == 2:
# #             x=int(input("press 1 to add post\npress 2 to delete\n"))
# #             if x== 1:
# #                 Title = input("Title: ")
# #                 job = input("Job: ")
# #                 description = input("Description: ")
# #                 required_skills = input("Required Skills: ")
# #                 post(Title, job, description, required_skills)

# #             elif x==2:
# #                 pass


# #             else:
# #                 print("invalid option please (1-2)")

# #         elif client_option == 3:
# #             pass
# #             # with open("./freelancers.txt", "r") as f:
# #             #     users = json.load(f)
# #             #     for user in users:
# #             #         if 'name' in user:
# #             #             modified_name = user['name'][:3] + user['name'][4:]
# #             #             user['name'] = modified_name
# #             #             print(user)
# #         # elif client_option == 3:
# #         #     with open("./freelancers.txt","r")as f:
# #         #         users=json.load(f)
# #         #         for user in users:
# #         #             print(user[:3]+user[5:])

# #         elif client_option ==0:
# #             break

# #         else:
# #             print("Invalid option. Please choose again.")










# # client.py

# class Client:
#     def __init__(self, user_id, name, email, password):
#         self.user_id = user_id
#         self.name = name
#         self.email = email
#         self.password = password
#         self.job_posts = []

#     def add_job_post(self, title, job_description, required_skills):
#         job_post_id = len(self.job_posts) + 1
#         job_post = job_post(job_post_id, title, job_description, required_skills)
#         self.job_posts.append(job_post)
#         return job_post

#     def remove_job_post(self, job_post):
#         self.job_posts.remove(job_post)

#     def list_freelancers(self):
#         freelancers = []
#         for job_post in self.job_posts:
#             freelancers.extend(job_post.get_proposal_freelancers())
#         return list(set(freelancers))

#     def process_proposal(self, freelancer, job_post, accept=True):
#         if accept:
#             job_post.accept_proposal(freelancer)
#         else:
#             job_post.reject_proposal(freelancer)





# client.py

from job_post import JobPost

class Client:
    def __init__(self, user_id, name, email, password, **kwargs):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.job_posts = []

    def add_job_post(self, title, job_description, required_skills):
        job_post_id = len(self.job_posts) + 1
        job_post = JobPost(job_post_id, title, job_description, required_skills)
        self.job_posts.append(job_post)
        return job_post

    def remove_job_post(self, job_post):
        self.job_posts.remove(job_post)

    def list_freelancers(self):
        freelancers = []
        for job_post in self.job_posts:
            freelancers.extend(job_post.get_proposal_freelancers())
        return list(set(freelancers))

    def process_proposal(self, freelancer, job_post, accept=True):
        if accept:
            job_post.accept_proposal(freelancer)
        else:
            job_post.reject_proposal(freelancer)
