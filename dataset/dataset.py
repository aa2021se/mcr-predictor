#!/usr/bin/python3 -u
'''
Helper functions and classes to get training and test sets.
'''

import pandas as pd


def get_dataset_periods(dataset_name):
    '''For a given dataset referenced by its name, get the list of periods
    that need to be evaluated, with a granularity of 1 month. '''

    datasets = {
        'test-T1a': ['2019-01'],
        'test-T1': ['2019-01', '2019-02', '2019-03'],
        'test-T2': ['2018-10', '2018-11', '2018-12'],
        'test-T3': ['2018-07', '2018-08', '2018-09'],
        'test-T4': ['2018-04', '2018-05', '2018-06'],
        'test-T5': ['2018-01', '2018-02', '2018-03'],
        'test-S1': ['2019-01', '2019-02', '2019-03'],
        'test-S2': ['2018-10', '2018-11', '2018-12'],
        'test-S3': ['2018-07', '2018-08', '2018-09'],
        'test-S4': ['2018-04', '2018-05', '2018-06'],
        'test-S5': ['2018-01', '2018-02', '2018-03'],
        'test-N1': ['2019-01', '2019-02', '2019-03'],
        'test-N2': ['2018-10', '2018-11', '2018-12'],
        'test-N3': ['2018-07', '2018-08', '2018-09'],
        'test-N4': ['2018-04', '2018-05', '2018-06'],
        'test-N5': ['2018-01', '2018-02', '2018-03'],
        'test-Y1': ['2019-01', '2019-02', '2019-03'],
        'test-Y2': ['2018-10', '2018-11', '2018-12'],
        'test-Y3': ['2018-07', '2018-08', '2018-09'],
        'test-Y4': ['2018-04', '2018-05', '2018-06'],
        'test-Y5': ['2018-01', '2018-02', '2018-03'],
        'training-T1': ['2018-10', '2018-11', '2018-12'],
        'training-T2': ['2018-07', '2018-08', '2018-09'],
        'training-T3': ['2018-04', '2018-05', '2018-06'],
        'training-T4': ['2018-01', '2018-02', '2018-03'],
        'training-T5': ['2017-10', '2017-11', '2017-12'],
        'training-S1': ['2018-07', '2018-08', '2018-09',
                        '2018-10', '2018-11', '2018-12'],
        'training-S2': ['2018-04', '2018-05', '2018-06',
                        '2018-07', '2018-08', '2018-09'],
        'training-S3': ['2018-01', '2018-02', '2018-03',
                        '2018-04', '2018-05', '2018-06'],
        'training-S4': ['2017-10', '2017-11', '2017-12',
                        '2018-01', '2018-02', '2018-03'],
        'training-S5': ['2017-07', '2017-08', '2017-09',
                        '2017-10', '2017-11', '2017-12'],
        'training-N1': ['2018-04', '2018-05', '2018-06',
                        '2018-07', '2018-08', '2018-09',
                        '2018-10', '2018-11', '2018-12'],
        'training-N2': ['2018-01', '2018-02', '2018-03',
                        '2018-04', '2018-05', '2018-06',
                        '2018-07', '2018-08', '2018-09'],
        'training-N3': ['2017-10', '2017-11', '2017-12',
                        '2018-01', '2018-02', '2018-03',
                        '2018-04', '2018-05', '2018-06'],
        'training-N4': ['2017-07', '2017-08', '2017-09',
                        '2017-10', '2017-11', '2017-12',
                        '2018-01', '2018-02', '2018-03'],
        'training-N5': ['2017-04', '2017-05', '2017-06',
                        '2017-07', '2017-08', '2017-09',
                        '2017-10', '2017-11', '2017-12'],
        'training-Y1': ['2018-01', '2018-02', '2018-03',
                        '2018-04', '2018-05', '2018-06',
                        '2018-07', '2018-08', '2018-09',
                        '2018-10', '2018-11', '2018-12'],
        'training-Y2': ['2017-10', '2017-11', '2017-12',
                        '2018-01', '2018-02', '2018-03',
                        '2018-04', '2018-05', '2018-06',
                        '2018-07', '2018-08', '2018-09'],
        'training-Y3': ['2017-07', '2017-08', '2017-09',
                        '2017-10', '2017-11', '2017-12',
                        '2018-01', '2018-02', '2018-03',
                        '2018-04', '2018-05', '2018-06'],
        'training-Y4': ['2017-04', '2017-05', '2017-06',
                        '2017-07', '2017-08', '2017-09',
                        '2017-10', '2017-11', '2017-12',
                        '2018-01', '2018-02', '2018-03'],
        'training-Y5': ['2017-01', '2017-02', '2017-03',
                        '2017-04', '2017-05', '2017-06',
                        '2017-07', '2017-08', '2017-09',
                        '2017-10', '2017-11', '2017-12'],
    }

    try:
        return datasets[dataset_name]
    except KeyError as err:
        print('Dataset name {} was not found. Error: {}'.format(dataset_name, err))
        raise


class Dataset(object):
    '''A helper class to get training and test sets by their names or execution names.
    The full dataset is loaded from a file provided to the constructor and any subsequent
    call accesses data already loaded in the memory.'''

    _raw_data = None
    _csv_path = None

    def __init__(self, csv_path):
        '''Constructor that loads data from a CSV file with the full dataset for all periods.'''

        self._csv_path = csv_path

        with open(self._csv_path, 'r') as csvfile:
            print('Loading dataset from {} ...'.format(self._csv_path))

            self._raw_data = pd.read_csv(csvfile, header=0)

        print('Loaded data with columns:')
        for column in self._raw_data.columns.values:
            print('\t{}'.format(column))

    def get_training_and_test_by_exec_name(self, exec_name, only_with_participation=False):
        '''Get a tuple with training and test sets for a given execution referenced by its name;
        for instance: T1, S2, Y5.'''

        training_set_name = 'training-{}'.format(exec_name)
        test_set_name = 'test-{}'.format(exec_name)
        return self.get_training_and_test_by_name(training_set_name, test_set_name, only_with_participation)

    def get_training_and_test_by_name(self, training_set_name, test_set_name, only_with_participation=False):
        '''Get a tuple with training and test sets specified by their names.'''

        print('Getting datasets: {}, {}'.format(training_set_name, test_set_name))
        training_periods = get_dataset_periods(training_set_name)
        test_periods = get_dataset_periods(test_set_name)

        # filter by period
        training_df = self._raw_data[self._raw_data['Period'].isin(training_periods)]
        test_df = self._raw_data[self._raw_data['Period'].isin(test_periods)]

        if only_with_participation is True:
            print("Shape of training set before: " + str(training_df.shape))
            print("Shape of test set before: " + str(test_df.shape))
            training_df = training_df[training_df['Target-HaveParticipation'].eq(True)]
            test_df = test_df[test_df['Target-HaveParticipation'].eq(True)]
            print("Shape of training set after: " + str(training_df.shape))
            print("Shape of test set after: " + str(test_df.shape))

        # drop unused columns
        training_df = training_df.drop(columns=['Period', 'Ref-UniqueKey'])
        test_df = test_df.drop(columns=['Period', 'Ref-UniqueKey'])

        print("Shape of training set {}: {}".format(training_set_name, str(training_df.shape)))
        print("Shape of test set {}: {}".format(test_set_name, str(test_df.shape)))

        return (training_df, test_df)
