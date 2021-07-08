# This is an example feature definition file

from google.protobuf.duration_pb2 import Duration

from feast import Entity, Feature, FeatureView, ValueType
from feast.data_source import FileSource

# Read data from parquet files. Parquet is convenient for local development mode. For
# production, you can use your favorite DWH, such as BigQuery. See Feast documentation
# for more info.
iris_data = FileSource(
    path="iris_example/data/iris.parquet",
    event_timestamp_column="event_timestamp",
)

# Define an entity for the driver. You can think of entity as a primary key used to
# fetch features.
iris_entity = Entity(name="iris_id", value_type=ValueType.INT64, description="driver id",)

# Our parquet files contain sample data that includes a driver_id column, timestamps and
# three feature column. Here we define a Feature View that will allow us to serve this
# data to our model online.
driver_hourly_stats_view = FeatureView(
    name="iris",
    ttl=None,
    entities=["iris_id"],
    features=[
        Feature(name="sepal_length", dtype=ValueType.FLOAT),
        Feature(name="sepal_width", dtype=ValueType.FLOAT),
        Feature(name="petal_length", dtype=ValueType.FLOAT),
        Feature(name="petal_width", dtype=ValueType.FLOAT),
        Feature(name="target", dtype=ValueType.STRING),
    ],
    online=True,
    input=iris_data,
    tags={},
)
