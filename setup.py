"""Downloads the MiiJS browser build (MiiJS + FFL.js renderer) next to the page.
Nothing from it is stored in this repo; it is fetched from the MiiJS project at a pinned commit."""
import io, os, sys, urllib.request, zipfile

COMMIT = "de10c3c5237fbf18da88ac860f5c0ac7ad1a3b4b"
URL = f"https://raw.githubusercontent.com/Stewared/MiiJS/{COMMIT}/browserBuild.zip"
HERE = os.path.dirname(os.path.abspath(__file__))

if os.path.exists(os.path.join(HERE, "fflModule.cjs")) and "--force" not in sys.argv:
    print("MiiJS build already present (use --force to re-download).")
    sys.exit(0)

print("Downloading MiiJS browser build...")
data = urllib.request.urlopen(URL, timeout=60).read()
with zipfile.ZipFile(io.BytesIO(data)) as z:
    for name in z.namelist():
        if name.endswith(".map") or name == "README.md" or name.endswith("/"):
            continue
        z.extract(name, HERE)
print("Done. Now put your own FFLResHigh.dat in this folder (or use the Load button in the page).")
