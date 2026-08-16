import json
import re
import pandas as pd

def extract_data_from_notebook(notebook_path="run.ipynb"):
    with open(notebook_path, 'r') as f:
        notebook = json.load(f)

    hyperparameters = {}
    validation_results = []
    testing_results = []

    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            source = "".join(cell['source'])

            # Extract hyperparameters
            if "batch_size =" in source:
                match = re.search(r"batch_size = (\d+)", source)
                if match:
                    hyperparameters['batch_size'] = int(match.group(1))
            if "num_classes =" in source:
                match = re.search(r"num_classes = (\d+)", source)
                if match:
                    hyperparameters['num_classes'] = int(match.group(1))
            if "lr=" in source:
                match = re.search(r"lr=(e?-?\d\.\d+)", source)
                if match:
                    hyperparameters['learning_rate'] = float(match.group(1))
            if "num_epochs =" in source:
                match = re.search(r"num_epochs = (\d+)", source)
                if match:
                    hyperparameters['num_epochs'] = int(match.group(1))
            if "ViTModel.from_pretrained" in source:
                match = re.search(r'ViTModel.from_pretrained\("([^"]+)"\)', source)
                if match:
                    hyperparameters['model_name'] = match.group(1)
            if "device = torch.device" in source:
                match = re.search(r'device = torch.device\("([^"]+)"', source)
                if match:
                    hyperparameters['device'] = match.group(1)


            if 'outputs' in cell:
                for output in cell['outputs']:
                    if output['output_type'] == 'stream' and output['name'] == 'stdout':
                        output_text = "".join(output['text'])

                        # Extract validation results
                        for line in output_text.split('\n'):
                            val_match = re.search(r"Epoch (\d+)/\d+:\s+Train Loss: (\d+\.\d+)\s+Val Loss: (\d+\.\d+), Val Accuracy: (\d+\.\d+)", line)
                            if val_match:
                                epoch, train_loss, val_loss, val_accuracy = val_match.groups()
                                validation_results.append({
                                    'Epoch': int(epoch),
                                    'Train Loss': float(train_loss),
                                    'Val Loss': float(val_loss),
                                    'Val Accuracy': float(val_accuracy)
                                })

                        # Extract testing results
                        test_matches = re.findall(r"Test Loss: (\d+\.\d+), Test Accuracy: (\d+\.\d+)", output_text)
                        for i, match in enumerate(test_matches):
                            test_loss, test_accuracy = match
                            testing_results.append({
                                'Test Set': f'Test_{i}',
                                'Test Loss': float(test_loss),
                                'Test Accuracy': float(test_accuracy)
                            })
    return hyperparameters, validation_results, testing_results

def save_to_excel(hyperparameters, validation_results, testing_results, output_file="experiment_results.xlsx"):
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        # Hyperparameters
        hp_df = pd.DataFrame(hyperparameters.items(), columns=['Parameter', 'Value'])
        hp_df.to_excel(writer, sheet_name='Hyperparameters', index=False)

        # Validation Results
        if validation_results:
            val_df = pd.DataFrame(validation_results)
            val_df.to_excel(writer, sheet_name='Validation Results', index=False)

        # Testing Results
        if testing_results:
            test_df = pd.DataFrame(testing_results)
            test_df.to_excel(writer, sheet_name='Testing Results', index=False)

if __name__ == "__main__":
    hp, val_res, test_res = extract_data_from_notebook()
    save_to_excel(hp, val_res, test_res)
    print(f"Results saved to experiment_results.xlsx")
