from django.core.mail import send_mail
from django.conf import settings
from django_cron import CronJobBase, Schedule
import requests
from agent import process_incidents
from pymongo import MongoClient
import json



process_incidents()

