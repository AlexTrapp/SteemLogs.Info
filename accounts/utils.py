import json

#from steem import Steem
from app import settings

from beem import Steem
from beem.account import Account
from beem.comment import Comment


def get_user_posts(username, from_id, limit=100):
    stm = Steem(node='https://rpc.usesteem.com/')
    acc = Account(username, steem_instance=stm)

    blog_entries = acc.get_blog_entries(
        from_id,
        limit
    )

    entries_list = []

    for entry in blog_entries:
        # Could be util to load posts on utopian directly.
        # parent_permlink = comment.get('permlink')

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
