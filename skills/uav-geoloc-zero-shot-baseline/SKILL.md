---
name: uav-geoloc-zero-shot-baseline
description: Use when benchmarking place-recognition or cross-view CNNs (ResNet, MixVPR, CAMP) zero-shot on UAV-to-satellite datasets (AnyVisLoc, UAV-VisLoc) and reporting recall plus distance bands. Method, data layout, traps.
---
# Zero-shot UAV to satellite retrieval baseline

**Method:** embed the query and the map tiles with the same preprocessing, cosine similarity, rank; predicted position = centre of the top-1 tile.

- **AnyVisLoc layout** (one zip per scene): `Scene_XX/L??_reference.json` (map_path, map_resolution m/px, map_origin_local), `satellite_map.png`, `aerial_map.png`, per-image `L??_NNNN.npz` (image, K, xyz, euler_deg = roll, pitch, yaw). No lat/lon: a local metric frame. Scenes are under 1 km across, so a 5 km search window is the whole map.
- **Ground truth** is the camera view centre: x + z*tan(pitch)*sin(yaw), y - z*tan(pitch)*cos(yaw) (pitch from nadir). Map pixel = (x - origin) / resolution.
- **Tile size** = min(image side) * GSD, with GSD = (z / abs(cos(pitch))) / fx; 50 percent overlap; drop tiles under 40 percent non-black. A fixed 512 m tile does not fit low-altitude data.
- **Yaw alignment** helps models not trained for rotation a lot (MixVPR Recall@1 roughly doubled) and barely helps CAMP. Rotate the query clockwise by yaw (cv2 angle = -yaw) and keep the inscribed square. Report raw and aligned as separate protocols.
- **CAMP:** use the dataset repo's loader (ConvNeXt-B 384, University-1652 weights; guard `sys.argv` because its config parses argv); feature = `output[-2]`, fp16 autocast, L2 normalise. **MixVPR:** backbone with `layers_to_crop=[4]` plus aggregator (in_channels 1024, 20x20, out 1024, mix_depth 4, rows 4), load with `strict=True`.
- **Metrics:** Recall@K = rank of the tile nearest the true centre; error bands on the top-1 tile centre; exclude queries whose truth lies outside the map; print the tile-spacing floor (`best_possible_median_m`) so the 100 m band is read correctly.
- **Sanity:** run 20 queries first; expect CAMP > MixVPR > ResNet and yaw alignment to help. A tiny scene saturates Recall@10, so never headline small scenes alone. UAV-VisLoc differs (lat/lon, 0.3 m/px satellite maps, high altitude); its Drive downloads hit quota limits (`download-from-gdrive-onedrive-blocked`).
- Use a modern CUDA torch rather than the repos' pinned old versions; import only their model files (`wsl-torch-cu128-env-setup`).
