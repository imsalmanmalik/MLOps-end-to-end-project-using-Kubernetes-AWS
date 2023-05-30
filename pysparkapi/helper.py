from pyspark.sql import functions as F
import pickle
from pyspark.ml import PipelineModel
from pyspark.ml.classification import RandomForestClassificationModel
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType, DoubleType

# read model objects saved from the training process

char_labels = PipelineModel.load('/deploy/char_label_model.h5')
assembleModel = PipelineModel.load('/deploy/assembleModel.h5')
clf_model = RandomForestClassificationModel.load('/deploy/clf_model.h5')

with open('/deploy/file.pkl','rb') as handle:
	features_list, char_vars, num_vars = pickle.load(handle)
	

def rename_columns(df, char_vars):
	mapping = dict(zip([i + '_index' for i in char_vars], char_vars))
	df = df.select([F.col(c).alias(mapping.get(c,c)) for c in df.columns])
	return df
	

def score_new_df(scoredf):
	X = scoredf.select(features_list)
	X = char_labels.transform(X)
	X = X.select([c for c in X.columns if c not in char_vars])
	X = rename_columns(X, char_vars)
	final_X = assembleModel.transform(X)
	final_X.cache()
	pred = clf_model.transform(final_X)
	pred.cache()
	split_udf = udf(lambda value: value[1].item(), DoubleType())
	pred = pred.select('prediction', split_udf('probability') \
						.alias('probability'))
						
	return pred 
	