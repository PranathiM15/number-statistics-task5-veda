import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HOST = "127.0.0.1"
PORT = 8000
ROOT = Path(__file__).resolve().parent


def analyze_numbers(numbers):
    """Analyze numbers using a loop and modulo operator."""
    evens = []
    odds = []

    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
        else:
            odds.append(number)

    return {
        "numbers": numbers,
        "count": len(numbers),
        "even": evens,
        "odd": odds,
        "largest": max(numbers),
        "smallest": min(numbers),
        "sum": sum(numbers),
        "average": round(sum(numbers) / len(numbers), 2),
    }


class NumberStatsHandler(BaseHTTPRequestHandler):
    def _send(self, status, content_type, body):
        if isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self._send(
                200,
                "text/html; charset=utf-8",
                (ROOT / "index.html").read_text(encoding="utf-8"),
            )
        elif self.path == "/style.css":
            self._send(
                200,
                "text/css; charset=utf-8",
                (ROOT / "style.css").read_text(encoding="utf-8"),
            )
        elif self.path == "/script.js":
            self._send(
                200,
                "application/javascript; charset=utf-8",
                (ROOT / "script.js").read_text(encoding="utf-8"),
            )
        else:
            self._send(404, "text/plain; charset=utf-8", "Page not found.")

    def do_POST(self):
        if self.path != "/api/analyze":
            self._send(404, "application/json", json.dumps({"error": "Endpoint not found."}))
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            raw = payload.get("numbers", "")

            if not isinstance(raw, str) or not raw.strip():
                raise ValueError("Enter at least one number.")

            # Accept commas, spaces, tabs, and new lines.
            tokens = raw.replace(",", " ").split()
            numbers = [int(token) for token in tokens]

            if len(numbers) > 500:
                raise ValueError("Please enter 500 numbers or fewer.")

            result = analyze_numbers(numbers)
            self._send(
                200,
                "application/json; charset=utf-8",
                json.dumps(result),
            )
        except ValueError as exc:
            self._send(
                400,
                "application/json; charset=utf-8",
                json.dumps({"error": str(exc)}),
            )
        except Exception:
            self._send(
                400,
                "application/json; charset=utf-8",
                json.dumps({"error": "Please enter valid whole numbers only."}),
            )

    def log_message(self, format, *args):
        print("[server]", format % args)


if __name__ == "__main__":
    print("=" * 58)
    print("  NOVA NUMBER STATISTICS LAB")
    print("  Running at http://127.0.0.1:8000")
    print("  Press Ctrl+C to stop the server.")
    print("=" * 58)
    ThreadingHTTPServer((HOST, PORT), NumberStatsHandler).serve_forever()
