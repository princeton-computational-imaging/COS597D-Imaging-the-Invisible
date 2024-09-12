import pytest
import pprint
import json
import os
import numpy as np

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    This hook puts the result of the test into the object that is the argument to
    log_test_result. Some pytest magic.
    """
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)

def load_json(json_path):
    if not os.path.isfile(json_path):
        return {}
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data

def save_json(data, json_path):
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=4)

@pytest.fixture(scope='function', autouse=True)
def log_test_result(request):
    """
    This function logs the result of each test case to tests/test_result.json.
    True indicates the test was passed, false indicates the test was failed
    tests/test_result.json is parsed by grade_assignment to generate a score
    for the submission.
    """
    yield
    test_result = load_json('tests/test_result.json')
    test_passed = not request.node.rep_call.failed
    test_result[request.node.name] = test_passed
    save_json(test_result, 'tests/test_result.json')

@pytest.fixture(scope="function", autouse=True)
def grade_assignment(request):
    """
    This is the autograder. It works by checking the results of each test case
    (kept in tests/test_result.json), looking up the weight for each test case
    in tests/rubric.json. The output of the autograder is printed to the 
    command line and logged to tests/rubric.json. 

    tests/rubric.json has the following structure:
    {
        "name_of_test_case": {
            "weight": relative_weight_for_test_case_in_grading,
            "depends": [
                "list_of", 
                "test_case_names",
                "that_this",
                "test_case",
                "depends_on",
            ]
        }
    }

    weight can be a float or an int, or it can be "required", a special string. 
    When the test case is "required", the grade for the assignment is a 0 unless
    the given test case is passed. This can be used when checking for disallowed
    imports (e.g. importing sklearn to implement the assignment). The list kept
    in the "depends" will check the status of the listed test cases. If those test
    cases are not passed, the output of this test case will be disregarded when
    computing the grade.

    The autograder outputs to tests/report.json, which looks something like this:

    {
        "score": 0,
        "tests_passed": 0,
        "notes": {
            "test_load_data": "FAIL",
            "test_train_test_split": "FAIL",
            "test_f1_measure": "FAIL",
            "test_precision_and_recall": "FAIL",
            "test_confusion_matrix": "FAIL",
            "test_experiment_run_decision_tree": "FAIL",
            "test_experiment_run_prior_probability": "FAIL",
            "test_accuracy": "FAIL",
            "test_experiment_run_and_compare": "FAIL"
        }
    }

    It also prints to the console (this may not be seen if all tests passed), 
    which looks like this:

        Output of autograder
        ======================
        # of tests:     0/9 tests passed
        Overall score:  0/100
        ======================
        FAIL test_load_data
        FAIL test_train_test_split
        FAIL test_f1_measure
        FAIL test_precision_and_recall
        FAIL test_confusion_matrix
        FAIL test_experiment_run_decision_tree
        FAIL test_experiment_run_prior_probability
        FAIL test_accuracy
        FAIL test_experiment_run_and_compare
        ======================

    Run this autograder by running the following in the project's root directory.
        python -m pytest
    
    To run a specific test, run:
        python -m pytest -k test_load_data

    The score assigned by the autograder will be the grade, unless plagiarism or 
    other disqualifying behavior is discovered.
    """
    yield
    test_result = load_json('tests/test_result.json')
    rubric = load_json('tests/rubric.json')
    report = {
        'score': 0,
        'tests_passed': 0,
        'notes': {}
    }
    total = 0
    tests_passed = 0
    total_tests = 0

    
    for name, result in test_result.items():
        if name in rubric:
            if rubric[name]['weight'] == 'required':
                if not result:
                    report['score'] = 0
                    report['notes'][name] = (
                        f'FAIL - REQUIRED (automatic zero)'
                    )
                    total = 1
                    total_tests = 1
                    break
            else:
                dependencies_satisifed = True
                for dependency in rubric[name]['depends']:
                    if not test_result[dependency]:
                        dependencies_satisifed = False
                
                if result and dependencies_satisifed:
                    report['score'] += rubric[name]['weight']
                    report['tests_passed'] += 1
                    report['notes'][name] = (
                        f'PASS'
                    )
                else:
                    report['notes'][name] = (
                        f'FAIL'
                    )
                total += rubric[name]['weight']
                total_tests += 1

    report['score'] = int(np.ceil(100 * report['score'] / total))
    # print(
    #     f"Output of autograder\n"
    #     f"======================\n"
    #     f"# of tests:\t{report['tests_passed']}/{total_tests} tests passed\n"
    #     f"Overall score:\t{report['score']}/{100}"
    # )
    # print("======================")
    # for i, note in report['notes'].items():
    #     print(f'{note} {i}')
    # print("======================")
    save_json(report, 'tests/report.json')
    
def pytest_unconfigure(config):
    
    test_result = load_json('tests/test_result.json')
    rubric = load_json('tests/rubric.json')
    report = {
        'score': 0,
        'tests_passed': 0,
        'notes': {}
    }
    total = 0
    tests_passed = 0
    total_tests = 0

    
    for name, result in test_result.items():
        if name in rubric:
            if rubric[name]['weight'] == 'required':
                if not result:
                    report['score'] = 0
                    report['notes'][name] = (
                        f'FAIL - REQUIRED (automatic zero)'
                    )
                    total = 1
                    total_tests = 1
                    break
            else:
                dependencies_satisifed = True
                for dependency in rubric[name]['depends']:
                    if not test_result[dependency]:
                        dependencies_satisifed = False
                
                if result and dependencies_satisifed:
                    report['score'] += rubric[name]['weight']
                    report['tests_passed'] += 1
                    report['notes'][name] = (
                        f'PASS'
                    )
                else:
                    report['notes'][name] = (
                        f'FAIL'
                    )
                total += rubric[name]['weight']
                total_tests += 1

    report['score'] = int(np.ceil(100 * report['score'] / total))
    
    print = False
    if print == True:
        print('=========================================================')
        print('================ Output of autograder ===================')
        print('=========================================================')

        print(
            f"# of tests:\t{report['tests_passed']}/{total_tests} tests passed\n"
            f"Overall score:\t{report['score']}/{100}"
        )
        print("======================")
        for i, note in report['notes'].items():
            print(f'{note} {i}')
        print("======================")