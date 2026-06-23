# Fingerprint-Bloom

A probabilistic device authentication framework built in pure Python. Designed for edge security networks, this engine implements a custom **Bloom Filter bit-array** to check incoming device connections instantly, avoiding high-latency cloud database lookups.

## ⚡ Probabilistic Performance Metrics
* **Space Complexity:** Fixed bit-allocation size $O(M)$, bypassing the need to store raw device signature strings.
* **Time Complexity:** Constant-time $O(K)$ lookups, where $K$ is the number of hash operations.
* **Error Margin:** Guaranteed zero False Negatives; any rejected device is 100% untrusted.
