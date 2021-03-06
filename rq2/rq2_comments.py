#!/usr/bin/python3 -u
'''
Research Question 2:
Run Recursive Feature Elimination (RFE) for the prediction of 'Target-CommentsCount'
'''

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.feature_selection import RFECV
from sklearn.model_selection import PredefinedSplit
from dataset import Dataset

####################################################################################################
#                                                                                                  #
# Configuration for Research Questions 2:                                                          #
# - Path to file with all-time dataset in CSV format                                               #
# - Name of training and test sets used                                                            #
# - Target Name:  Target-CommentsCount                                                             #
#                                                                                                  #
####################################################################################################

DATASET_CSV_PATH = 'raw_dataset.csv'

TRAINING_SET_NAME = 'training-Y1'

TEST_SET_NAME = 'test-T1a'

TARGET_COLUMN_NAME = 'Target-CommentsCount'

# all features (F1-F12)
EXECUTIONS_FEATURES = ['F1-ChangedLOC', 'F2-SameTeam', 'F3-SameLocation', 'F4-IsMaintainer',
                       'F5-ModuleReviewXp', 'F6-ModuleModifXp', 'F7-TeamReviewXp',
                       'F8-TeamModifXp', 'F9-FileReviewXp', 'F10-FileModifXp',
                       'F11-OngoingAsAuthor', 'F12-OngoingAsReviewer']

BASE_LEARNERS = {
    'Random Forest': RandomForestRegressor(random_state=0, n_estimators=150, min_samples_leaf=10, criterion='mse', max_features=None, max_depth=None),
}

METRICS = ['r2', 'neg_root_mean_squared_error']

####################################################################################################
#                                                                                                  #
# Run Research Question 2 tests.                                                                   #
# Results are written to terminal only.                                                            #
#                                                                                                  #
####################################################################################################

# Load training and test sets
dataset = Dataset(DATASET_CSV_PATH)
training_df, test_df = dataset.get_training_and_test_by_name(
    TRAINING_SET_NAME, TEST_SET_NAME, only_with_participation=True)

exec_training_features = training_df.reindex(columns=EXECUTIONS_FEATURES)
exec_training_target = training_df[TARGET_COLUMN_NAME]
exec_test_features = test_df.reindex(columns=EXECUTIONS_FEATURES)
exec_test_target = test_df[TARGET_COLUMN_NAME]

# scale
scaler = StandardScaler()
scaler.fit(exec_training_features)
exec_training_features = scaler.transform(exec_training_features)
exec_test_features = scaler.transform(exec_test_features)

# configure training and test splitting for RFECV
training_and_test_features = np.concatenate((exec_training_features, exec_test_features), axis=0)
training_and_test_target = np.concatenate((exec_training_target, exec_test_target), axis=0)
test_fold = [-1] * len(exec_training_target) + [0] * len(exec_test_target)
ps = PredefinedSplit(test_fold)

# Test for each base learner with different scoring metrics
for metric in METRICS:
    for learner_name, learner in BASE_LEARNERS.items():
        print('\n\nComputing RFECV for {} using score {}'.format(learner_name, metric))
        rfe = RFECV(learner, min_features_to_select=1, verbose=10, cv=ps, scoring=metric)
        fit = rfe.fit(training_and_test_features, training_and_test_target)
        print("\tNum Features: %d" % fit.n_features_)
        print("\tSelected Features: %s" % fit.support_)
        print("\tFeature Ranking: %s" % fit.ranking_)
        try:
            print("\tImportance: {}".format(fit.estimator_.feature_importances_))
        except AttributeError:
            print("\tImportance: Not found")
        except RuntimeError:
            print("\tImportance: Not found")
        print("\tGrid: %s" % str(fit.grid_scores_))
