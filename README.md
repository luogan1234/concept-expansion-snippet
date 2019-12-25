# concept-expansion-snippet

**requirements:** Python >= 3.5, Tensorflow >= 1.10

This toolkit provides graph propagation, average distance, PageRank and tf-idf algorithms with pretrained word vectors (BERT) to do the concept extraction and concept expansion tasks. It supports both Chinese and English text.

- **Concept extraction:** Given seed concepts, extract the related concepts from the input text.
- **Concept expansion:** Given seed concepts, extract the related concepts from the snippets of search engine results (Baidu for Chinese and Google for English).

## Before running the code
1. run `bash init.sh`.
2. `cd bert_start/`
3. run `bert_start.sh -l en|zh` to start the BERT service.

## Parameters

You can run `example_cmd.sh -t en0|en1|zh0|zh1` to run examples, and follow the `example_cmd.sh` to run this toolkit.

Some important parameters available in command line:

```
-task: required, extract | expand
--input_text, -it: the text file for concept extraction task
--input_seed, -is: the seed file for concept extraction & expansion task
--language, -l: required, zh | en
--snippet_source, -ss: baidu | google | bing
--no_seed, -ns: store true if every candidate in text is a seed
--noun_filter, -nf: remove non-noun candidates
--algorithm, -a: graph_propagation | average_distance | tf_idf | pagerank
```

The following path lists can be modified in `config.py`:

```
zh_list, en_list: the candidate concepts
db: store the crawled snippets
cookie_paths: some cookie files to support the crawl process
```

## Note

To crawl Google search snippets, you need VPN (for users in Mainland China). 

The crawler may be blocked by anti-crawler programs, do not crawl Google search engine results too fast.
