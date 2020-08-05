import sys
import os

sys.path.append(os.path.realpath('.'))

import string
import random

from thebookofinternet import db
from thebookofinternet.models import Post

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

db.create_all()

for i in range(100):
    db.session.add(
        Post(
            title=get_random_string(10),
            username=get_random_string(random.randint(0, 40)),
            post=get_random_string(random.randint(1, 500))
        )
    )

db.session.commit()
