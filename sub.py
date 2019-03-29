#
#pip3 install --upgrade google-api-python-client
#pip3 install google.api_core - may not be needed
#pip3 install --upgrade google-cloud-pubsub
#pip3 install --upgrade oauth2client
#gcloud beta pubsub subscriptions pull --limit=3 'projects/analog-period-235204/subscriptions/my-sub'

from google.api_core.protobuf_helpers import get_messages
from google.cloud import pubsub;

subscriber = pubsub.SubscriberClient()
subscription_path = subscriber.subscription_path('analog-period-235204', 'my-sub')

def callback(message):
  print(message.data)

subscriber.subscribe(subscription_path, callback=callback)