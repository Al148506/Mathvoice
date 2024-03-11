init 999 python:
    renpy.display.screen.screens[("OLDchoice", None)] = renpy.display.screen.get_screen_variant("choice")
    renpy.display.screen.screens[("choice", None)] = renpy.display.screen.get_screen_variant("NEWchoice")

screen NEWchoice(*args, **kwargs):
    python:
        num = 0
        items = kwargs.get("items", ())
        for i in range(len(items)):
            if (num >= 9):
                break
            item = items[i]
            if not hasattr(item, 'kwargs'):
                item.kwargs = {}
            if not (
                item.kwargs.get("disabled", False) #ex: "menu text" (disabled=True):
                or "(disabled)" in item.caption #ex: "menu text (disabled)":
                or item.action == None
                or (hasattr(item.action, 'sensitive') and not item.action.sensitive) #ex: "menu text" if False:
            ):
                num += 1
                if not hasattr(item, 'menumod_processed'): #screen sometimes gets called about a dozen times? .. only change caption once
                    item.caption = str(num) + ") " + __(item.caption) # __() function translates to current language
                    item.menumod_processed = True
                    me = renpy.MenuEntry((item.caption, item.action, item.chosen)) # have to recreate ME because base unnamed args are immutable
                    for key, value in vars(item).items():
                        setattr(me, key, value)
                    item = items[i] = me
                renpy.ui.key(key="K_" + str(num), action=item.action) #number row
                renpy.ui.key(key="K_KP" + str(num), action=item.action) #numpad
    use OLDchoice(*args, **kwargs)
