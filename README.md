# concept-expansion-snippet

**requirements:** Python >= 3.5, PyTorch >= 1.5.0, jieba, requests, bs4, nltk, pytorch-pretrained-bert

This toolkit provides graph propagation, average distance, tf-idf and PageRank algorithms with pretrained word vectors (BERT) to do the concept extraction and the concept expansion tasks. It supports both Chinese and English text.

- **Concept extraction:** Given **seed concepts** and **text**, extract the related concepts from the input text.
- **Concept expansion:** Given **seed concepts**, extract the related concepts from the snippets of search engine results (Baidu for Chinese and Google for English).

## Before running the code
1. run `python init.py`.

## Parameters

You can run `bash example_cmd.sh -t en0|en1|zh0|zh1` to run examples, and follow the `example_cmd.sh` to run this toolkit.

Some important parameters available in command line:

```
-task: required, extract | expand
-input_text, -it: the text file for concept extraction task
-input_seed, -is: the seed file for concept extraction & expansion task
-language, -l: required, zh | en
-snippet_source, -ss: baidu | google | bing
-no_seed, -ns: store true if every candidate in text is a seed
-algorithm, -a: graph_propagation | average_distance | tf_idf | pagerank
-result_path, -r
-cpu
```

The following path lists can be modified in `config.py`:

```
zh_list, en_list: all possible candidate concepts
db: store the crawled snippets
cookie_paths: some cookie files to support the crawl process
cached_vecs_path: store vectors of candidate concepts
text_path, candidate_path: tmp file
```

## Note

To crawl Google search snippets, you need VPN (for users in Mainland China). 

The crawler may be blocked by anti-crawler programs, do not crawl Google search engine results too fast.
