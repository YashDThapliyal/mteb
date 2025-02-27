from mteb.abstasks.AbsTaskClassification import AbsTaskClassification
from mteb.abstasks.TaskMetadata import TaskMetadata

class DMLabClassification(AbsTaskClassification):
    metadata = TaskMetadata(
        name="WDS_DMLab",
        description="A dataset containing images and corresponding class labels for classification tasks.",
        reference="https://huggingface.co/datasets/haideraltahan/wds_dmlab",
        type="ImageClassification",
        category="i2t",
        modalities=["image", "text"],
        eval_splits=["test"],
        eval_langs=["eng-Latn"],  # UNSURE: Language information not specified
        main_score="accuracy",
        dataset={
            "path": "haideraltahan/wds_dmlab",
            "revision": "4a8270a975450742eac5c6b2825da34a619b9658", 
        },
        date=("2024-04-12", "2024-04-12"), 
        domains=["Fiction", "Scene"],  # UNSURE
        task_subtypes=["Scene recognition"],  # UNSURE
        license="not specified",
        annotations_creators="expert-annotated",  # UNSURE
        dialect=[],
        sample_creation="found",  # UNSURE
        bibtex_citation="""
@dataset{altahan_wds_dmlab,
    title={WDS_DMLab},
    author={Haider Altahan},
    year={2024},
    publisher={Hugging Face},
    url={https://huggingface.co/datasets/haideraltahan/wds_dmlab}
}
""",
    )

print("DMLabClassification task loaded successfully")
