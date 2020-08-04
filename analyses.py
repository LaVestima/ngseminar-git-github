import numpy as np
import pandas as pd

data = pd.read_csv('raw_data_human.csv').set_index('miRname')

results = pd.DataFrame(p, index = dataCombined.index, columns = ['p'])

meanExpressionTreatment = data.groupby(level=['Treatment'], axis=1).get_group('Yes').mean(axis=1)
meanExpressionNoTreatment = data.groupby(level=['Treatment'], axis=1).get_group('No').mean(axis=1)

fc = 2.0 ** (-meanExpressionTreatment + meanExpressionNoTreatment)
results = results.join(pd.DataFrame(fc, columns = ['fc']))

results['logfc'] = np.log2(results['fc'])

results.to_excel('TSC_treatment_effect_all_groups_t-test.xlsx')
