#! /usr/bin/python
from pushbullet import Pushbullet
pb = Pushbullet('o.1LLpJVStlbb4i7EgT9fgKeVWdJUCI4rM')
push = pb.push_note("Webfaro Spento!", "Hei ciao, il Webfaro e' spento, ha bisogno della tua assistenza, YEAH!")
