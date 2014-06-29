import os

def get_short_path(cwd):
    home = os.getenv('HOME')
    names = cwd.split(os.sep)
    if names[0] == '': names = names[1:]
    path = ''
    for i in range(len(names)):
        path += os.sep + names[i]
        if os.path.samefile(path, home):
            return ['~'] + names[i+1:]
    if not names[0]:
        return ['/']
    return names

def add_cwd_segment():
    cwd = powerline.cwd or os.getenv('PWD')
    names = os.path.join(*(get_short_path(cwd.decode('utf-8'))))
    bg = Color.CMD_PASSED_BG
    fg = Color.CMD_PASSED_FG
    if powerline.args.prev_error != 0:
        fg = Color.CMD_FAILED_FG
        bg = Color.CMD_FAILED_BG
    powerline.append(' %s ' % names, fg, bg)
    
'''
    max_depth = powerline.args.cwd_max_depth
    if len(names) > max_depth:
        names = names[:2] + [u'\u2026'] + names[2 - max_depth:]
    if not powerline.args.cwd_only:
        for n in names[:-1]:
            if n == '~' and Color.HOME_SPECIAL_DISPLAY:
                powerline.append(' %s ' % n, Color.HOME_FG, Color.HOME_BG)
            else:
                powerline.append(' %s ' % n, Color.PATH_FG, Color.PATH_BG,
                    powerline.separator_thin, Color.SEPARATOR_FG)

    if names[-1] == '~' and Color.HOME_SPECIAL_DISPLAY:
        powerline.append(' %s ' % names[-1], Color.HOME_FG, Color.HOME_BG)
    else:
        powerline.append(' %s ' % names[-1], Color.CWD_FG, Color.PATH_BG)
'''
add_cwd_segment()
