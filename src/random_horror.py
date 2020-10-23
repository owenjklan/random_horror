#!/usr/bin/env python3
import json

import click

from random import choice


def load_word_list(f):
    return [
        w.strip() for w in open(f, "r").readlines() if len(w.strip()) > 0
    ]


def pick_items(misc, item_count):
    items = []
    for x in range(item_count):
        items.append(choice(misc))
    return items


def generate_json(pprinter, pick):
    pprinter.pprint(json.dumps(pick))


def print_to_console(number, pick):
    if number > 0:
        print("\u2500" * 80)

    print("#{}: \033[33;1mWho:\033[0m   {}".format(
        number + 1, pick['who']))
    print("    \033[33;1mPlace:\033[0m {}".format(
        pick['place']))
    print("    \033[33;1mPlot-device:\033[0m")
    print("           {}".format(pick['plot_device']))
    print("    \033[33;1m5 Random items, pick at least 2:\033[0m")
    print("           {}".format(pick['random_items']))
    print()


def randomise(count, output_json, output_html=True, items_count=5):
    who_adjectives = load_word_list("lists/who_adjectives.txt")
    who = load_word_list("lists/who_nouns.txt")
    plot_devices = load_word_list("lists/plot_devices.txt")
    items_list = load_word_list("lists/misc.txt")
    place_adjectives = load_word_list("lists/place_adjectives.txt")
    places = load_word_list("lists/place_nouns.txt")

    print()

    if output_json:
        json_objects = []

    for x in range(count):
        pick = {}

        pick['who'] = " ".join([
            choice(who_adjectives), choice(who)
        ])
        pick['place'] = " ".join([
            choice(place_adjectives), choice(places)
        ])
        pick['plot_device'] = choice(plot_devices)
        pick['random_items'] = pick_items(items_list, items_count)

        if output_json:
            json_objects.append(pick)
        else:
            print_to_console(x, pick)
    if output_json:
        return json.dumps(json_objects, indent=4)


@click.command()
@click.argument("count", type=int)
@click.option("--json", 'output_json', is_flag=True, default=False)
def main(count, output_json):
    randomise(count, output_json)


if __name__ == '__main__':
    main()
