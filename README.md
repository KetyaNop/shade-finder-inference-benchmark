Below a guide on how to use the benchmark inference for the Shade Finder API. Follow the steps outlined below to upload images, run the benchmark script, and generate an inference results Excel sheet.

### Steps to Use the Benchmark Inference

1. Install `requests`, `pands`, and `openpyxl`

```bash
pip install requests pandas openpyxl
```

2. Upload all the images you want to use for inference to the `images` directory
3. Execute the script

```bash
python benchmark.py 
```

4. Results in an excel sheet located in `/results`
