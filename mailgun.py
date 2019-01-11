import os
import requests
from jinja2 import FileSystemLoader, Environment, StrictUndefined
from jinja2.exceptions import TemplateNotFound
import requests
import json
import os
from datetime import datetime
from emails import emails

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
EMAIL_TEMPLATE_DIR = BASE_DIR

MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY", "")
MAILGUN_API_URL = os.environ.get("MAILGUN_API_URL",
                                 "https://api.mailgun.net/v3/mg.pycon.ng")

# moses context variable


def width_ratio(this_value, max_value, max_width):
    actual_value = (this_value / max_value) * max_width
    return int(round(actual_value))


def intcomma(number):
    new_number = "{:,.2f}".format(number)
    return new_number[:-2]


def pluralize(value):
    if value == 1:
        return ""
    return "s"


def render_from_template(**kwargs):
    loader = FileSystemLoader(BASE_DIR)
    env = Environment(loader=loader, undefined=StrictUndefined)
    # else:
    # full_email = "emails/%s" % template_name
    template = env.get_template("template.html")
    return template.render(**kwargs)


def get_mail_content(data):
    return {
        "html": render_from_template(),
        "text": render_from_template(),
        "subject": data["title"],
        "from": data.get("from_mail") or "PyconNG <hello@pycon.ng>",
        "to": data["to"],
        "bcc": data.get("bcc"),
    }


def mailgun_mailer(data, **kwargs):
    content = get_mail_content(data)
    files = None
    response = requests.post(
        MAILGUN_API_URL + "/messages",
        auth=("api", MAILGUN_API_KEY),
        data=content,
        files=files,
    )
    if response.status_code >= 400:
        import pdb
        pdb.set_trace()
        response.raise_for_status()
    print(response.json())


import csv
import itertools


def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


results = []
with open("py_slack.csv") as csvfile:
    files = csv.reader(csvfile)
    for o in files:
        if len(o) > 2:
            if o[2] != "Deactivated":
                results.append(o[1])
                # print(o[1])

for x, o in enumerate(grouper(200, emails)):
    list_ = ",".join([i for i in o if i and i != 'email'])
    print(list_)
    import pdb
    pdb.set_trace()
    mailgun_mailer({
        "title": "Share Your PyConNG2018 Experience...",
        "to": ["gbozee@gmail.com"],
        "bcc": list_,
    })
