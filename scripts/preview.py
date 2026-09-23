"""Build in an ASCII temporary directory to support Windows Unicode project paths."""
import argparse
import functools
import http.server
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser(description="Build and preview this academic homepage.")
    parser.add_argument("--port", type=int, default=4000)
    parser.add_argument("--build-only", action="store_true")
    args = parser.parse_args()
    project = Path(__file__).resolve().parent.parent
    temp = Path(tempfile.gettempdir())
    ruby_path = shutil.which("ruby")
    portable = temp / "academic-homepage-runtime/rubyinstaller-3.3.12-1-x64/bin/ruby.exe"
    if not ruby_path and portable.is_file():
        ruby_path = str(portable)
    if not ruby_path:
        raise SystemExit("Ruby is required. Install Ruby 3.3 with Devkit: https://rubyinstaller.org/downloads/")
    ruby = Path(ruby_path).resolve()
    bundle = ruby.parent / "bundle"
    if not bundle.is_file():
        raise SystemExit("Bundler is required. Run: gem install bundler")
    env = os.environ.copy()
    env["PATH"] = str(ruby.parent) + os.pathsep + env.get("PATH", "")
    env["BUNDLE_PATH"] = str(temp / "academic-homepage-build/vendor/bundle")
    env["JEKYLL_ENV"] = "development"
    portable_devkit = temp / "academic-homepage-build-tools/msys64"
    if portable_devkit.is_dir() and not env.get("MSYS2_PATH"):
        env["MSYS2_PATH"] = str(portable_devkit)
    build = Path(tempfile.mkdtemp(prefix="academic-homepage-preview-"))
    ignored = {".git", ".bundle", ".jekyll-cache", "_site", "vendor", "node_modules", "docs", ".tools", "__pycache__"}
    for source in project.iterdir():
        if source.name in ignored or source.name.startswith(".env"):
            continue
        destination = build / source.name
        if source.is_dir():
            shutil.copytree(source, destination, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        else:
            shutil.copy2(source, destination)
    command = [str(ruby), str(bundle)]
    def run(arguments):
        subprocess.run(command + arguments, cwd=build, env=env, check=True)
    if subprocess.run(command + ["check"], cwd=build, env=env).returncode:
        run(["install"])
    run(["exec", "jekyll", "build"])
    subprocess.run([os.sys.executable, str(project / "scripts/check_site.py"), str(build / "_site")], check=True)
    if args.build_only:
        print("Built site:", build / "_site")
        return
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(build / "_site"))
    with http.server.ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
        print(f"Preview: http://127.0.0.1:{args.port}/", flush=True)
        print("Restart this command after editing the source. Press Ctrl+C to stop.", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as error:
        raise SystemExit(f"Build failed (exit {error.returncode}). See the output above.")
