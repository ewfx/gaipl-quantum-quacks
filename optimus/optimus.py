from django.core.mail import send_mail
from django.conf import settings
from django_cron import CronJobBase, Schedule
import requests
from agent import process_incidents
from pymongo import MongoClient
import json


# # ServiceNow API credentials
# SERVICENOW_INSTANCE = "dev305595.service-now.com"
# SERVICENOW_USERNAME = "admin"
# SERVICENOW_PASSWORD = "pu!ycN3Q7/XX"


# def fetch_unassigned_incidents():
#     url = f"https://{SERVICENOW_INSTANCE}/api/now/table/incident?sysparm_query=state=1^assigned_toISEMPTY"
#     response = requests.get(url, auth=(SERVICENOW_USERNAME, SERVICENOW_PASSWORD), headers={"Accept": "application/json"})
#     return response.json().get("result", []) if response.status_code == 200 else []

# def getAgentDetails(assignment_group):
#     client = MongoClient("mongodb+srv://quantam:admin@cluster0.87zbx.mongodb.net/")
#     db = client["platformManager"]
#     collection = db["assignmentGroup"]
#     assignment_doc = collection.find_one({"_id": "assignment_mapping"})
#     if assignment_doc:
#         assignmentGroupInfo = assignment_doc["mappings"].get(assignment_group, {})
#         return assignmentGroupInfo
#     return {}

# def sendToAgent(assignment_group,incidentNumber,priority,shortDescription,longDescription,comments):
#     agentDetails=getAgentDetails(assignment_group)
#     agentUrl=agentDetails.get("restURL")
#     agentMail=agentDetails.get("mailId")
#     print(agentUrl)
#     print(agentMail)
#     print(incidentNumber)
#     print(priority)
#     print(shortDescription)
#     print(longDescription)
#     print(comments)

# def assign_incident(incident_sys_id, assignment_group, assigned_to):
#     url = f"https://{SERVICENOW_INSTANCE}/api/now/table/incident/{incident_sys_id}"
#     payload = {"assigned_to": assigned_to, "state": 2}  # 2 -> Assigned
#     requests.patch(url, auth=(SERVICENOW_USERNAME, SERVICENOW_PASSWORD), json=payload, headers={"Content-Type": "application/json"})


# def getAssignementGroup(url):
#     response = requests.get(url, auth=(SERVICENOW_USERNAME, SERVICENOW_PASSWORD), headers={"Accept": "application/json"})
#     return response.json().get("result", []).get("name") if response.status_code == 200 else []

# def send_email():
#     print("Hi")

# def process_incidents():
#     incidents = fetch_unassigned_incidents()
#     for incident in incidents:
#         assignmentGroupDetail = incident.get("assignment_group",{})
#         incidentNumber=incident.get("number",{})
#         priority=incident.get("priority",{})
#         shortDescription=incident.get("short_description",{})
#         longDescription=incident.get("description",{})
#         comments=incident.get("comments",{})

#         if(isinstance(assignmentGroupDetail,dict)):
#             assignment_group_link = assignmentGroupDetail.get("link")
#             assignmentGroup=getAssignementGroup(assignment_group_link)
#             sendToAgent(assignmentGroup,incidentNumber,priority,shortDescription,longDescription,comments)
        
#         # assigned_to = ASSIGNMENT_MAPPING.get(assignment_group)
#         # if assigned_to:
#         #     assign_incident(incident["sys_id"], assignment_group, assigned_to)
#         # send_email()


# def check_resolved_incidents():
#     url = f"https://{SERVICENOW_INSTANCE}/api/now/table/incident?sysparm_query=state=6"
#     response = requests.get(url, auth=(SERVICENOW_USERNAME, SERVICENOW_PASSWORD), headers={"Accept": "application/json"})
#     incidents = response.json().get("result", []) if response.status_code == 200 else []
#     # for incident in incidents:
#     #     send_email()



process_incidents()

