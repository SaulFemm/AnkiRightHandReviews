# Austin Hasten
# Initial Commit - January 13th, 2018
# License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>

from anki.hooks import wrap
from aqt.reviewer import Reviewer

from .config import local_conf

def newShortcutKeys(self, _old):
    return _old(self) + [
        (local_conf["ans_1"], lambda: self._answerCard(1)),
        (local_conf["ans_2"], lambda: self._answerCard(2)),
        (local_conf["ans_3"], lambda: self._answerCard(3)),
        (local_conf["ans_4"], lambda: self._answerCard(4)),
    ]

def newAnswerCard(self, ease, _old):
    if local_conf["silly_mode"]:
        if self.state == "question":
            self.state = 'answer'
    if local_conf["conflate_ease"]:
        _old(self, min(self.mw.col.sched.answerButtons(self.card), ease))
    else:
        _old(self, ease)

Reviewer._shortcutKeys = wrap(Reviewer._shortcutKeys, newShortcutKeys, "around")
if local_conf["silly_mode"] or local_conf["conflate_ease"]:
    Reviewer._answerCard = wrap(Reviewer._answerCard, newAnswerCard, "around")
