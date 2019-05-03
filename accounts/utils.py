import json

#from steem import Steem
from app import settings

from beem import Steem
from beem.account import Account
from beem.comment import Comment

def get_user_vops(username):
    stm = Steem("https://steemd.privex.io")
    acc = Account(username, steem_instance=stm)
    return acc.virtual_op_count()

def get_user_posts(username, from_id, limit=100):
    stm = Steem("https://steemd.privex.io")
    acc = Account(username, steem_instance=stm)

    blog_entries = acc.get_blog_entries(
        from_id,
        limit
    )

    entries_list = []

    for entry in blog_entries:
        if username == entry['author']:
            comment = Comment("@" + entry['author'] + "/" + entry['permlink'])
            entry_dict = {
                'id': comment.id,
                'title': comment.title,
                'clickable': 'https://www.steemit.com/{0}/@{1}/{2}'.format(
                    comment.category,
                    comment.author,
                    comment.permlink,
                ),
                'url': '/{0}/@{1}/{2}'.format(
                    comment.category,
                    comment.author,
                    comment.permlink,
                ),
                'author': comment.author,
                'category': comment.category,
                'tags': comment.json_metadata['tags'],
                'entry_id': entry['entry_id']
            }

            if 'images' in comment.json_metadata:
                entry_dict['images'] = comment.json_metadata['images']
            entries_list.append(entry_dict)

    return entries_list

def get_user_history(username, start, stop):
    stm = Steem("https://steemd.privex.io")
    acc = Account(username, steem_instance=stm)

    entries_list = []
    for c in acc.history_reverse(start=start, stop=stop, use_block_num=False, only_ops=["comment"]):
        if c['parent_author'] == '':
            entry_dict = {
                'id': c['trx_id'],
                'title': c['title'],
                'clickable': 'https://www.steemit.com/{0}/@{1}/{2}'.format(
                    c['parent_permlink'],
                    c['author'],
                    c['permlink'],
                ),
                'url': '/{0}/@{1}/{2}'.format(
                    c['parent_permlink'],
                    c['author'],
                    c['permlink'],
                ),
                'author': c['author'],
                'category': c['parent_permlink'],
                'tags': json.loads(c['json_metadata'])['tags'],
                'entry_id': c['index']
            }
            entries_list.append(entry_dict)
    return entries_list