# # job_post.py

# class JobPost:
#     def __init__(self, job_post_id, title, job_description, required_skills):
#         self.job_post_id = job_post_id
#         self.title = title
#         self.job_description = job_description
#         self.required_skills = required_skills
#         self.proposals = []

#     def get_proposal_freelancers(self):
#         return [proposal.freelancer for proposal in self.proposals]

#     def accept_proposal(self, freelancer):
#         for proposal in self.proposals:
#             if proposal.freelancer == freelancer:
#                 proposal.accepted = True

#     def reject_proposal(self, freelancer):
#         for proposal in self.proposals:
#             if proposal.freelancer == freelancer:
#                 proposal.accepted = False






# job_post.py
from proposal import Proposal

class JobPost:
    def __init__(self, job_post_id, title, job_description, required_skills):
        self.job_post_id = job_post_id
        self.title = title
        self.job_description = job_description
        self.required_skills = required_skills
        self.proposals = []

    def get_proposal_freelancers(self):
        return [proposal.freelancer for proposal in self.proposals]

    def accept_proposal(self, freelancer):
        for proposal in self.proposals:
            if proposal.freelancer == freelancer:
                proposal.accepted = True

    def reject_proposal(self, freelancer):
        for proposal in self.proposals:
            if proposal.freelancer == freelancer:
                proposal.accepted = False
