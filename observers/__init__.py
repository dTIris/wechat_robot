# -*- coding:utf-8 -*-

from observers.rule import Rule
from observers.configure import Configure
from observers.record import Record
from observers.shop import Shop
from observers.follow import Follow
from observers.user_data import UserData
from observers.task import Task
from observers.clock import Clock
from observers.main_menu import MainMenu
from observers.informer import Informer


informer = Informer()
main_menu = MainMenu(informer.register)
clock = Clock(informer.register)
task = Task(informer.register)
record = Record(informer.register)
user_data = UserData(informer.register)
rule = Rule(informer.register)
shop = Shop(informer.register)
configure = Configure(informer.register)

follow = Follow(informer.register)

