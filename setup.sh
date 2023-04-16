python3 -m venv .venv
source ./env/bin/activate
pip install -r requirements.txt

mkdir -p models
mkdir -p images
mkdir -p inference
mkdir -p inference/imgs
mkdir -p inference/masks

mkdir -p data
unzip -q data/dataset.zip -d data/
mkdir -p data/test/masks
rm data/sample_submission.csv data/transform_solution.ipynb

python3 prepare.py