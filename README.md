# 🧪 ISCAS Structural Simulator

### 📌 Course: Testability
**Instructor:** Dr. Shahin Hesabi  
**Contributors:** Zahra Mirzaei 

---

## 📄 Project Description

This project implements a **structural-level simulator** for **ISCAS benchmark combinational circuits**.  
It parses netlists written in the ISCAS format and simulates the circuit behavior gate-by-gate using Python.

The simulator supports a variety of logic gates and reads custom input values to compute the final logic state of all nodes.

---

## 📂 Repository Structure

```
.
├── iscas_structural_simulator.py   # Main Python script for simulation
├── sample_input.isc                # Example ISCAS-format circuit netlist (e.g., c17.isc)
├── input.txt                # Input values for simulation
├── final.txt                       # Simulation results
└── README.md                       # Project description
```

---

## 🛠 How to Use

1. Download an ISCAS-format `.isc` netlist file from a trusted source like:  
   [ISCAS-85 Benchmark Circuits](http://www.pld.ttu.ee/~maksim/benchmarks/iscas85/isc/)

2. Prepare an input file containing logic values in this format:

```
node_address value
...
```

3. Run the simulator:

```bash
python iscas_structural_simulator.py
```

4. Provide the required filenames when prompted.

5. The output will be saved in `final.txt`, showing each node’s logic value and stuck-at faults (if any).

---

## 🔧 Supported Logic Gates

- AND
- NAND
- OR
- NOR
- XOR
- XNOR
- NOT
- BUF
- FANOUT

---

## 📋 Sample Output

```
Node Address     Value
1                1
2                0
...
```

For each node, the simulator also reports:
- Address
- Type
- Fan-ins and fan-outs
- Fault information (stuck-at-0 / stuck-at-1)

---

## 🔗 Useful Resources

- [ISCAS Benchmark Info](https://web.eecs.umich.edu/~jhayes/iscas.restore/)
- [Netlist Downloads](http://www.pld.ttu.ee/~maksim/benchmarks/iscas85/isc/)
