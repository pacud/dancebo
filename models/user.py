# coding: utf8
from slugify import slugify


tmp_profile_pic = 'http://img15.hostingpics.net/pics/811484defaultavatar.png'
USER_LIST = [
    {
        'id': 1,
        'firstname': u'Coco',
        'lastname': u'Nut',
        'mobile': u'0612345789',
        'cart_paid': 1,
        'lessons_left': 5,
        'profile_pic': tmp_profile_pic,
        'medical_certificate': 0,
    },
    {
        'id': 2,
        'firstname': u'Pea',
        'lastname': u'Nut',
        'mobile': u'0123456789',
        'cart_paid': 1,
        'lessons_left': 2,
        'profile_pic': tmp_profile_pic,
        'medical_certificate': 1,
    },
    {
        'id': 3,
        'firstname': u'Wall',
        'lastname': u'Nut',
        'mobile': u'0033412356789',
        'cart_paid': 1,
        'lessons_left': 1,
        'profile_pic': tmp_profile_pic,
        'medical_certificate': 1,
    },
    {
        'id': 4,
        'firstname': u'Hairy',
        'lastname': u'Nut',
        'mobile': u'0712345689',
        'cart_paid': 0,
        'lessons_left': 0,
        'profile_pic': tmp_profile_pic,
        'medical_certificate': 1,
    },
]


class UserModel(object):

    def get_by_id(self, user_id):
        user = None
        for user in USER_LIST:
            if user['id'] == user_id:
                break
        return user

    def list(self):
        return USER_LIST

    def search(self, firstname, lastname):
        user_list = self.list()
        matches = []
        search_last = slugify(lastname)
        search_first = slugify(firstname)
        for user in user_list:
            user_last = slugify(user['lastname'])
            user_first = slugify(user['firstname'])
            if search_last == user_last and search_first == user_first:
                matches.append(user)
        return matches

    def add(self, title=None, firstname=None, lastname=None, profile_pic=None,
            birth_date=None, email=None, mobile=None, card_type=None,
            paiment_method=None, medical_certificate=None,
            inscription_paid=None, amount=None, origin=None,
            origin_other_social=None, origin_hearsay=None, origin_other=None,
            favorite_chanel=None):
        return {
            'title': title,
            'firstname': firstname,
            'lastname': lastname,
            'profile_pic': profile_pic,
            'birth_date': birth_date,
            'email': email,
            'mobile': mobile,
            'card_type': card_type,
            'paiment_method': paiment_method,
            'medical_certificate': medical_certificate,
            'inscription_paid': inscription_paid,
            'amount': amount,
            'origin': origin,
            'origin_other_social': origin_other_social,
            'origin_hearsay': origin_hearsay,
            'origin_other': origin_other,
            'favorite_chanel': favorite_chanel,
            'lessons_left': 0,
        }
