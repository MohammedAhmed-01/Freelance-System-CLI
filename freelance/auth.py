# import os
# import json
# import client
# import freelancer
# def register_client(name, email, password, role):
#     if os.path.exists("./clients.txt"):
#         with open("./clients.txt", "r") as file:
#             clients = json.load(file)
#             for user in clients:
#                 if user[2] == email:
#                     print("Email already exists")
#                     return

#         user_id = clients[-1][0]+1
#         clients.append([user_id, name, email, password, role])

#         with open("./clients.txt", "w") as f:
#             json.dump(clients, f)
#     else:
#         clients = [[1,name, email, password, role]]
#         with open("./clients.txt", "x") as f:
#             json.dump(clients, f)
# # def register_client(name, email, password, role):
# #     if os.path.exists("./clients.txt"):
# #         with open("./clients.txt", "r") as f:
# #             clients = json.load(f)
# #
# #         for user in clients:
# #             if user[1] == email and user[2] == password:
# #                 print("Account already exists")
# #                 return
# #
# #         user_id = clients[-1][0]+1
# #         clients.append([user_id, name, email, password, role])
# #         with open("./clients.txt", "w") as f:
# #             json.dump(clients, f,indent=2)


# def register_freelancer(name, email, password,role,phone_number,national_id):
#     if os.path.exists("./freelancers.txt"):
#         with open("./freelancers.txt", "r") as f:
#             freelancers = json.load(f)
#             for user in freelancers:
#                 if user[2] == email:
#                     print("Account already exists")
#                     return

#         user_id = freelancers[-1][0]+1
#         freelancers.append(user_id, name, email, password,role,phone_number,national_id)
#         with open("./freelancers.txt", "w") as f:
#             json.dump(freelancers, f)
#     else:
#         freelancers = [[1, name,email,password,role,phone_number,national_id]]
#         with open("./freelancers.txt", "x") as f:
#             json.dump(freelancers, f)
# def login(email, password):
#     if os.path.exists("./clients.txt"):
#         with open("./clients.txt", "r") as f:
#             clients = json.load(f)
#             for user in clients:
#                 if user[2]== email and user[3] == password:
#                     return True, user

#     if os.path.exists("./freelancers.txt"):
#         with open("./freelancers.txt", "r") as f:
#             freelancers = json.load(f)
#             for user in freelancers:
#                 if user[2]== email and user[3]==password:
#                     return True, user

#     print("Wrong email or password")
#     return False, []





# auth.py

import os
import json
from client import Client
from freelancer import Freelancer

def load_users(file_path, user_class):
    users = []
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            users_data = json.load(file)
            for user_data in users_data:
                user = user_class(**user_data)
                users.append(user)
    return users

def save_users(file_path, users):
    users_data = []
    for user in users:
        user_data = vars(user).copy()
        users_data.append(user_data)

    with open(file_path, "w") as file:
        json.dump(users_data, file, indent=2)

def register_client(name, email, password):
    clients = load_users("clients.txt", Client)
    for user in clients:
        if user.email == email:
            print("Email already exists")
            return

    user_id = len(clients) + 1
    client = Client(user_id, name, email, password)
    clients.append(client)

    save_users("clients.txt", clients)

def register_freelancer(name, email, password, phone_number, national_id):
    freelancers = load_users("freelancers.txt", Freelancer)
    for user in freelancers:
        if user.email == email:
            print("Email already exists")
            return

    user_id = len(freelancers) + 1
    freelancer = Freelancer(user_id, name, email, password, phone_number, national_id)
    freelancers.append(freelancer)

    save_users("freelancers.txt", freelancers)

def login(email, password, user_class):
    users = load_users(f"{user_class.__name__.lower()}s.txt", user_class)
    for user in users:
        if user.email == email and user.password == password:
            return True, user
    print("Wrong email or password")
    return False, None
