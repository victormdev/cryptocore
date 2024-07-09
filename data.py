import os
import sys
import time
#import json
sys.path.append(
    os.path.join(os.path.dirname(__file__), 'groupmesagebot')
)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "groupmesagebot.settings")
import django
django.setup()

from django.conf import settings
from django.core import exceptions
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta

from main.models import Course,Question,Text
from django.utils import timezone

from datetime import datetime, timedelta
import random






def get_topic(topic_id):
    topic = Course.objects.get(id=topic_id)
    return topic

def get_text():
    text = Text.objects.last()
    return text

def get_all_topic():
    all_topic = Course.objects.all()
    return all_topic

def get_question(question_id):
    question = Question.objects.get(id=question_id)
    return question


def get_user(userid):
    try:
        user = BotUser.objects.get(userid=userid)
    except BotUser.DoesNotExist:
        user = None
    return user