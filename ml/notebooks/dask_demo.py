import dask.array as da
import time
import dask.dataframe as dd

start = time.time()
data = da.random.randint(1,100,1000)
stop = time.time()
tiempo = stop - start
print(type(data))
print(tiempo)

df = dd.io.from_dask_array(data)
print(type(data))
df.to_csv("values")
print("saved")

