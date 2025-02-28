from mteb import MTEB
from mteb.tasks.Image import Any2TextMultipleChoice
from mteb.abstasks.TaskMetadata import TaskMetadata

class CountBench(Any2TextMultipleChoice):
    metadata = TaskMetadata(
        name="WDS_CountBench",
        description="A benchmark dataset for evaluating models on counting tasks within images, featuring a variety of images paired with textual descriptions indicating the quantity of objects present.",
        reference="https://huggingface.co/datasets/haideraltahan/wds_countbench",
        type="Any2TextMutipleChoice",  
        category="i2t",  
        modalities=["text","image"],
        eval_splits=["test"],
        eval_langs=["eng-Latn"], 
        main_score="counting_accuracy", 
        dataset={
            "path": "haideraltahan/wds_countbench",
            "revision": "a54b04030680563e97da7cb4fc91173e6a7a9707", #most recent commit id on hugging face
        },
        date=("2024-05-08", "2024-05-08"),
        domains=["Non-fiction"],  # not sure about this
        task_subtypes=["Object recognition"],  # Closest valid subtype
        license="not specified",  # not sure cuz liscense is not mentioned in the dataset
        annotations_creators="expert-annotated",  # not sure about this
        dialect=[],
        sample_creation="found",  # Fixed to a valid value
        bibtex_citation="""
    @dataset{altahan2024wds_countbench,
        title={WDS_CountBench: A Benchmark for Counting Tasks in Images},
        author={Haider Altahan},
        year={2024},
        publisher={Hugging Face},
        url={https://huggingface.co/datasets/haideraltahan/wds_countbench}
    }
    """,
    )

        

print("CountBench task loaded successfully")
