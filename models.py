from collections import defaultdict
from random import randint, shuffle
# from decorators import property_required


colors = {
    'yellow': {
        'house_price': 150,
        'num_properties': 3,
    }
}

"""
    rents: contains an array with all the possibles rents:
            - Initial rent:
            - 1 House 1
            - 2 Houses
            - 3 Houses
            - 4 Houses
            - Hotel
"""
properties = {
    'atlantico': {
        'color': 'yellow',
        'name': 'Av. Atlantico',
        'price': 160,
        'rent': 25,
        'rents': [25, 120, 240, 360, 480, 650],
    },
    'marvin': {
        'color': 'yellow',
        'name': 'Jardines Marvin',
        'price': 180,
        'rents': [26, 120, 240, 360, 480, 650],
    },
    'ventnor': {
        'color': 'yellow',
        'name': 'Av. Ventnor',
        'price': 160,
        'rents': [26, 120, 240, 360, 480, 650],
    },
}


class Player(object):
    def __init__(self, name, initial_wage=1500):
        self.name = name
        self.properties = {}
        self.wage = initial_wage
        self.color_properties = defaultdict(list)
        self.position = 0

    def take_off_money(self, amount):
        if amount > self.wage:
            raise(BaseException("Not enough wage."))
        self.wage -= amount
        return self.wage

    def __get_initial_property(self, sproperty):
        mproperty = properties.get(sproperty, None)
        if not mproperty:
            raise(BaseException("Property not found."))
        if sproperty in self.properties.keys():
            raise(BaseException("Property already added."))
        self.take_off_money(mproperty['price'])
        property_color = mproperty['color']
        self.color_properties[property_color].append(sproperty)
        self.properties[sproperty] = {
            'rent': properties[sproperty]['rents'][0],
            'rent_i': 0,
        }
        if self.has_all_color_properties(sproperty):
            for mproperty in self.color_properties[property_color]:
                self.properties[mproperty]['rent'] *= 2

    def has_all_color_properties(self, sproperty):
        mproperty = properties.get(sproperty, None)
        if not property:
            return False
        property_color = mproperty['color']
        return len(self.color_properties[property_color]) >= colors[
            mproperty['color']]['num_properties']

    def can_add_house(self, sproperty):
        rent_i = self.properties[sproperty]['rent_i']
        return len(properties[sproperty]['rents']) > rent_i + 1

    def buy_property(self, sproperty):
        properties[sproperty]
        self.__get_initial_property(sproperty)

    def add_house(self, sproperty):
        if sproperty not in self.properties.keys():
            raise(BaseException("Property not found."))
        if not self.has_all_color_properties(sproperty):
            raise(BaseException("You don't have all the color properties."))
        if not self.can_add_house(sproperty):
            raise(BaseException("Impossible to add more houses."))
        mproperty = properties.get(sproperty, None)
        self.take_off_money(colors[mproperty['color']]['house_price'])
        self.properties[sproperty]['rent_i'] += 1
        rent_i = self.properties[sproperty]['rent_i']
        self.properties[sproperty]['rent'] = properties[
            sproperty]['rents'][rent_i]

    def put_money(self, amount):
        self.wage += amount

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '%s - M/ %.2f - [%s]' % (
            self.name, self.wage, ', '.join(self.properties))


class Game(object):
    num_dices = 2
    TYPE_PROPERTY = 'property'
    TYPE_ACTION = 'action'
    STATUS_AVAILABLE = 'available'
    STATUS_PURCHASED = 'purchased'
    BANK = 'bank'
    players = {}
    properties = properties.keys()
    distribution = [
        # Go 0
        'mediterraneo',
        # Arca 2
        'baltica',
        # Impuestos 4
        'f_reading',
        'oriental',
        # Fortuna 7
        'vermont',
        'connecticut',
        # Visita en la carcel 10
        'san_carlos',
        's_luz',
        'estados',
        'virginia',
        'f_penssylvania',
        'st_james',
        # Arca 17
        'tenesse',
        'nueva_york',
        # Parada Libre 20
        'kentucky',
        # Fortuna 22
        'indiana',
        'illinois',
        'f_B&O',
        'atlantico',
        'ventnor',
        's_agua',
        'marvin',
        # Carcel 30
        'pacifico',
        'carolina_norte',
        # Arca 33
        'penssylvania',
        'f_via_rapida',
        # Fortuna 36
        'plaza_parque',
        # Impuesto 38
        'el_muelle'
    ]
    player_distribution = ()

    def __fill_board(self):
        self.distribution.insert(0, 'go')
        self.board['go'] = {
            'type': self.TYPE_ACTION,
            'foo': lambda x: x,
        }
        self.distribution.insert(2, 'arca_2')
        self.board['arca_2'] = {
            'type': self.TYPE_ACTION,
            'foo': lambda x: x,
        }
        self.distribution.insert(4, 'impuestos_4')
        self.board['impuestos_4'] = {
            'type': self.TYPE_ACTION,
            'foo': lambda x: x,
        }
        self.distribution.insert(7, 'fortuna_7')
        self.board['fortuna_7'] = {
            'type': self.TYPE_ACTION,
            'foo': lambda x: x,
        }
        self.distribution.insert(10, 'visita_10')
        self.board['visita_10'] = {
            'type': self.TYPE_ACTION,
            'foo': lambda x: x,
        }
        self.distribution.insert(17, 'arca_17')
        self.board['arca_17'] = {
            'type': self.TYPE_ACTION,
            'foo': lambda x: x,
        }
        self.distribution.insert(20, 'stop_20')
        self.board['stop_20'] = {
            'type': self.TYPE_ACTION,
            'foo': lambda x: x,
        }
        self.distribution.insert(22, 'fortuna_22')
        self.board['fortuna_22'] = {
            'type': self.TYPE_ACTION,
            'foo': lambda x: x,
        }
        self.distribution.insert(30, 'carcel_30')
        self.board['carcel_30'] = {
            'type': self.TYPE_ACTION,
            'foo': lambda x: x,
        }
        self.distribution.insert(33, 'arca_33')
        self.board['fortuna_33'] = {
            'type': self.TYPE_ACTION,
            'foo': lambda x: x,
        }
        self.distribution.insert(36, 'fortuna_36')
        self.board['fortuna_36'] = {
            'type': self.TYPE_ACTION,
            'foo': lambda x: x,
        }
        self.distribution.insert(38, 'impuestos_38')
        self.board['impuestos_38'] = {
            'type': self.TYPE_ACTION,
            'foo': lambda x: x,
        }

    def __init__(self, *args, **kw):
        self.initial_wage = kw.get('initial_wage', 1500)
        self.double_go = kw.get('double_go', False)
        self.board = {
            sproperty: {
                'type': self.TYPE_PROPERTY,
                'status': self.STATUS_AVAILABLE,
                'owner': self.BANK
            } for sproperty in self.properties
        }
        self.__fill_board()

    def add_player(self, name):
        player = self.players.get(name, '')
        if player or name == self.BANK:
            raise(BaseException('Player with name %s already exists' % name))
        player = Player(name, self.initial_wage)
        self.players[name] = player
        return player

    def buy_property(self, sproperty, player):
        mproperty = self.board[sproperty]
        if not mproperty['type'] == self.TYPE_PROPERTY:
            raise BaseException("%s is not a property." % sproperty)
        if mproperty['owner'] != self.BANK:
            raise BaseException("%s has already purchased by %s." % (
                sproperty, mproperty['owner']))
        if self.players[player.name] != player:
            raise BaseException(
                "%s is not part of this game." % player.name)
        player.buy_property(sproperty)
        mproperty['owner'] = player.name
        mproperty['status'] = self.STATUS_PURCHASED


class LocalGame(Game):
    def launch_dices(self):
        return [randint(1, 6) for i in xrange(self.num_dices)]


class AutomaticGame(Game):
    # Implemente movements, and plays, such as pays and charges
    o_players = []

    def start_game(self):
        if len(self.players.keys()) == len(self.o_players):
            return
        self.o_players = self.players.keys()
        shuffle(self.o_players)
        print '---->', self.o_players

    def run_simulation(self):
        self.start_game()
        # print self.distribution
        for splayer in self.o_players:
            self.move(splayer)
            # print splayer

    def move(self, player):
        dices = self.launch_dices()
        sum_dices = [i for i in dices]
        # current_position = player.position
        print sum_dices

        # num_repeated = 0
        # play_again = True if dices[0] == dices[1] else False
