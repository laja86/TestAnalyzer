## Test Result Analyzer

This Python script parses a JSON file containing test case results, export the data to a CSV file for further analysis, calculates various metrics, and prints them in a user-friendly format.

### Features

* Parses JSON files containing test case data.
* Exports the data to a CSV file.
* Calculates various test metrics, including:
    * Total tests
    * Passed tests
    * Failed tests
    * Blocked tests
    * Average execution time
    * Minimum execution time
    * Maximum execution time
* Prints the calculated metrics to the console.

### Usage

1. Install the required libraries: `pip install pandas argparse`
2. Save the script as `test_analyzer.py`.
3. Run the script with the following command, replacing `<json_file>` and `<output_file>` with your actual file paths:

```
python test_analyzer.py <json_file> <output_file>
```

### Example

Here's an example of how to use the script:

```
python test_analyzer.py TC_results.json test_results.csv
```

This will parse the file `TC_results.json`, calculate the metrics, and save them to the file `test_results.csv`. The metrics will also be printed to the console.

### Requirements

* Python 3.6 or later
* pandas library
* argparse library


### Additional Notes

* The script assumes the JSON data has a specific structure. Please modify the code if your data is formatted differently.

Please let me know if you have any questions or suggestions!
