"""Minimal test for LAGC simulation."""
from lagc import LAGC

# Test small cluster only
print("Testing small cluster...")
sim = LAGC(ram_limit_gb=4, hardware='ideal')
sim.create_lattice('2d_cluster', 3, 3)  # Only 9 qubits
print(f"Lattice: {sim.n_qubits} qubits")

sim.apply_loss(0.1, seed=42)
info = sim.graph.get_graph_info()
print(f"Active: {info['n_active']}, Lost: {info['n_lost']}")

result = sim.run_simulation()
print(f"Fidelity: {result.fidelity:.4f}")
print(f"Time: {result.execution_time:.2f}s")
print("SUCCESS!")
