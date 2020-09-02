#!/usr/bin/env python3
import pprint
import json

import click

from random import choice

from places import places, place_adjectives
from who import who, who_adjectives
from plots import plot_devices
from misc import misc


def pick_random_plot():
    plot_base = choice(plots)
    sub_parts = []

    if "{}" not in plot_base:
        return plot_base

    for sub in range(plot_base[0].count("{}")):
        sub_parts.append(choice(plot_base[sub]))

    sub_tuple = tuple(sub_parts)
    print("ST: {}".format(sub_tuple))
    return plot_base[0].format(sub_tuple)


def pick_items():
    items = []
    for x in range(5):
        items.append(choice(misc))
    return ", ".join(items)


def generate_json(pprinter, pick):
    pprinter.pprint(json.dumps(pick))


def print_to_console(number, pick):
    if number > 0:
        print("\u2500" * 80)

    print("#{}: \033[33;1mWho:\033[0m   {}".format(
        number + 1, pick['who_value']))
    print("    \033[33;1mPlace:\033[0m {}".format(
        pick['place_value']))
    print("    \033[33;1mPlot-device:\033[0m")
    print("           {}".format(pick['plot_dev_value']))
    print("    \033[33;1m5 Random items, pick at least 2:\033[0m")
    print("           {}".format(pick['random_items']))
    print()


@click.command()
@click.argument("count", type=int)
@click.option("--json", 'output_json', is_flag=True, default=False)
def main(count, output_json):
    print()

    if output_json:
        json_objects = []

    for x in range(count):
        pick = {}

        pick['who_value'] = " ".join([
            choice(who_adjectives), choice(who)
        ])
        pick['place_value'] = " ".join([
            choice(place_adjectives), choice(places)
        ])
        pick['plot_dev_value'] = choice(plot_devices)
        pick['random_items'] = pick_items()

        if output_json:
            json_objects.append(pick)
        else:
            print_to_console(x, pick)
    if output_json:
        print(json.dumps(json_objects, indent=4))


if __name__ == '__main__':
    main()
