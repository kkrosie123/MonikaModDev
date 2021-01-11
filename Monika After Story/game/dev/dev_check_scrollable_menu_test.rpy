
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="dev_check_scrollable_menu_test",
            category=["dev"],
            prompt="TEST CHECK SCROLLABLE MENU",
            pool=True,
            unlocked=True
        )
    )

label dev_check_scrollable_menu_test:
    show monika 3eua t11 zorder MAS_MONIKA_Z with dissolve

    $ checked_buttons = store.mas_utils.tryparseint(
        renpy.input(
            "How many {b}checked{/b} buttons would you like in the menu?",
            allow=numbers_only,
            length=2
        ).strip("\t\n\r"),
        0
    )

    $ unchecked_buttons = store.mas_utils.tryparseint(
        renpy.input(
            "How many {b}unchecked{/b} buttons would you like in the menu?",
            allow=numbers_only,
            length=2
        ).strip("\t\n\r"),
        0
    )

    if not checked_buttons and not unchecked_buttons:
        m 2rksdla "I can't build a menu w/o buttons."
        return

    m 1eub "Would you like the menu to return the items with true values, or any items?{nw}"
    $ _history_list.pop()
    menu:
        m "Would you like the menu to return the items with true values, or any items?{fast}"

        "Only with true values":
            $ return_all = False

        "Any":
            $ return_all = True

    m 1eua "Shall we use True or False as the true value?{nw}"
    $ _history_list.pop()
    menu:
        m "Shall we use True or False as the true value?{fast}"

        "Use True":
            $ true_value = True

        "Use False":
            $ true_value = False

    python:
        false_value = not true_value
        items = []
        i = 0

        while checked_buttons + unchecked_buttons > 0:
            i += 1
            if (
                checked_buttons > 0
                and (
                    unchecked_buttons == 0
                    or renpy.random.randint(0, 1) == 1
                )
            ):
                checked_buttons -= 1
                items.append(
                    ("Button #{0}".format(i), "button_#_{0}".format(i), True, true_value, false_value)
                )

            else:
                unchecked_buttons -= 1
                items.append(
                    ("Button #{0}".format(i), "button_#_{0}".format(i), False, true_value, false_value)
                )

    call screen mas_check_scrollable_menu(items, mas_ui.SCROLLABLE_MENU_AREA, mas_ui.SCROLLABLE_MENU_XALIGN, return_button_prompt="Finish test", return_all=return_all)

    if _return:
        $ result = str(_return).replace("{", "{{")
        m 1dsa "And this's what we got from the menu.{w=0.2}.{w=0.2}.{w=0.2}{nw}"
        m 4eua "[result]"

    else:
        m 4eub "The menu returned an empty dict."

    return
