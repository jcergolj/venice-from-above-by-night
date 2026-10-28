import json
from pathlib import Path
import unittest


THEME = Path(__file__).resolve().parents[1] / "opencode-theme.json"


def contrast(first, second):
    def luminance(colour):
        channels = [int(colour[i:i + 2], 16) / 255 for i in (1, 3, 5)]
        linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
        return sum(c * weight for c, weight in zip(linear, (0.2126, 0.7152, 0.0722)))

    low, high = sorted((luminance(first), luminance(second)))
    return (high + 0.05) / (low + 0.05)


class ThemeContrastTest(unittest.TestCase):
    def test_pasted_label_and_focused_actions_are_readable(self):
        base = json.loads(THEME.read_text())["base"]
        action = base["text"]["action"]["primary"]
        foreground = action.get("$focused", action["base"])
        # OpenCode renders extmark.paste with focused primary text on warning text colour.
        paste_background = base["text"]["feedback"]["warning"]["base"]
        background = base["background"]["action"]["primary"]
        focused_background = background.get("$focused", background["base"])
        for surface in (paste_background, focused_background):
            with self.subTest(background=surface):
                self.assertGreaterEqual(contrast(foreground, surface), 4.5)


if __name__ == "__main__":
    unittest.main()
