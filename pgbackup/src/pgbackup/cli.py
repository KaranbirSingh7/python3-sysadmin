from argparse import ArgumentParser, Action
"""
Extend argparse.Action class by making a new child DriverAction
"""

known_drivers = ['local', 's3']


class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error("Unknown driver. Available drivers are local and s3")
        namespace.driver = driver.lower()
        namespace.destination = destination


"""
Create and return a new parse object
"""


def create_parser():
    parser = ArgumentParser(description="""
    Back up PostgreSQL databases locally or to AWS S3.
    """)
    parser.add_argument('url', help='URL of postgres DB to backup')
    parser.add_argument('--driver',
                        help='how and where to store backup',
                        nargs=2,
                        action=DriverAction,
                        required=True)
    return parser