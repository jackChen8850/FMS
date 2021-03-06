# coding=utf-8
import hashlib
import os
from functools import partial

from config import UPLOAD_FOLDER

HERE = os.path.abspath(os.path.dirname(__file__))


def get_file_md5(f, chunk_size=8192):
    h = hashlib.md5()
    while True:
        chunk = f.read(chunk_size)
        if not chunk:
            break
        h.update(chunk)
    return h.hexdigest()


def humanize_bytes(bytesize, precision=2):
    abbrevs = (
        (1 << 50, 'PB'),
        (1 << 40, 'TB'),
        (1 << 30, 'GB'),
        (1 << 20, 'MB'),
        (1 << 10, 'kB'),
        (1, 'bytes')
    )
    if bytesize == 1:
        return '1 byte'
    for factor, suffix in abbrevs:
        if bytesize >= factor:
            break
    return '%.*f %s' % (precision, bytesize / factor, suffix)


if not os.path.exists(os.path.join(HERE, UPLOAD_FOLDER)):
    os.makedirs(os.path.join(HERE, UPLOAD_FOLDER))


get_file_path = partial(os.path.join, HERE, UPLOAD_FOLDER)
