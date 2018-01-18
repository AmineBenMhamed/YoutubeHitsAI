# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

import subprocess
import random

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'Amine'

LOGGER = getLogger(__name__)


class YoutubeHitsSkill(MycroftSkill):
    def __init__(self):
        super(YoutubeHitsSkill, self).__init__(name="YoutubeHitsSkill")
        self.process = None

    def initialize(self):
        #self.load_data_files(dirname(__file__))
        youtube_skills_intent = IntentBuilder("YoutubeHitsIntent"). \
            require("YoutubeSkillsKeyword").build()
        self.register_intent(youtube_skills_intent, self.handle_youtube_hits_intent)



    def handle_youtube_hits_intent(self, message):

        vid = ["https://www.youtube.com/watch?v=3k4oS0-jnl8","https://www.youtube.com/watch?v=NlsF1dWT30I" ,"https://www.youtube.com/watch?v=a4BWBmFA8xk"]
        self.process = subprocess.Popen(["mpv",random.choice(vid)] )




    def stop(self):
        pass


def create_skill():
    return YoutubeHitsSkill()
