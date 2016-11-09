from __future__ import absolute_import

import os, platform, pyclbr

from django.utils.timezone import get_current_timezone

from datetime import datetime

from lxml import etree

from scandir import scandir, walk

import requests

XSD_NAMESPACE = "http://www.w3.org/2001/XMLSchema"
XSI_NAMESPACE = "http://www.w3.org/2001/XMLSchema-instance"

def sliceUntilAttr(iterable, attr, val):
    for i in iterable:
        if getattr(i, attr) == val:
            return
        yield i

def available_tasks():
    modules = ["preingest.tasks", "preingest.tests.tasks"]
    tasks = []
    for m in modules:
        module_tasks = pyclbr.readmodule(m)
        tasks = tasks + zip(
            [m+"."+t for t in module_tasks],
            module_tasks
        )
    return tasks

def create_event(eventType, eventArgs, agent, ip=None):
    """
    Creates a new event and saves it to the database

    Args:
        eventType: The event type
        eventArgs: The args that will be used to create the detail text
        agent: The agent creating the event
        ip: The information package connected to the event

    Returns:
        The created event
    """

    from ESSArch_Core.ip.models import EventIP

    detail = eventType.eventDetail % tuple(eventArgs)

    return EventIP.objects.create(
        eventType=eventType, eventDetail=detail,
        linkingAgentIdentifierValue=agent,
        linkingObjectIdentifierValue=ip,
    )


def getSchemas(doc=None, filename=None):
    """
        Creates a schema based on the schemas specified in the provided XML
        file's schemaLocation attribute
    """


    if filename:
        try:
            doc = etree.ElementTree(file=filename)
        except etree.XMLSyntaxError:
            raise
        except IOError:
            raise

    res = []
    root = doc.getroot()
    xsi_NS = "%s" % root.nsmap['xsi']

    xsd_NS = "{%s}" % XSD_NAMESPACE
    NSMAP = {'xsd': XSD_NAMESPACE}

    root = etree.Element(xsd_NS + "schema", nsmap=NSMAP)
    root.attrib["elementFormDefault"] = "qualified"

    schema_locations = set(doc.xpath("//*/@xsi:schemaLocation", namespaces={'xsi': xsi_NS}))
    for schema_location in schema_locations:
        ns_locs = schema_location.split()
        for ns, loc in zip(ns_locs[:-1], ns_locs[1:]):
            res.append([ns, loc])
            etree.SubElement(root, xsd_NS + "import", attrib={
                "namespace": ns,
                "schemaLocation": loc
            })

    return etree.XMLSchema(root)

def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime

def timestamp_to_datetime(timestamp):
    tz = get_current_timezone()
    return datetime.fromtimestamp(timestamp, tz)


def find_destination(use, structure, path=""):
    for content in structure:
        name = content.get('name')
        if content.get('use') == use:
            return path, name

        dest, fname = find_destination(
            use, content.get('children', []), os.path.join(path, name)
        )

        if dest: return dest, fname

    return None, None

def download_file(url, dst):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(dst, 'wb') as f:
            for chunk in r:
                f.write(chunk)

def get_tree_size(path):
    """Return total size of files in given path and subdirs."""
    total = 0
    for entry in scandir(path):
        if entry.is_dir(follow_symlinks=False):
            total += get_tree_size(entry.path)
        else:
            total += entry.stat(follow_symlinks=False).st_size
    return total

def get_tree_count(path):
    """Return total amount of files in given path and subdirs."""
    total = 0
    for root, dirs, files in walk(path):
        total += len(files)
    return total
