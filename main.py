from password_manager.password_manager import PasswordManager
import argparse


actions = {
    'none': lambda x, args: None,
    'dump': lambda x, args: print(', '.join(list(map(str, x.passwords())) or ['no objects here'])),
    'adds': lambda x, args: x.add_service(**eval('dict({})'.format(', '.format(args)))),
    'addp': lambda x, args: x.add_password(**eval('dict({})'.format(', '.format(args)))),
    'rmp': lambda x, args: x.remove_password(args[0]),
    'rms': lambda x, args: x.remove_service(args[0])
}

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--database', type=str, default='./db.sqlite', action='store')
    parser.add_argument('--action', type=str, action='store', default='none', choices=actions.keys())
    parser.add_argument('arguments', nargs=argparse.REMAINDER) 
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    pm = PasswordManager(args.database)
    actions[args.action](pm, args.arguments)

