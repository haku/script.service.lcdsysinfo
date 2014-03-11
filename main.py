# http://wiki.xbmc.org/index.php?title=Add-on_structure
# http://wiki.xbmc.org/index.php?title=Python_development
# http://wiki.xbmc.org/index.php?title=HOW-TO_write_Python_Scripts
# http://romanvm.github.io/xbmcstubs/docs/classxbmc_1_1_player.html
# http://wiki.xbmc.org/?title=InfoLabels

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
from pylcdsysinfo import LCDSysInfo, TextLines, BackgroundColours, TextColours

bg = BackgroundColours.BLACK
fg = TextColours.GREEN

d = LCDSysInfo()
d.clear_lines(TextLines.ALL, bg)
d.dim_when_idle(False)
d.set_brightness(127)
d.save_brightness(127, 255)
d.set_text_background_colour(bg)

def draw_lines(lines, first = 0):
  for i in range(0, (6 - first)):
    d.clear_lines(1 << (first + i), bg)
    if i < len(lines):
      d.display_text_on_line(1 + first + i, lines[i], False, None, fg)

draw_lines(['starting desu ...'])

p = xbmc.Player()

def draw_time():
  line = str(datetime.timedelta(seconds=int(p.getTime()))) \
      + ' of ' \
      + str(datetime.timedelta(seconds=int(p.getTotalTime())))
  d.display_text_on_line(1, line, False, None, fg)

while (not xbmc.abortRequested):
  last_title = None
  while 1:
    title = xbmc.getInfoLabel('Player.Title') if p.isPlaying() else 'stopped desu.'
    if title != last_title:
      last_title = title
      draw_lines(textwrap.wrap(title, 23), (1 if p.isPlaying() else 0))
    if p.isPlaying():
      draw_time()
    time.sleep(1)

draw_lines(['shutdown desu.'])
