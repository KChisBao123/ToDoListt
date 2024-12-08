import os
from win32api import GetSystemMetrics

WINDOW_WIDTH            = 500
WINDOW_HEIGHT           = 740
WINDOW_POSITION_RIGHT   = int(GetSystemMetrics(0)/2 - WINDOW_WIDTH/2)
WINDOW_POSITION_DOWN    = int(GetSystemMetrics(1)/2 - WINDOW_HEIGHT/2)

SCROLL_FRAME_WIDTH      = 434
SCROLL_FRAME_HEIGHT     = 512

COLOR_BACKGROUND        = "#FCE8E8"
COLOR_HEX               = "#CF9C9C"
COLOR_WHITE             = "#FFFAFA"
COLOR_ORGANRE           = "#DE6723"
COLOR_GREY              = "#958E8B"
COLOR_GREEN             = "#81AD4E"

PATH_DIRECTORY          = os.path.dirname(__file__)
PATH_IMAGES             = os.path.join(PATH_DIRECTORY, 'image')
PATH_ICON_TASK      = os.path.join(PATH_IMAGES, 'task.png')
PATH_ICON_DELETE        = os.path.join(PATH_IMAGES, 'delete.png')
PATH_ICON_TOPBAR       = os.path.join(PATH_IMAGES, 'topbar.png')
PATH_ICON_DOCK       = os.path.join(PATH_IMAGES, 'dock.png')

FONT_STATUS             = ('Roboto', 20,'bold')
FONT_ORDER_TASK         = ('Roboto', 16,'bold')
FONT_INPUT_TASK         = ('Roboto', 18,'normal')
FONT_NAME_TASK_LINE     = ('Roboto', 16,'normal', 'overstrike')
FONT_NAME_TASK_NO_LINE  = ('Roboto', 16,'normal')