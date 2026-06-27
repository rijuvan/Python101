"""
Post-run hook: prints a summary after running the app.
Extend this to log output, send notifications, etc.
"""
import datetime


def on_run_complete(exit_code: int = 0):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "SUCCESS" if exit_code == 0 else f"FAILED (exit {exit_code})"
    print(f"[{timestamp}] Run completed: {status}")


if __name__ == "__main__":
    on_run_complete()
