body_settings_pst = {
  ##0
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 2,
  },
"mappings": {
    "properties": {
        "date": {
            "type": "date",
            "format": "yyyy-MM-dd HH:mm:ss"
        }
    }
  }
}
