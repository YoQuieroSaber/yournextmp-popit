from candidates.static_data import (
    BaseMapItData, BasePartyData, BaseAreaPostData
)


class MapItData(BaseMapItData):
    pass


class PartyData(BasePartyData):

    def __init__(self):
        super(PartyData, self).__init__()
        self.ALL_PARTY_SETS = (
            {'slug': 'nacionale', 'name': 'Nacionale'},
        )

    def party_data_to_party_sets(self, party_data):
        return ['nacionale']


class AreaPostData(BaseAreaPostData):

    def __init__(self, *args, **kwargs):
        super(AreaPostData, self).__init__(*args, **kwargs)
        self.ALL_POSSIBLE_POST_GROUPS = [None]

    def area_to_post_group(self, area_data):
        return None

    def post_id_to_party_set(self, post_id):
        return 'nacionale'

    def post_id_to_post_group(self, election, post_id):
        return None

    def shorten_post_label(self, election, post_label):
        return post_label

    def party_to_possible_post_groups(self, party_data):
        return (None,)
