from core.remesh import calc_vertex_normals
from core.opt import MeshOptimizer
from util.func import load_obj, make_sphere,make_star_cameras, normalize_vertices, save_obj, save_images
from util.render import NormalsRenderer
from tqdm import tqdm
from util.snapshot import snapshot
try:
    from util.view import show
except:
    show = None

import time     
    
fname = 'data/lucy.obj'

V,F =  load_obj(fname)
#V = normalize_vertices(V)

opt = MeshOptimizer(V,F, edge_len_lims=(0.99,1.01))
#opt = MeshOptimizer(V,F)

print(f"Input Mesh #Faces= {F.size()[0]}, #Verices= {V.size()[0]}")

start_time = time.time()
for i in range(1, 4):
    print(f"\n iter{i}")
    V,F = opt.remesh()
    
end_time = time.time()
duration = end_time - start_time
print(f"Remeshing took {duration * 1000:.3f} milliseconds")
print(f"Output Mesh #Faces= {F.size()[0]}, #Verices= {V.size()[0]}")

save_obj(V,F,'./out/result.obj')