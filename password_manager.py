#!/usr/bin/env python3.5
from password_manager.password_manager import PasswordManager
from os.path import expanduser
import argparse


actions = {
    'na': lambda x, args: None,
    'ls': lambda x, args: print('\n'.join(list(map(str, x.passwords() + x.services())) or ['no objects here'])),
    'as': lambda x, args: x.add_service(**eval('dict({})'.format(', '.join(args)))),
    'ap': lambda x, args: x.add_password(**eval('dict({})'.format(', '.join(args)))),
    'rp': lambda x, args: x.remove_password(int(args[0])),
    'rs': lambda x, args: x.remove_service(int(args[0]))
}


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('action',
                        type=str,
                        action='store',
                        default='none',
                        choices=actions.keys(),
                        help='the name of the action on the database')
    parser.add_argument('-d',
                        '--database',
                        nargs='?',
                        default=expanduser('~/.passdb'),
                        help='database path')
    parser.add_argument('arguments',
                        nargs=argparse.REMAINDER,
                        help='arguments for a command')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    pm = PasswordManager(args.database)
    actions[args.action](pm, args.arguments)

