import json
import argparse
import pandas as pd

def parse_json(json_file, output_file):
    """
    Parses a JSON file containing test results, converts the "executed_on"
    column to datetime format, and exports the data to a CSV file.

    Args:
        json_file (str): Path to the JSON file containing test case data.
        output_file (str): Path to the output CSV file.

    Returns:
        tuple: A tuple containing (parsed JSON data, DataFrame with test cases).
    """

    with open(json_file, "r") as f:
        data = json.loads(f.read())

    df = pd.DataFrame(data["test_cases"])

    # Convert the "executed_on" column to datetime format
    df["executed_on"] = pd.to_datetime(df["executed_on"])

    # Export the DataFrame to a CSV file
    df.to_csv(output_file, index=False)
    print(f"{json_file} was exported successfully to {output_file}")
    return data, df


def calculate_metrics(df):
    """
    Calculates various metrics based on the provided DataFrame containing test results.

    Args:
        df (pd.DataFrame): DataFrame with test case data.

    Returns:
        list: List containing the calculated metrics in the following order:
            - Total tests
            - Passed tests
            - Failed tests
            - Blocked tests
            - Average execution time (in minutes)
            - Minimum execution time
            - Maximum execution time
    """

    total_tests = df.shape[0]
    passed = df[df["status"] == "passed"].shape[0]
    failed = df[df["status"] == "failed"].shape[0]
    blocked = df[df["status"] == "blocked"].shape[0]
    avg_duration = df["execution_time"].mean()
    min_duration = df["execution_time"].min()
    max_duration = df["execution_time"].max()

    return [
        total_tests,
        passed,
        failed,
        blocked,
        avg_duration,
        min_duration,
        max_duration
    ]


def print_metrics(metrics):
    """
    Prints the calculated test metrics in a user-friendly format.

    Args:
        metrics (list): List containing the calculated metrics.
    """

    print(f"Total tests: {metrics[0]}")
    print(f"Passed: {metrics[1]} out of {metrics[0]} tests")
    print(f"Failed: {metrics[2]} out of {metrics[0]} tests")
    print(f"Blocked: {metrics[3]} out of {metrics[0]} tests")
    print(f"Average duration: {metrics[4]:.2f} minutes")
    print(f"Minimum duration: {metrics[5]:.2f} minutes")
    print(f"Maximum duration: {metrics[6]:.2f} minutes")


def main():
    """
    Parses a JSON file containing test results, export it to CSV file, calculates metrics, and prints them.
    """

    parser = argparse.ArgumentParser(description="Process TC results from JSON file")
    parser.add_argument("json_file", type=str, help="Path to the JSON file containing test case data")
    parser.add_argument("output_file", type=str, help="Path to the output CSV file")
    args = parser.parse_args()

    data, df = parse_json(args.json_file, args.output_file)
    metrics = calculate_metrics(df)

    print_metrics(metrics)


if __name__ == "__main__":
    main()
