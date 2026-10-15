#!/usr/bin/env python3
"""Serve the built site (dist/) over the local network.

Usage:
    npm run build   # first
    python3 serve.py [port]

Then open http://<this-machine-ip>:<port> from another device on the same Wi-Fi.
"""

import argparse
import functools
import http.server
import os
import socket
import socketserver
import sys

DIST_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIST_DIR, **kwargs)

    def log_message(self, format, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), format % args))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("port", nargs="?", type=int, default=8000)
    args = parser.parse_args()

    if not os.path.isdir(DIST_DIR):
        sys.exit("dist/ not found. Run `npm run build` first.")

    handler = functools.partial(QuietHandler)
    with socketserver.ThreadingTCPServer(("0.0.0.0", args.port), handler) as httpd:
        host = socket.gethostbyname(socket.gethostname())
        print(f"Serving {DIST_DIR} on http://0.0.0.0:{args.port}")
        print(f"Reachable at: http://{host}:{args.port} (and http://localhost:{args.port})")
        print("Press Ctrl+C to stop.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()
