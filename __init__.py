from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

class uPortalDemoSkill(MycroftSkill):
    def __init__(self):
        super(uPortalDemoSkill, self).__init__(name="uPortalDemoSkill")
        self.count = 0

    @intent_handler(IntentBuilder("").require("Hello").require("World"))
    def handle_hello_world_intent(self, message):
        self.speak_dialog("hello.world")

    @intent_handler(IntentBuilder("").require("Count").require("Dir"))
    def handle_count_intent(self, message):
        if message.data["Dir"] == "up":
            self.count += 1
        else:  # assume "down"
            self.count -= 1
        self.speak_dialog("count.is.now", data={"count": self.count})

def create_skill():
    return uPortalDemoSkill()
