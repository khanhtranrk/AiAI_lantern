from typing import Optional
from .chatting.conosle import ConsoleChattingGUI

def create_chatting_gui(icebreaker: str, gui: Optional[str] = None):
    if gui is None:
        return ConsoleChattingGUI(icebreaker)
