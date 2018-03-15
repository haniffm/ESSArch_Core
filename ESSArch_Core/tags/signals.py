import cPickle
import logging

from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from redis import StrictRedis

from ESSArch_Core.tags import DELETION_QUEUE, INDEX_QUEUE, UPDATE_QUEUE
from ESSArch_Core.tags.models import TagVersion

logger = logging.getLogger('essarch.core')
r = StrictRedis()


@receiver(post_save, sender=TagVersion)
def queue_tag_for_index(sender, instance, created, **kwargs):
    if created:
        r.rpush(INDEX_QUEUE, cPickle.dumps(instance.to_search()))
    else:
        data = {
            '_op_type': 'update',
            'doc_as_upsert': True,
            '_index': instance.elastic_index,
            '_type': 'doc',
            '_id': str(instance.pk),
            'doc': {
                'name': instance.name,
                'type': instance.type,
            },
        }
        r.rpush(UPDATE_QUEUE, cPickle.dumps(data))


@receiver(post_delete, sender=TagVersion)
def queue_tag_for_deletion(sender, instance, **kwargs):
    data = {
        '_op_type': 'delete',
        '_index': instance.elastic_index,
        '_type': 'doc',
        '_id': str(instance.pk),
    }
    r.rpush(DELETION_QUEUE, cPickle.dumps(data))