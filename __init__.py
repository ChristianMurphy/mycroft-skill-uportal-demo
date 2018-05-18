from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

class uPortalDemoSkill(MycroftSkill):
    def __init__(self):
        super(uPortalDemoSkill, self).__init__(name="uPortalDemoSkill")

    @intent_handler(IntentBuilder("").require("RequestMeal").require("Meals").optionally("TimeSpan"))
    def request_menu_intent(self, message):
        self.speak_dialog("todays.specials", data={"specials": "garden vegetable soup and grilled salmon salad"})

    @intent_handler(IntentBuilder("").require("RequestAssignment").require("Assignments").optionally("TimeSpan"))
    def request_assignment_intent(self, message):
        self.speak_dialog("due.soon", data={
            "timespan": "today",
            "type": "assignments",
            "assignments": "Literature review of Macbeth Act 1, Biology Lab 4, and Mathematics chapter 14 assessment"
        })

    @intent_handler(IntentBuilder("").require("RequestCourse").require("Course").optionally("TimeSpan"))
    def request_course_schedule_intent(self, message):
        self.speak_dialog("schedule", data={
            "timespan": "today",
            "courses": "this morning Biology Lab at 11, this afternoon Mathematics at 2 and Literature at 4"
        })

def create_skill():
    return uPortalDemoSkill()
