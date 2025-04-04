import time
from databases.redis_connector import get_redis_database


def publish_fake_coordinates(order_tracking_id):
    coord = [[8.650906272461723, 49.4136668966928],
             [8.651627250048476, 49.41369202511265],
             [8.652215190395507, 49.41371436141591],
             [8.65218085798915, 49.41329834566034],
             [8.652172275018529, 49.41292420771248],
             [8.652172275018529, 49.41292141567013],
             [8.653528399994684, 49.41275668233391],
             [8.65508193545611, 49.412558443305215],
             [8.655120559003992, 49.41193300765829],
             'Delivered']

    rc = get_redis_database()

    for item in coord:
        rc.publish(order_tracking_id, str(item))
        time.sleep(4)


if __name__ == '__main__':
    publish_fake_coordinates("63ee98fbdebd7ba1775d9317")
