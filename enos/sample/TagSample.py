import time

from enos.message.upstream.tag.TagDeleteRequest import TagDeleteRequest
from enos.message.upstream.tag.TagQueryRequest import TagQueryRequest
from enos.message.upstream.tag.TagUpdateRequest import TagUpdateRequest
from enos.sample.SampleHelper import SampleHelper


def tag_query():
    """this sample is to query tag"""
    tag_query_request = TagQueryRequest.builder() \
        .add_key('tag1') \
        .add_keys(SampleHelper.TAGS) \
        .query_all() \
        .build()
    tag_query_response = client.publish(tag_query_request)
    if tag_query_response:
        print('tag_query_response: %s' % tag_query_response.get_code())


def tag_delete():
    """this sample is to delete tag"""
    tag_delete_request = TagDeleteRequest.builder() \
        .delete_tag_key("size") \
        .delete_tag_keys(SampleHelper.TAGS) \
        .build()
    tag_delete_response = client.publish(tag_delete_request)
    if tag_delete_response:
        print('tag_delete_response: %s' % tag_delete_response.get_code())


def tag_update():
    """this sample is to update tag"""
    tag_update_request = TagUpdateRequest.builder() \
        .add_tag("tag1", "22") \
        .add_tags(SampleHelper.TAGS) \
        .build()
    tag_update_response = client.publish(tag_update_request)
    if tag_update_response:
        print('tag_update_response: %s' % tag_update_response.get_code())


if __name__ == "__main__":
    client = SampleHelper.CLIENT
    client.get_profile().set_auto_reconnect(True)
    client.setup_basic_logger('INFO')
    client.connect()  # connect in sync
    tag_query()
    tag_delete()
    tag_update()
    time.sleep(10)
