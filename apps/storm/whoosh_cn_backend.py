#在全局引入的最后一行加入jieba分词器
from jieba.analyse import ChineseAnalyzer


elif field_class.field_type == 'edge_ngram':
    schema_fields[field_class.index_fieldname] = NGRAMWORDS(minsize=2, maxsize=15, at='start', stored=field_class.stored, field_boost=field_class.boost)
else:
    # 修改
    schema_fields[field_class.index_fieldname] = TEXT(stored=True, analyzer=ChineseAnalyzer(), field_boost=field_class.boost, sortable=True)