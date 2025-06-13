# export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
import time
from hy3dgen.shapegen import Hunyuan3DDiTFlowMatchingPipeline

start_time = time.time()
pipeline = Hunyuan3DDiTFlowMatchingPipeline.from_pretrained('tencent/Hunyuan3D-2')
mesh = pipeline(image='benormal.png')[0]
mesh.export('benormal.obj')
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")

start_time = time.time()
mesh = pipeline(image='what.png')[0]
mesh.export('what.obj')
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")