#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# GuessIt - A library for guessing information from filenames
# Copyright (c) 2012 Nicolas Wack <wackou@gmail.com>
#
# GuessIt is free software; you can redistribute it and/or modify it under
# the terms of the Lesser GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# GuessIt is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Lesser GNU General Public License for more details.
#
# You should have received a copy of the Lesser GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import unicode_literals
from guessittest import *

IGNORE_EPISODES = [ 'finale ' ]
IGNORE_MOVIES = []

class TestAutoDetectAll(TestGuessit):
    def testAutoMatcher(self):
        self.checkMinimumFieldsCorrect(filetype='autodetect',
                                       filename='autodetect.yaml',
                                       remove_type=False)

    def testAutoMatcherMovies(self):
        self.checkMinimumFieldsCorrect(filetype='autodetect',
                                       filename='movies.yaml',
                                       exclude_files=IGNORE_MOVIES)

    def testAutoMatcherEpisodes(self):
        self.checkMinimumFieldsCorrect(filetype='autodetect',
                                       filename='episodes.yaml',
                                       exclude_files=IGNORE_EPISODES)


suite = allTests(TestAutoDetectAll)

if __name__ == '__main__':
    TextTestRunner(verbosity=2).run(suite)
