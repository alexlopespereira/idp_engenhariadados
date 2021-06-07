import os
from elasticsearch import Elasticsearch

from etlelk.configbase import ConfigBase
from settings.settings_pst import body_settings_pst


class Config(ConfigBase):

    DEBUG = os.environ.get('DEBUG') == "True"
    KIBANA_SAVED_OBJECTS_PATH = os.environ.get('KIBANA_SAVED_OBJECTS_PATH') or './saved_objects'
    KIBANA_HOST = os.environ.get('KIBANA_HOST') or os.environ.get('ES_HOST') or '127.0.0.1'
    KIBANA_PORT = os.environ.get('KIBANA_PORT') or '5601'
    ES_HOST = os.environ.get('ES_HOST') or '127.0.0.1'
    ES_PORT = os.environ.get('ES_PORT') or '9200'
    ES_USER = os.environ.get('ES_USER') or 'admin'
    ES_PASSWORD = os.environ.get('ES_PASSWORD') or 'pass'  ## Setar Variavel de Ambiente
    ES_USE_SSL = os.environ.get('ES_USE_SSL') == "True"
    ES_VERIFY_CERTS = os.environ.get('ES_VERIFY_CERTS') == "True"


    if DEBUG:
        KIBANA_DEST_URL = os.environ.get('KIBANA_DEST_URL') or 'http://10.209.42.191:5601'
    else:
        KIBANA_DEST_URL = "http://{0}:{1}".format(KIBANA_HOST, KIBANA_PORT)

    DEST_PATH = "./saved_objects/"

    ES_PST_INDEX = 'pst__pst'

    job_pst = {"index": ES_PST_INDEX, "settings": body_settings_pst,
              "namespace":"default", "date_field": "date",
              "module_name": "etlpst", "class_name": "EtlPst"}

    INDEXES = {'pst': job_pst}

    es = Elasticsearch(
        hosts=[{'host': ES_HOST, 'port': ES_PORT}],
        # http_auth=(ES_USER, ES_PASSWORD),
        # use_ssl=ES_USE_SSL,
        # verify_certs=ES_VERIFY_CERTS
    )
