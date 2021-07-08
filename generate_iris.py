from sklearn.datasets import load_iris
import pandas as pd
import datetime
from feast import FeatureStore


iris = load_iris()
df = pd.DataFrame(iris['data'], columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
df['target'] = iris['target']
df['iris_id'] = df.index

# add event_timestamp
df['event_timestamp'] = pd.to_datetime(datetime.datetime.now())
df.to_parquet("iris_example/data/iris.parquet")

store = FeatureStore("./iris_example")

entity_df = pd.DataFrame({
    'iris_id':[1],
    'event_timestamp':[pd.to_datetime(datetime.datetime.now())]
})

training_df = store.get_historical_features(
    entity_df=entity_df,
    feature_refs=[
        'iris:sepal_length',
        'iris:target'
    ]
)

print(training_df.to_df())