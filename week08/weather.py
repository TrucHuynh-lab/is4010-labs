
import argparse
import os
import sys
from pathlib import Path

FAVORITES_FILE = Path(__file__).resolve().parent / "favorites.json"


try:
    from .favorites import FavoritesManager
    from .weather_api import (
        WeatherAPI,
        format_current_weather,
        format_forecast,
    )
except ImportError:
    from favorites import FavoritesManager
    from weather_api import (
        WeatherAPI,
        format_current_weather,
        format_forecast,
    )


def load_api_key():
    api_key = os.environ.get("WEATHER_API_KEY")

    if api_key:
        return api_key

    try:
        import config
        return getattr(
            config,
            "WEATHER_API_KEY",
            getattr(config, "API_KEY", None)
        )
    except ImportError:
        return None


def build_parser():
    parser = argparse.ArgumentParser(
        description="Weather CLI Application"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    current_parser = subparsers.add_parser(
        "current",
        help="Get current weather"
    )
    current_parser.add_argument("location")

    forecast_parser = subparsers.add_parser(
        "forecast",
        help="Get weather forecast"
    )
    forecast_parser.add_argument("location")
    forecast_parser.add_argument(
        "--days",
        type=int,
        default=3,
        choices=range(1, 4)
    )

    favorites_parser = subparsers.add_parser(
        "favorites",
        help="Manage favorite locations"
    )

    favorites_subparsers = favorites_parser.add_subparsers(
        dest="favorites_command",
        required=True
    )

    add_parser = favorites_subparsers.add_parser("add")
    add_parser.add_argument("name")
    add_parser.add_argument("location")

    favorites_subparsers.add_parser("list")

    remove_parser = favorites_subparsers.add_parser("remove")
    remove_parser.add_argument("name")

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    manager = FavoritesManager(str(FAVORITES_FILE))

    if args.command == "favorites":
        if args.favorites_command == "add":
            if manager.add(args.name, args.location):
                print(f"Added favorite: {args.name}")
                return 0

            print("Error: Favorite already exists.", file=sys.stderr)
            return 1

        if args.favorites_command == "list":
            favorites = manager.list_all()

            if not favorites:
                print("No favorite locations saved.")
            else:
                for name, location in favorites.items():
                    print(f"{name}: {location}")

            return 0

        if args.favorites_command == "remove":
            if manager.remove(args.name):
                print(f"Removed favorite: {args.name}")
                return 0

            print("Error: Favorite not found.", file=sys.stderr)
            return 1

    api_key = load_api_key()

    if not api_key:
        print("Error: Weather API key is missing.", file=sys.stderr)
        return 1

    api = WeatherAPI(api_key)

    location = manager.get_location(args.location)
    if location is None:
        location = args.location

    if args.command == "current":
        data = api.get_current_weather(location)

        if data is None:
            print("Error: Could not get current weather.", file=sys.stderr)
            return 1

        try:
            print(format_current_weather(data))
        except (KeyError, TypeError, ValueError):
            print("Error: Invalid weather data.", file=sys.stderr)
            return 1

        return 0

    if args.command == "forecast":
        try:
            data = api.get_forecast(location, args.days)
        except ValueError as error:
            print(f"Error: {error}", file=sys.stderr)
            return 1

        if data is None:
            print("Error: Could not get forecast.", file=sys.stderr)
            return 1

        try:
            print(format_forecast(data))
        except (KeyError, TypeError, ValueError):
            print("Error: Invalid forecast data.", file=sys.stderr)
            return 1

        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
