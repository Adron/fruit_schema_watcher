import threading
import time
from chaos import the_deluge

class FiveSecondService:
    def __init__(self):
        self._stop_event = threading.Event()
        self._thread = threading.Thread(target=self._run)

    def start(self):
        """Start the service."""
        self._stop_event.clear()
        self._thread.start()

    def stop(self):
        """Stop the service."""
        self._stop_event.set()
        self._thread.join()

    def _run(self):
        while not self._stop_event.is_set():
            start_time = time.time()
            self.execute_code()

            elapsed_time = time.time() - start_time
            time_to_sleep = max(0, 5 - elapsed_time)
            time.sleep(time_to_sleep)

    def execute_code(self):
        # This is the part that runs every 5 seconds.
        the_deluge()
        print("Code executed at:", time.strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == "__main__":
    service = FiveSecondService()
    try:
        service.start()
        while True:
            time.sleep(1)  # Keep the main thread alive
    except KeyboardInterrupt:
        service.stop()
        print("Service stopped.")
