import json
import functools
from loguru import logger

from config import user_client, data


def get_users_group(group_list):
    '''
    Get all members from a group and save in a json file.
    '''
    def _get_groups(archived=False):
        '''
        Get all dialogs from a client
        '''
        with user_client as client:
            all_dialogs = client.get_dialogs(limit=None, archived=archived)

        return {dialog.name: dialog for dialog in all_dialogs if dialog.is_group}

    def _get_all_members(group):
        '''
        Get all users from a group.
        '''
        with user_client as client:
            all_members = client.get_participants(
                group,
                aggressive=True
            )
        all_members = [
            {
                'name': member.username,
                'id': member.id,
                'full_name': f'{member.first_name} {member.last_name or ""}'
            }
            for member in all_members
            if not member.bot
            ]
        return all_members

    for group_name in group_list:
        groups = _get_groups()
        group = groups.get(group_name)
        if not group:
            group = _get_groups(archived=True).get(group_name)

        users = _get_all_members(group.id) or _get_all_members(group_name)
        logger.info(f'{group_name}: {len(users)} listed users (bots not included)')
        with open(f'{group_name}.users.json', 'w') as json_file:
            json.dump(users, json_file)


def restricted(func):
    '''
    This decorator allows you to restrict the access of a handler
    to only the 'user_ids' specified in data['groups']['restricted'].
    '''
    @functools.wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        user_id = update.effective_user.id
        chat_title = update.effective_chat.title
        if chat_title and chat_title not in data['groups']['names']:
            logger.warning(f"Unauthorized use in {chat_title} group.")
            return
        if user_id not in data['groups']['restricted']:
            logger.warning(f'Unauthorized access denied for {user_id}')
            return
        logger.info(f'Authorized user: {user_id}')
        return func(bot, update, *args, **kwargs)
    return wrapped
