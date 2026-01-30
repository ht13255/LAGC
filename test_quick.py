"""Quick test for LAGC simulation."""
from lagc import LAGC

# Test 1: 2D Cluster
print("=" * 50)
print("Test 1: 2D Cluster State")
print("=" * 50)
sim = LAGC(ram_limit_gb=4, hardware='realistic')
sim.create_lattice('2d_cluster', 5, 5)
print(f"Lattice: {sim.n_qubits} qubits")
sim.apply_loss(0.1, seed=42)
info = sim.graph.get_graph_info()
print(f"Active: {info['n_active']}, Lost: {info['n_lost']}")
result = sim.run_simulation()
print(f"Fidelity: {result.fidelity:.4f}")
print(f"Time: {result.execution_time:.2f}s")
print("✓ 2D Cluster Test PASSED")

# Test 2: 3D RHG (smaller for speed)
print("\n" + "=" * 50)
print("Test 2: 3D RHG Lattice")
print("=" * 50)
sim = LAGC(ram_limit_gb=4, hardware='ideal')
sim.create_lattice('3d_rhg', 3, 3, 3)
print(f"Lattice: {sim.n_qubits} qubits, {sim.graph.get_edge_count()} edges")
sim.apply_loss(0.05, seed=42)
info = sim.graph.get_graph_info()
print(f"Active: {info['n_active']}, Lost: {info['n_lost']}")
result = sim.run_simulation()
print(f"Fidelity: {result.fidelity:.4f}")
print(f"Time: {result.execution_time:.2f}s")
print("✓ 3D RHG Test PASSED")

# Test 3: Loss Scan
print("\n" + "=" * 50)
print("Test 3: Loss Rate Scan")
print("=" * 50)
sim = LAGC(hardware='ideal', seed=42)
for p_loss in [0.0, 0.05, 0.1, 0.15, 0.2]:
    sim.reset()
    sim.create_lattice('2d_cluster', 4, 4)
    sim.apply_loss(p_loss)
    result = sim.run_simulation()
    bar = "█" * int(result.fidelity * 20)
    print(f"p={p_loss:.2f}: {result.fidelity:.4f} |{bar}")

print("✓ Loss Scan Test PASSED")

print("\n" + "=" * 50)
print("ALL TESTS PASSED!")
print("=" * 50)
