import hashlib
import os

files_to_cache = [
    "index.html",
    "jb.html",
    "core.js",
    "jb.js",
    "mem.js",
    "int64.js",
    "ps4_offsets.js",
    "rpc_worker.js",
    "PSCLINIC.png",
    "goldhen.bin",
    "payload2.bin",
    "patches/1100.bin",
    "patches/1150.bin",
    "patches/1200.bin",
    "patches/1250.bin",
    "patches/1300.bin",
]

print("CACHE MANIFEST")
print(f"# build {hashlib.sha256(str(os.urandom(8)).encode()).hexdigest()[:13]}\n")

for f in files_to_cache:
    if os.path.exists(f):
        hasher = hashlib.sha256()
        with open(f, "rb") as afile:
            buf = afile.read()
            hasher.update(buf)
        print(f"{f} #{hasher.hexdigest()}")
    else:
        print(f"# Missing: {f}")

print("\nNETWORK:\n*")