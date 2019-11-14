import click
import logging

from prepare.prepare_json_l8 import add_datacube_dataset


@click.command(help="Enter Bucket name. Optional to enter configuration file to access a different database")
@click.argument('bucket_name')
@click.option('--config', '-c', help=" Pass the config file to access the database", type=click.Path(exists=True))
@click.option('--prefix', '-p', help="Pass the prefix of the object to the bucket")
def main(bucket_name, config, prefix):
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)
    add_datacube_dataset(bucket_name, config, prefix)


if __name__ == "__main__":
    main()



