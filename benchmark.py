import requests
import os
import pandas as pd
image_dir = "images"
api_endpoint = "http://3.23.107.86/predict/"

def get_inference(image_path):
    with open(image_path, 'rb') as image_file:
        files = {'file':image_file}
        response = requests.post(api_endpoint, files=files)
        inference_results = response.json()
        for recommendation in inference_results['recommendations']:
            recommendation['Image'] = image_name
        return inference_results

results = []

for image_name in os.listdir(image_dir):
    print(image_name)
    image_path = os.path.join(image_dir, image_name)
    print(image_path)
    try:
        inference_result = get_inference(image_path=image_path)
        results.extend(inference_result['recommendations'])
    except Exception as e:
        print(f"Error processing {image_name}: {e}")
        results.append({
            'Image': image_name,
            'Result': 'Error'
        })
        
# Create a DataFrame from the results
df = pd.DataFrame(results)

# Export the DataFrame to an Excel file
output_file = "results/inference_results.xlsx"
os.makedirs(os.path.dirname(output_file), exist_ok=True)
df.to_excel(output_file, index=False)

print(f"Results have been exported to {output_file}")