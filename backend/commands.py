import asyncio
import argparse


FUNC_MAP = {}


def main():
    parser = argparse.ArgumentParser()

    kwargs = vars(parser.parse_args())
    command = kwargs.pop("command")
    asyncio.get_event_loop().run_until_complete(FUNC_MAP[command](**kwargs))


if __name__ == "__main__":
    main()
