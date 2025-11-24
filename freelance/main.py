# import client
# import auth
# import freelancer

# def login_menu():
#         email = input("Enter your email: ").strip()
#         password = input("Enter your password: ")
#         result, user = auth.login(email, password)
#         if result:
#             if user[4] == "client":
#                 client.client_menu(user)
#             elif user[4] == "freelancer":
#                 freelancer.freelancer_menu()


# def registration_menu():
#         name = input("Enter your name: ").strip()
#         email = input('Enter your email: ').strip()
#         password = input("Enter your password: ").strip()
#         role = input("Enter your role: ").strip().lower()
#         if role == "client":
#             auth.register_client(name,email,password,role)
#         elif role == "freelancer":
#             phone_number = input("Enter your phone number: ")
#             national_id= input("Enter your national id: ")
#             auth.register_freelancer(name, email, password, role,phone_number,national_id)
#         else:
#             print("Invalid role")


# while True:
#         option = input("Press 1 to login\nPress 2 to register\nPress 0 to exit\n")
#         if option == '1':
#             login_menu()
#         elif option == '2':
#             registration_menu()
#         elif option == '0':
#             break

#         else:
#             print("Invalid option Please enter a valid option.")
















# main.py

from client import Client
from freelancer import Freelancer
from auth import login, register_client, register_freelancer

def main():
    while True:
        option = input("Press 1 to login\nPress 2 to register\nPress 0 to exit\n")
        if option == '1':
            email = input("Enter your email: ").strip()
            password = input("Enter your password: ")
            role = input("Enter your role (client/freelancer): ").strip().lower()

            if role == "client":
                result, user = login(email, password, Client)
                if result:
                    client_menu(user)
            elif role == "freelancer":
                result, user = login(email, password, Freelancer)
                if result:
                    freelancer_menu(user)
            else:
                print("Invalid role. Please enter 'client' or 'freelancer'.")

        elif option == '2':
            name = input("Enter your name: ").strip()
            email = input('Enter your email: ').strip()
            password = input("Enter your password: ").strip()
            role = input("Enter your role (client/freelancer): ").strip().lower()

            if role == "client":
                register_client(name, email, password)
            elif role == "freelancer":
                phone_number = input("Enter your phone number: ")
                national_id = input("Enter your national id: ")
                register_freelancer(name, email, password, phone_number, national_id)
            else:
                print("Invalid role. Please enter 'client' or 'freelancer'.")

        elif option == '0':
            break

        else:
            print("Invalid option. Please enter a valid option.")

def client_menu(client):
    while True:
        client_option = input(
            "Press 1 to view your profile\nPress 2 to add or delete job post\nPress 3 to see registered freelancers\nPress 0 to logout\n"
        )

        if client_option == '1':
            print(f"Id: {client.user_id}\nName: {client.name}\nEmail: {client.email}\nPassword: {client.password}")

        elif client_option == '2':
            x = input("Press 1 to add post\nPress 2 to delete\n")
            if x == '1':
                title = input("Title: ")
                job_description = input("Job Description: ")
                required_skills = input("Required Skills (comma separated): ").split(',')
                job_post = client.add_job_post(title, job_description, required_skills)
                print(f"Job post added with ID: {job_post.job_post_id}")

            elif x == '2':
                job_post_id = input("Enter job post ID to delete: ")
                job_post = next((post for post in client.job_posts if post.job_post_id == int(job_post_id)), None)
                if job_post:
                    client.remove_job_post(job_post)
                    print("Job post deleted successfully.")
                else:
                    print("Job post not found.")

            else:
                print("Invalid option. Please enter '1' or '2'.")

        elif client_option == '3':
            freelancers = client.list_freelancers()
            print("Registered Freelancers:")
            for freelancer in freelancers:
                print(f"Freelancer ID: {freelancer.user_id}, Name: {freelancer.name}")

        elif client_option == '0':
            break

        else:
            print("Invalid option. Please choose again.")

def freelancer_menu(freelancer):
    while True:
        freelancer_option = input(
            "Press 1 to see job posts \nPress 2 to search job posts by title\nPress 3 to see the result of your proposal\nPress 4 to logout\n"
        )

        if freelancer_option == '1':
            for job_post in freelancer.job_posts:
                print(f"Job Post ID: {job_post.job_post_id}, Title: {job_post.title}")

            job_post_id = input("Send a request for the job you want by its ID: ")
            job_post = next((post for post in freelancer.job_posts if post.job_post_id == int(job_post_id)), None)
            if job_post:
                skill_name = input("Enter the skill name you are perfect in: ")
                proposal = freelancer.send_proposal(job_post, skill_name)
                print(f"Proposal sent successfully. Proposal ID: {id(proposal)}")
            else:
                print("Job post not found.")

        elif freelancer_option == '2':
            title_keyword = input("Enter a title keyword to search for: ")
            matching_job_posts = freelancer.search_job_posts(title_keyword, freelancer.job_posts)
            for job_post in matching_job_posts:
                print(f"Job Post ID: {job_post.job_post_id}, Title: {job_post.title}")

        elif freelancer_option == '3':
            print("Displaying the result of your proposal")
            for proposal in freelancer.proposals:
                if proposal.accepted is not None:
                    status = "Accepted" if proposal.accepted else "Rejected"
                    print(f"Proposal ID: {id(proposal)}, Job Post ID: {proposal.job_post.job_post_id}, Status: {status}")

        elif freelancer_option == '4':
            break

        else:
            print("Invalid option. Please enter a valid option.")

if __name__ == "__main__":
    main()
