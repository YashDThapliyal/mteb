from mteb.abstasks.AbsTaskClassification import AbsTaskClassification
from mteb.abstasks.TaskMetadata import TaskMetadata

class DiabeticRetinopathyDetection(AbsTaskClassification):
    metadata = TaskMetadata(
        name="WDS_Diabetic_Retinopathy",
        description=(
            "The dataset comprises of images labeled to indicate the presence or absence of diabetic retinopathy."
        ),
        reference="https://huggingface.co/datasets/haideraltahan/wds_diabetic_retinopathy",
        type="ImageClassification",
        category="i2t", #its image to number but i think thats close enough?
        modalities=["image", "text"],
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="accuracy",
        dataset={
            "path": "haideraltahan/wds_diabetic_retinopathy",
            "revision": "63214e0024f8dac2b1e40d077f789ae1f1b9f0fa",
        },
        date=("2024-04-12", "2024-04-12"), 
        domains=["Medical"],
        task_subtypes=["Tumor detection"],
        #license="cc-by-4.0",  # not sure about liscense as its not mentioned in the dataset
        annotations_creators="expert-annotated",
        dialect=[],
        sample_creation="found",
        bibtex_citation="""
@dataset{altahan2024wds_diabetic_retinopathy,
    title={WDS_Diabetic_Retinopathy},
    author={Haider Altahan},
    year={2024},
    publisher={Hugging Face},
    url={https://huggingface.co/datasets/haideraltahan/wds_diabetic_retinopathy}
}
""",
    )

print("DiabeticRetinopathyDetection task loaded successfully")
