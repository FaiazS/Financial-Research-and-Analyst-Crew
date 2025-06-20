#!/usr/bin/env python
import sys

import warnings

from financial_analyst.crew import FinancialAnalyst

from dotenv import load_dotenv

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

load_dotenv()

def run():
    """
    Run the crew.
    """
    inputs = {

        'company': 'Amazon',
        
    }
    try:

       result = FinancialAnalyst().crew().kickoff(inputs=inputs)

       print(result.raw)

    except Exception as e:

        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == '__main__':

    run()