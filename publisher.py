import time
import paho.mqtt.client as mqtt

if __name__ == "__main__":
    client = mqtt.Client()
    client.connect("broker.hivemq.com", 1883, 60)
    client.loop_start()
    topic = "test/topic"
    count = 0
    while True:
        message = f"Hello MQTT {count}"
        result = client.publish(topic, message)
        if result[0] == 0:
            print(f"Sent `{message}` to `{topic}`")
        else:
            print(f"Failed to send message to {topic}")
        count += 1
        time.sleep(2)