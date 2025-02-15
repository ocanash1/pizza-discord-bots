import random
import csv
from datetime import datetime
from constants import AVATAR_CSV_FILE, THRESHOLD, WELCOME_MSGS, JOIN_DA_MAFIA_CHAN_ID


def get_member_data(member):
    """ id,name,nickname,created_at,joined_at,roles,top_role,avatar_url """
    data = [member.id, member.name,  member.nick, member.created_at]
    data.append(member.joined_at if member.joined_at is not None else "")
    data.append("|".join(list(map(lambda role: role.name, member.roles)))
                if member.roles is not None else "")
    data.append(member.top_role if member.top_role is not None else "")
    data.append(member.avatar_url if member.avatar is not None else "")
    return data


def generate_welcome_message(username):
    return WELCOME_MSGS[random.randint(0, len(WELCOME_MSGS)-1)].format(username=username)


def create_csv_file(data, filename=AVATAR_CSV_FILE):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    return


def time_exceeded(last, now=datetime.now()):
    """ calculates the time difference (in hours) since a new member joined.
    returns true if that time difference is greater than THRESHOLD """

    hours = (now - last).total_seconds() / (60 * 60)
    return (hours >= THRESHOLD)
