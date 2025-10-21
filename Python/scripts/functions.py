def lighten_color(color, intensity):
    intensity += 1
    r, g, b = color
    r = min(int(r * intensity), 255)
    g = min(int(g * intensity), 255)
    b = min(int(b * intensity), 255)

    return (r, g, b)

def blit_render_multiline(x, y, font, text, antialiasing, color, surface, x_align, y_align):
    lines = text.split("\n")

    for line in lines:
        render_line = font.render(line, antialiasing, color)

        # set alignment
        match x_align:  # L (left), M (middle), R (right)
            case "M": xa = x - render_line.get_width() / 2
            case "R": xa = x - render_line.get_width()
            case _: xa = x
        match y_align:  # T (top), M (middle), B (bottom)
            case "M": ya = y - render_line.get_height() / 2
            case "B": ya = y - render_line.get_height()
            case _: ya = y

        surface.blit(render_line, (xa, ya))
        y += render_line.get_height()