from contextlib import contextmanager

class BaseStorageBackend(object):
    @contextmanager
    def open(self, storage_object, file, *args, **kwargs):
        raise NotImplementedError('subclasses of BaseValidator must provide an open() method')

    def read(self, storage_object, dst, extract=False, include_xml=True, block_size=None):
        raise NotImplementedError('subclasses of BaseValidator must provide an read() method')

    def write(self, src, ip, storage_method, storage_medium, create_obj=True, update_obj=None, block_size=None):
        raise NotImplementedError('subclasses of BaseValidator must provide an write() method')