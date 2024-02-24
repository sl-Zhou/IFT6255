# Exp1: porter + no stopwords + BM25
## Indexing
python3 -m pyserini.index.lucene   \
--collection JsonCollection   \
--input Data_json   \
--index indexes/exp1 \
 --generator DefaultLuceneDocumentGenerator   \
 --threads 2  \
 --stemmer none  \
 --stopwords stop_words  \
 --storePositions --storeDocvectors --storeRaw
 ## Search
 python3 -m pyserini.search.lucene  \
 --index indexes/exp1   \
 --topics tsv/query.tsv  \
 --output results/ranking1.txt  \
 --bm25
 ## Evaluation
 ./trec_eval -m runid -m map -m ndcg_cut.5,10 -m P.5,10 -m recall.100 qrels.1-150.AP8890 results/ranking1.txt

 
