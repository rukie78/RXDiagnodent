
import sys
import random
import json
from PIL import Image

def simulate_diagnosis(image_path):
    print(f"Processing image: {image_path}")
    teeth = [11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26]
    diagnoses = ['carie', 'pulpita', 'granulom', 'parodontita', 'fractura', 'sănătos']
    results = {}

    for tooth in teeth:
        diag = random.choice(diagnoses)
        score = round(random.uniform(0.60, 0.99), 2)
        results[f"tooth_{tooth}"] = {"diagnosis": diag, "score": score}

    print(json.dumps(results, indent=4))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_diagnosis.py path_to_image")
        sys.exit(1)

    image_path = sys.argv[1]
    try:
        Image.open(image_path)
        simulate_diagnosis(image_path)
    except Exception as e:
        print("Invalid image file:", e)
