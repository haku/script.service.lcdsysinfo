# http://wiki.xbmc.org/index.php?title=Add-on_structure
# http://wiki.xbmc.org/index.php?title=Python_development
# http://wiki.xbmc.org/index.php?title=HOW-TO_write_Python_Scripts
# http://romanvm.github.io/xbmcstubs/docs/classxbmc_1_1_player.html

import os
import time
import datetime
import xbmc
import xbmcaddon
import textwrap

__settings__ = xbmcaddon.Addon(id='script.service.lcdsysinfo')
__cwd__ = __settings__.getAddonInfo('path')
BASE_RESOURCE_PATH = xbmc.translatePath(os.path.join( __cwd__, 'resources', 'lib'))
sys.path.append (BASE_RESOURCE_PATH)
from pylcdsysinfo import LCDSysInfo, TextLines, TextLines, BackgroundColours, TextColours

bg = BackgroundColours.BLACK
fg = TextColours.GREEN

d = LCDSysInfo()
d.clear_lines(TextLines.ALL, bg)
d.dim_when_idle(False)
d.set_brightness(127)
d.save_brightness(127, 255)
d.set_text_background_colour(bg)

d.display_text_on_line(1, "starting desu~ ...", False, None, fg)

p = xbmc.Player()

while (not xbmc.abortRequested):
  while 1:
    if p.isPlaying():
      line1 = "Playing desu~"
      line2 = str(datetime.timedelta(seconds=int(p.getTime()))) \
          + " of " \
          + str(datetime.timedelta(seconds=int(p.getTotalTime())))
      title_lines = textwrap.wrap(p.getPlayingFile(), 23)
      line3 = title_lines[0] if len(title_lines) >= 1 else ""
      line4 = title_lines[1] if len(title_lines) >= 2 else ""
      line5 = title_lines[2] if len(title_lines) >= 3 else ""
      line6 = title_lines[3] if len(title_lines) >= 4 else ""
    else:
      line1 = "stopped desu~"
      line2 = ""
      line3 = ""
      line4 = ""
      line5 = ""
      line6 = ""

    d.display_text_on_line(1, line1, False, None, fg)
    d.display_text_on_line(2, line2, False, None, fg)
    d.display_text_on_line(3, line3, False, None, fg)
    d.display_text_on_line(4, line4, False, None, fg)
    d.display_text_on_line(5, line5, False, None, fg)
    d.display_text_on_line(6, line6, False, None, fg)
    time.sleep(1)

d.display_text_on_line(1, "shutdown desu~", False, None, fg)
