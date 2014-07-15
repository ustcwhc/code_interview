#!/user/bin/python
# filename: chapter7.py

import random
import os
import sys

# PROBLEM 7.1
# Design the data structures for a generic deck of cards. Explain how you
# would subclass it to implement particular card games
class Card(object):
    def __init__(self, point, suit):
        self.point = point
        self.Suit = suit
        self.Power = point

class DeckOfCards(object):
    def __init__(self):
        self._cards = []
        for i in range(4):
            for v in range(1, 14):
                self._cards.append(Card(v, i))
        # add jokers
        self._cards.append(Card(15, -1))
        self._cards.append(Card(16, -1))


    def add_more_cards(self, deckOfCards):
        for card in deckOfCards._cards:
            self._cards.append(card)

    def shuffule(self):
        new_cards = []
        while len(self._cards) > 0:
            index = random.randint(0, len(self._cards) - 1)
            new_cards.append(self._cards.pop(index))
        self._cards = new_cards

    def del_card(self, card_player):
        pass


class LeadCards(object):
    def __init__(self, cards):
        self._cards = cards
        self.Power = self.get_power()

    def get_power(self):
        return 0

class CardPlayer(object):
    def __init__(self, name):
        self.Name = name
        self._cards = []

    def receive_card(self, card):
        self._cards.append(card)

    def lead_cards(self, selected_cards, former_lead=None):
        my_lead = LeadCards(selected_cards)
        if not former_lead or my_lead.Power > former_lead.Power:
            for card in selected_cards:
                self._cards.remove(card)
            return my_lead
        else:
            raise Exception('Your cards are not larger than former lead')


# PROBLEM 7.2
# Three level of employees, multi freshers, on technical lead (TL),
# one product manager (PM)
# An incoming call need to allocate a fresher who is free
# If fresher is not able to answer, give it to free TL or PM
class Employee(object):
    def __init__(self, name):
        self.Name = name
        self.Subordinates = None
        self.Boss = None
        self.Peers = None
        self.Available = True

    def set_boss(self, boss):
        self.Boss = boss

    def set_subordinates(self, subordinates):
        self.Subordinates = subordinates

    def answer_call(self):
        self.Available = False

    def finish_call(self):
        self.Available = True


class Fresher(object):
    def __init__(self, name):
        Employee.__init__(self, name)

    def set_boss(self, boss):
        if not boss:
            raise Exception('Fresher does not have boss')
        if type(boss) != TechnicalLead:
            raise Exception('Fresher\'s boss is not TechnicalLead')
        Employee.set_boss(self, boss)

    def set_subordinates(self, subordinates):
        if subordinates and len(subordinates) > 0:
            raise Exception('Freshers cannot have subordinates')
        Employee.set_subordinates(self, subordinates)


class TechnicalLead(object):
    def __init__(self, name):
        Employee.__init__(self, name)

    def set_boss(self, boss):
        if not boss:
            raise Exception('TL does not have boss')
        if type(boss) != ProductManager:
            raise Exception('TL\'s boss is not PM')
        Employee.set_boss(self, boss)

    def set_subordinates(self, subordinates):
        if not subordinates:
            raise Exception('Technical Lead does not have freshers for subordinates')
        else:
            for subordinate in subordinates:
                if type(subordinate) != Fresher:
                    raise Exception('Technical lead can only have freshers as subordinates')
        Employee.set_subordinates(self, subordinates)

class ProductManager(object):
    def __init__(self, name):
        Employee.__init__(self, name)

    def set_boss(self, boss):
        if boss:
            raise Exception('Product manager cannot have boss')
        Employee.set_boss(self, boss)

    def set_subordinates(self, subordinates):
        if not subordinates or len(subordinates) > 0:
            raise Exception('Product manager does not have a subordinate')
        elif len(subordinates) > 1:
            raise Exception('Product manager cannot have multi subordinates')
        elif type(subordinates[0]) != TechnicalLead:
            raise Exception('Product manager can only have technical lead as subordinate')
        Employee.set_subordinates(self, subordinates)


class CallCenter(object):
    def __init__(self, fresher_n):
        # initial fresher
        self.FresherEmployees = []
        for i in range(fresher_n):
            self.FresherEmployees.append(Fresher('Fresher' + str(i + 1)))

        # initial TL
        self.TechnicalLead = TechnicalLead('Technical Lead')

        # initial PM
        self.ProductManager = ProductManager('Product Manager')

        # set boss
        for fresher in self.FresherEmployees:
            fresher.set_boss(self.TechnicalLead)
        self.TechnicalLead.set_boss(self.ProductManager)

        # set subordinates
        self.TechnicalLead.set_subordinates(self.FresherEmployees)
        self.ProductManager.set_subordinates([self.TechnicalLead])

    def get_call_handler(self):
        for fresher in self.FresherEmployees:
            if fresher.Available:
                fresher.answer_call()
                return True

        if self.TechnicalLead.Available:
            self.TechnicalLead.answer_call()
            return True

        if self.ProductManager.Available:
            self.ProductManager.answer_call()
            return True

        return False


# PROBLEM 7.3
# Design a musical juke box using object oriented principles
class Music(object):
    def __init__(self, music_file):
        self.music_file = music_file

    def is_valid_music(self):
        return self.music_file[-3:] == 'mp3'

class Player(object):
    def __init__(self):
        self.cur_music = None

    def set_music(self, music):
        self.cur_music = music

    def play(self):
        pass

    def pause(self):
        pass


class MusicList(object):
    def __init__(self):
        self.__musics = []
        self.__selected_music = None

    def add_music_file(self, music_file):
        music = Music(music_file)
        if music.is_valid_music():
            self.__musics.append(music)

    def add_music_files(self, music_files):
        for music_file in music_files:
            self.add_music_file(music_file)

    def add_music_folder(self, music_folder):
        music_files = []
        for dir, dir_names, file_names in os.walk(music_folder):
            for file_name in file_names:
                music_files.append(os.path.join(dir, file_name))

        self.load_music_files(music_files)

    def get_select_music(self):
        return self.__selected_music

    def set_selected_music(self, index):
        if index >= 0 and index < len(self.__musics):
            self.__selected_music = self.__musics[index]
        else:
            self.__selected_music = None


class MusicBox(object):
    def __init__(self):
        self.__player = Player()
        self.__music_list = MusicList()

    def play(self):
        music = self.__music_list.get_select_music()
        if music:
            self.__player.set_music(music)


# PROBLEM 7.4
# Design a chess game using object oriented principles
class Chessman(object):
    def __init__(self, value, x, y):
        self.Value = value
        self.X = x
        self.Y = y
        self.Player = None

    def move(self, target_x, target_y):
        if self.is_valid_move(target_x, target_y):
            self.X = target_x
            self.Y = target_y

    # this function has to be override in the subclass
    def is_valid_move(self, target_x, target_y):
        return False


class Chessman_King(object):
    def __init__(self, value, x, y):
        Chessman.__init__(self, value, x, y)


class ChessPlayer(object):
    def __init__(self, name):
        self.Name = name
        self.Chessmen = []

    def set_chessmen(self, chessmen):
        self.Chessmen = chessmen
        for chessman in chessmen:
            chessman.Player = self

    def get_chessman(self, x, y):
        for chessman in self.Chessmen:
            if chessman.X == x and chessman.Y == y:
                return chessman
        return None

    def move(self, x, y, target_x, target_y, opponent):
        # get original chessman
        chessman = self.get_chessman(x, y)
        if not chessman:
            return False

        # check whether there is already a chessman of his own
        target_chessman = self.get_chessman(target_x, target_y)
        if target_chessman and target_chessman.Player == self:
            return False

        if chessman.move(target_x, target_y, opponent):
            opponent_chessman = opponent.get_chessman(target_x, target_y)
            if opponent_chessman:
                opponent.remove(opponent_chessman)

    def concede(self):
        pass

    def remove(self, chessman):
        self.Chessmen.remove(chessman)
        if type(chessman) == Chessman_King:
            self.concede()
