#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from py_alarm.skeleton import fib
from py_alarm.clock import Clock

__author__ = "Olly Shaw"
__copyright__ = "Olly Shaw"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)

def test_should_tick_every_minute():
    clock = Clock()
    time = clock.sound("07:21")
    assert time == "tick"

def test_should_beep_every_hour():
    clock = Clock()
    time = clock.sound("21:00")
    assert time == "beep"

def test_should_wake_us_up_at_seven():
    clock = Clock()
    time = clock.sound("07:00")
    assert time == "wake up!"