from etlelk import KibanaFunctions
from etlelk.run_etl_jobs import run_etl_job
from config import Config
config = Config()
kf = KibanaFunctions(config)
# kf.download_all()
# kf.upload_files_replacing_index_id()
# kf.els.delete_index(config.es, config.INDEXES['apps']['index'])

run_etl_job(config, config.INDEXES['pst'])

# kf.download_all()
# Copia os armazenados nos arquivos ndjson para o Kibana
# kf.upload_files_replacing_index_id('apps__apps')


