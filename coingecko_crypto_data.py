import json
import requests
from constants import *
from google.cloud import pubsub_v1
import os

# Set the environment variable (consider using a secure approach)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_path


def top10_crypto_list():
    """Fetches a list of the top 10 cryptocurrencies from a CoinGecko API endpoint.

    Raises:
        Exception: If an error occurs during the API call.

    Returns:
        dict: A dictionary containing the retrieved top 10 crypto data.
    """

    try:
        headers = {
            "accept": content_type,
            "x-cg-pro-api-key": api_key
        }
        response = requests.get(url=url, headers=headers)
        return response.json()

    except Exception as e:
        print(f"Unable to retrieve the list of top 10 crypto currencies: {e}")
        raise


def initialize_pubsub():
    """Initializes a Pub/Sub publisher client and returns the publisher object
    and the topic path.

    Raises:
        Exception: If an error occurs during Pub/Sub client creation.

    Returns:
        tuple: A tuple containing the Pub/Sub publisher client (`pubsub_v1.PublisherClient`)
               and the topic path (`str`).
    """

    try:
        publisher = pubsub_v1.PublisherClient()
        path_of_the_topic = publisher.topic_path(project=project_id, topic=topic_id)
        return publisher, path_of_the_topic

    except Exception as e:
        print(f"Unable to initialize publisher: {e}")
        raise


def publish_data_to_pubsub(publisher, path_of_the_topic, data):
    """Publishes a list of cryptocurrency data records to a Pub/Sub topic.

    Args:
        publisher (pubsub_v1.PublisherClient): The Pub/Sub publisher client.
        path_of_the_topic (str): The path of the Pub/Sub topic to publish to.
        data (list): A list of cryptocurrency data records (dictionaries).

    Raises:
        Exception: If an error occurs during data publishing.
    """

    try:
        for record in data:
            message_json = json.dumps(record)
            message_bytes = message_json.encode('utf-8')
            published_data = publisher.publish(topic=path_of_the_topic, data=message_bytes)
            print("Data -> ", message_json)
            print(f"Published message ID: {published_data.result()}")

    except Exception as e:
        print(f"Failed to publish data: {e}")
        raise


if __name__ == '__main__':

    # Consider using a configuration manager or environmental variables for service account path
    # Initialising publisher
    publisher, topic = initialize_pubsub()

    # Fetching top 10 crypto-currency data
    data = top10_crypto_list()

    # Publishing data to pubsub
    publish_data_to_pubsub(publisher=publisher, path_of_the_topic=topic, data=data)