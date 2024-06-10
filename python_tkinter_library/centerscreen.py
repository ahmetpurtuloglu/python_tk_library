def center_screen_geometry(screen_width, screen_height, window_width, window_height):
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    return f"{window_width}x{window_height}+{x}+{y}"
