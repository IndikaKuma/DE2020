import logging
import os

from google.cloud import pubsub_v1


def create_topic(project_id, topic_id):
    # create the publisher client
    publisher = pubsub_v1.PublisherClient()
    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_id}`
    topic_path = publisher.topic_path(project_id, topic_id)
    # get create the topic
    topic = publisher.create_topic(topic_path)
    print("Created topic: {}".format(topic.name))


def publish_messages(project_id, topic_id, data_file):
    publisher = pubsub_v1.PublisherClient()
    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_id}`
    topic_path = publisher.topic_path(project_id, topic_id)
    for file_name in os.listdir(data_file):
        with open(os.path.join(data_file, file_name), 'r') as fp:  # open in readonly mode
            Lines = fp.readlines()
            for data in Lines:
                # Data must be a bytestring
                data = data.encode("utf-8")
                # When you publish a message, the client returns a future.
                future = publisher.publish(topic_path, data)
                print(future.result())

    print(f"Published messages to {topic_path}.")


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    # create_topic("de2020", "game_data")
    # create_topic("de2020", "teamscore")
    # create_topic("de2020", "userscore")
    publish_messages("de2020", "game_data", "C:\Postdoc\DE2020\DE2020\lab8\stpipeline1withpubsub\data\game")
