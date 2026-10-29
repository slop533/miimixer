# Mii Mixer

Combine Wii Mii files (`.mii`, 74 bytes; `.rsd` 76 bytes also loads) into new amalgamations.
Pick how each part (face, hair, eyes, ...) is mixed: random, chaos, blend, or locked to one parent.
Shows renders of every parent and the result, and saves the result as `.mii` or `.rsd`.

Output filenames get a new version number each download (`Name_amalgam_v1.mii`, `_v2`, ...).

## Run it

Requires Python 3 and a browser with WebGL.

1. Get your own `FFLResHigh.dat` (from a Wii U: `sys/title/0005001b/10056000/content/FFLResHigh.dat`,
   or Miitomo's `AFLResHigh_2_3.dat` renamed). Put it in this folder, or use the Load button in the page.
2. Run `start.bat` (Windows) or `./start.sh` (Mac/Linux). First run downloads the renderer via `setup.py`.
3. Open http://localhost:8000/mii-mixer-v6-local.html

Use `serve.py`, not a plain `python -m http.server`: the renderer needs `SharedArrayBuffer`,
which needs the cross-origin isolation headers that `serve.py` sends.

Without `FFLResHigh.dat` the page still works and shows a simplified stylized drawing instead.

## Notes

- `FFLResHigh.dat` is Nintendo's data. It is **not** included, and `.gitignore` keeps it out of git. Don't commit it.
- Rendering uses [MiiJS](https://github.com/Stewared/MiiJS) (ISC) and FFL.js / FFL (AGPL-3.0, see `FFL_LICENSE`
  after setup). `setup.py` downloads them at a pinned commit; they are not stored in this repo.
- Wii format only (not 3DS/Wii U/Switch Miis).
- Mii and Wii are trademarks of Nintendo. This project is unofficial and not affiliated with Nintendo.

## License

MIT for the code in this repo (see `LICENSE`). Downloaded third-party components keep their own licenses.
