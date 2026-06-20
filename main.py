def on_forever():
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        """)
    basic.pause(300000)
    basic.show_leds("""
        . . # . .
        . # # # .
        # # # # #
        . # # # .
        . . # . .
        """)
    basic.pause(300000)
    basic.show_leds("""
        . . . . .
        . . # . .
        . # # # .
        . . # . .
        . . . . .
        """)
    basic.pause(300000)
basic.forever(on_forever)
