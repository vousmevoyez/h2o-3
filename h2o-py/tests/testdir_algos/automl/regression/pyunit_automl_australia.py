from __future__ import print_function
import sys, os
sys.path.insert(1, os.path.join("..","..","..",".."))
import h2o
from tests import pyunit_utils
from h2o.automl import H2OAutoML

def australia_automl():

    train = h2o.import_file(path=pyunit_utils.locate("smalldata/extdata/australia.csv"))

    build_control = {
        'stopping_criteria': {
            'stopping_rounds': 3,
            'stopping_tolerance': 0.001
        }
    }
    aml = H2OAutoML(max_runtime_secs = 30,build_control=build_control)
    aml.train(y="runoffnew", training_frame=train)

if __name__ == "__main__":
    pyunit_utils.standalone_test(australia_automl)
else:
    australia_automl()