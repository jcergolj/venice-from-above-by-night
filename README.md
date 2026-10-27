# Venice From Above by Night

A warm dark adaptation of [Venice From Above](https://github.com/mattbbia/venice-from-above) by [Matt (@mattbbia)](https://github.com/mattbbia), for Omarchy.

The original theme's Renaissance character and six Venice wallpapers are preserved, with warm near-black surfaces, parchment text, aged-gold and olive accents, and muted colours for code and feedback.

## Acknowledgements

- **Original theme:** [Venice From Above by Matt](https://github.com/mattbbia/venice-from-above), MIT licensed; copyright retained in [LICENSE](LICENSE).
- **Artwork:** Jacopo de' Barbari's *View of Venice* (1500), public domain per upstream, with images credited to the [National Gallery of Art](https://www.nga.gov/).
- **Dark adaptation:** [@jcergolj](https://github.com/jcergolj).

Independent adaptation; wallpapers unchanged.

## Install

For Omarchy versions supporting `colors.toml`:

```bash
omarchy theme install https://github.com/jcergolj/venice-from-above-by-night.git
omarchy theme set venice-from-above-by-night
```

Omarchy generates application colour configurations from the palette. This repository does not carry over the original light theme's application-specific configurations.

## Palette

| Role | Colour |
| --- | --- |
| Background | `#181715` |
| Raised background | `#2b2823` |
| Text | `#f0e8da` |
| Secondary text | `#bfb3a0` |
| Accent | `#bdb087` |
| Selection | `#443d32` |
| Terracotta | `#cb8978` |
| Olive | `#a3ad86` |
| Lagoon | `#88b3ab` |
| Blue | `#91aabd` |

## OpenCode V2

A matching explicit theme is included to avoid dependence on terminal palette detection. Omarchy installation does not activate it automatically.

After installing the Omarchy theme:

```bash
mkdir -p ~/.config/opencode/themes
cp ~/.config/omarchy/themes/venice-from-above-by-night/opencode-theme.json \
  ~/.config/opencode/themes/venice-from-above-by-night.json
```

Merge the following into `~/.config/opencode/cli.json`, preserving your other settings:

```json
{
  "theme": {
    "name": "venice-from-above-by-night",
    "mode": "dark"
  }
}
```

Open a new OpenCode instance after installing the theme file. Alternatively, use `/themes` to select it once discovered.

## Wallpapers

All six wallpapers are the original, unmodified artwork crops; “by Night” describes the interface palette, not altered artwork.

| | |
| --- | --- |
| ![View of Venice 1](backgrounds/View%20of%20Venice%20%231%201500.jpg) | ![View of Venice 2](backgrounds/View%20of%20Venice%20%232%201500.jpg) |
| ![View of Venice 3](backgrounds/View%20of%20Venice%20%233%201500.jpg) | ![View of Venice 4](backgrounds/View%20of%20Venice%20%234%201500.jpg) |
| ![View of Venice 5](backgrounds/View%20of%20Venice%20%235%201500.jpg) | ![View of Venice 6](backgrounds/View%20of%20Venice%20%236%201500.jpg) |

## License

Theme code is provided under the [MIT License](LICENSE), preserving the original author's copyright notice. The historical artwork is public domain, as documented by the upstream project.
