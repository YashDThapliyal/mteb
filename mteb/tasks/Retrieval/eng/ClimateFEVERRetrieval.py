from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


class ClimateFEVER(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="ClimateFEVER",
        description="CLIMATE-FEVER is a dataset adopting the FEVER methodology that consists of 1,535 real-world claims regarding climate-change. ",
        reference="https://www.sustainablefinance.uzh.ch/en/research/climate-fever.html",
        dataset={
            "path": "mteb/climate-fever",
            "revision": "47f2ac6acb640fc46020b02a5b59fdda04d39380",
        },
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="ndcg_at_10",
        date=None,
        domains=None,
        task_subtypes=None,
        license=None,
        annotations_creators=None,
        dialect=None,
        sample_creation=None,
        bibtex_citation="""@misc{diggelmann2021climatefever,
      title={CLIMATE-FEVER: A Dataset for Verification of Real-World Climate Claims}, 
      author={Thomas Diggelmann and Jordan Boyd-Graber and Jannis Bulian and Massimiliano Ciaramita and Markus Leippold},
      year={2021},
      eprint={2012.00614},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}""",
        prompt={
            "query": "Given a claim about climate change, retrieve documents that support or refute the claim"
        },
        descriptive_stats={
            "n_samples": None,
            "avg_character_length": {
                "test": {
                    "average_document_length": 538.241873443325,
                    "average_query_length": 123.39934853420195,
                    "num_documents": 5416593,
                    "num_queries": 1535,
                    "average_relevant_docs_per_query": 3.0495114006514656,
                }
            },
        },
    )


class ClimateFEVERHardNegatives(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="ClimateFEVERHardNegatives",
        description="CLIMATE-FEVER is a dataset adopting the FEVER methodology that consists of 1,535 real-world claims regarding climate-change. The hard negative version has been created by pooling the 250 top documents per query from BM25, e5-multilingual-large and e5-mistral-instruct.",
        reference="https://www.sustainablefinance.uzh.ch/en/research/climate-fever.html",
        dataset={
            "path": "mteb/ClimateFEVER_test_top_250_only_w_correct-v2",
            "revision": "3a309e201f3c2c4b13bd4a367a8f37eee2ec1d21",
        },
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="ndcg_at_10",
        date=None,
        domains=None,
        task_subtypes=None,
        license=None,
        annotations_creators=None,
        dialect=None,
        sample_creation=None,
        bibtex_citation="""@misc{diggelmann2021climatefever,
      title={CLIMATE-FEVER: A Dataset for Verification of Real-World Climate Claims}, 
      author={Thomas Diggelmann and Jordan Boyd-Graber and Jannis Bulian and Massimiliano Ciaramita and Markus Leippold},
      year={2021},
      eprint={2012.00614},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}""",
        descriptive_stats={
            "n_samples": {"test": 1000},
            "avg_character_length": {
                "test": {
                    "average_document_length": 1245.4236333727013,
                    "average_query_length": 121.879,
                    "num_documents": 47416,
                    "num_queries": 1000,
                    "average_relevant_docs_per_query": 3.048,
                }
            },
        },
    )
