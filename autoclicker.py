import argparse
import time

try:
    import pyautogui  # type: ignore
except Exception as exc:
    raise SystemExit(
        "pyautogui is required for the auto-clicker. "
        "Install it via 'pip install pyautogui'.\n" + str(exc)
    )

pyautogui.FAILSAFE = True


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Simple automatic mouse clicker"
    )
    parser.add_argument(
        "--interval", type=float, default=0.1,
        help="Seconds to wait between clicks (default: 0.1)"
    )
    parser.add_argument(
        "--button", choices=["left", "right", "middle"],
        default="left", help="Mouse button to click"
    )
    parser.add_argument(
        "--count", type=int, default=0,
        help="Number of clicks to perform (0 for infinite)"
    )
    args = parser.parse_args()

    print("Starting auto-clicker. Move mouse to a corner or press Ctrl+C to stop.")
    try:
        if args.count > 0:
            for _ in range(args.count):
                pyautogui.click(button=args.button)
                time.sleep(args.interval)
        else:
            while True:
                pyautogui.click(button=args.button)
                time.sleep(args.interval)
    except KeyboardInterrupt:
        print("Auto-clicker stopped by user.")


if __name__ == "__main__":
    main()
