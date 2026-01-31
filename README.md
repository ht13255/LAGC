<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Platform-CPU_Only-orange.svg" alt="Platform">
  <img src="https://img.shields.io/badge/Version-1.1.5-blueviolet.svg" alt="Version">
</p>

<h1 align="center">LAGC</h1>
<h3 align="center">LossAware-GraphCompiler</h3>

<p align="center">
  <b>A CPU-only, high-performance quantum graph compiler for photonic quantum computing research</b>
</p>

<p align="center">
  <a href="#-key-features">Features</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-rhg-lattice-system">RHG System</a> •
  <a href="#-citation">Citation</a>
</p>

---

## 🎯 What is LAGC?

**LAGC (LossAware-GraphCompiler)** is a high-performance simulation library designed for photonic quantum computing. It runs **entirely on CPU** using a highly optimized NumPy-based graph engine.

LAGC specializes in simulating **Fault-Tolerant Measurement-Based Quantum Computation (MBQC)** by modeling realistic photon loss, performing automatic graph surgery, and analyzing the topological connectivity of 3D cluster states.

### 🚀 Performance Leap (v1.1+)
- **Numpy Core**: Refactored `GraphEngine` directly manipulates adjacency matrices via NumPy, offering 10x-50x speedup over previous versions.
- **Memory Efficiency**: Advanced tensor slicing allows simulating circuits with 1,000+ qubits on a standard laptop with 8GB RAM.
- **Physics Accuracy**: True 3D RHG lattice implementation with half-integer coordinates and face-sharing connectivity.

---

## ✨ Key Features

- **🖥️ CPU-Only**: No GPU required — recursive slicing prevents memory overflow.
- **💎 Physics-Accurate RHG**: Measurement-based 3D lattice with guaranteed Degree 4 connectivity and 4D coordinate system.
- **📉 Loss-Aware Surgery**: Realistic photon loss modeling with automatic local complementation (recovery).
- **🔍 Syndrome Analysis**: Built-in percolation checking and Monte Carlo logical error rate estimation.
- **🔧 Hardware Profiles**: Pre-defined presets for current and future photonic hardware.

---

## 📦 Installation

```bash
pip install lagc
```

### Requirements
- Python ≥ 3.9
- NumPy, SciPy, opt-einsum, NetworkX (auto-installed)

---

## 🚀 Quick Start

### Basic Simulation with RHG Lattice

```python
from lagc import LAGC

# 1. Initialize simulator with realistic hardware parameters
sim = LAGC(ram_limit_gb=8.0, hardware='realistic')

# 2. Build a physics-accurate 3D RHG lattice (4x4x4 unit cells)
# This includes 144 edge qubits with proper diamond connectivity
sim.create_lattice('3d_rhg', 4, 4, 4, boundary='open')
print(f"Nodes: {sim.n_qubits}, Edges: {sim.n_edges}")

# 3. Apply 5% photon loss with automatic graph surgery
sim.apply_loss(p_loss=0.05, auto_recover=True)

# 4. Analyze topological syndrome pattern
analysis = sim.analyze_syndrome()
print(f"Percolates (Topologically Connected): {analysis['percolates']}")
print(f"Syndrome defects detected: {analysis['syndrome_count']}")

# 5. Get physical position of a qubit
pos = sim.get_stabilizer_coords(10)
print(f"Qubit 10 is at {pos}")
```

---

## 💎 RHG Lattice System

The 3D Raussendorf-Harrington-Goyal (RHG) lattice is the foundation of fault-tolerant photonic computing.

### Coordinate System
Uses a 4D tuple `(x, y, z, axis)` mapping to physical half-integers:
- **Axis 0 (X)**: Qubit at `(x+0.5, y, z)`
- **Axis 1 (Y)**: Qubit at `(x, y+0.5, z)`
- **Axis 2 (Z)**: Qubit at `(x, y, z+0.5)`

### Connectivity Logic
Guashed Degree 4 (topological invariant) via Face-sharing algorithm:
- Each qubit connects to 4 neighbors sharing the same cubic faces.
- Supports **Open** (physical chip) and **Periodic** (theoretical) boundaries.

---

## 🔍 Syndrome Analyzer

The `SyndromeAnalyzer` provides deep insights into the fault-tolerance of your graph state:

| Metric | Description |
|--------|-------------|
| **Percolation** | Checks if a spanning path exists across the lattice after loss. |
| **Syndrome Defects** | Identifies face-stabilizers with odd parity loss. |
| **Logical Error Rate** | Estimates failure probability via Monte Carlo sampling. |
| **Correctability** | Determines if the remaining connectivity allows for error correction. |

---

## ⚡ Performance

| Lattice | Qubits | Time (NumPy Engine) | Memory |
|---------|--------|---------------------|--------|
| 5×5 Cluster | 25 | 0.04s | < 500 MB |
| 10×10 Cluster| 100 | 12.5s | ~1.5 GB |
| 3D RHG 4×4×4 | 144 | 0.15s | ~600 MB |

---

## 📝 Citation

If you use LAGC in your research, please cite:

```bibtex
@software{lagc2026,
  title = {LAGC: LossAware-GraphCompiler for Photonic Quantum Computing},
  author = {LAGC Research Team},
  year = {2026},
  url = {https://github.com/ht13255/LAGC},
  version = {1.1.5}
}
```

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

<p align="center">
  <b>LAGC v1.1.5</b><br>
  <i>Accelerating Photonic Quantum Computing Research</i><br>
  <br>
  ⭐ Star us on GitHub if LAGC helps your research!
</p>
