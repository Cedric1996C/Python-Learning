# -*- coding: utf-8 -*-
from scrapy.conf import settings
from scrapy.contrib.exporter import CsvItemExporter

class myCsvExporter(CsvItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs['fields_to_export'] = settings.getlist('EXPORT_FIELDS') or None
        kwargs['encoding'] = settings.get('EXPORT_ENCODING', 'utf-8-sig')

        super(myCsvExporter, self).__init__(*args, **kwargs)
