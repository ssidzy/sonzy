# Electronics Study Sheet Index

## Available Sections & Topics

### Section 01 - Welcome to Electronics I
- [x] 01 - Introduction
- [x] 02 - The Story of Electricity
- [x] 03 - What is Electricity
- [x] 04 - What is Electric Current
- [x] 05 - What is Electronics
- [x] 06 - Looking inside Electronic Devices

### Section 02 - Understanding Electricity
- [x] 07 - What you will learn
- [x] 08 - Pondering the Wonder of Electricity
- [x] 09 - Atoms Introduction
- [x] 10 - Examining the Elements - Periodic Table
- [x] 11 - Charge and Electromagnetism
- [x] 12 - Conductors and Insulators
- [x] 13 - Electric Current Flow

### Section 03 - Simulator Tutorial
- [ ] 14 - Setting up the simulator
- [ ] 15 - How to get started !

### Section 04 - FUNDAMENTALS
- [ ] 16 - So, what is voltage anyway
- [ ] 17 - Direct Current(DC) vs Alternating Current(AC)
- [ ] 18 - How to measure voltage and current in a circuit
- [ ] 19 - Resistor Introduction
- [ ] 20 - Resistors in Series & Parallel
- [ ] 21 - Ohm's Law

### Section 05 - Kirchhoff's circuit laws

### Section 06 - Electric Power P[W] Fundamentals

### Section 07 - Alternating Current (AC)

### Section 08 - Capacitors

### Section 09 - RC Time Constant

### Section 10 - Inductors

### Section 11 - Diodes

### Section 12 - More Circuits with Diodes !

### Section 13 - Input and Output Impedance of a Circuit

### Section 14 - First order filters

### Section 15 - More Advanced Filters

### Section 16 - Radio and Signal Modulation

### Section 17 - Miscellaneous stuff

### Section 18 - Transistors Fundamentals

### Section 19 - Review + More Circuits with Transistors!

### Section 20 - Transistor Circuits

### Section 21 - Audio amplifier classes

### Section 22 - Other circuits using BJT

### Section 23 - Linear Power Supply Design

### Section 24 - Operational Amplifier (Op-Amp) - Fundamentals

### Section 25 - Op-Amp Arithmetic Circuits

### Section 26 - Op-Amp Based Precision Rectifiers

### Section 27 - BONUS! - Common Op-Amp Based Circuits

### Section 28 - Linear Voltage Regulator

### Section 29 - MOSFETs

### Section 30 - N-channel MOSFET Characteristic Curve

### Section 31 - DC-to-DC Switching Converters

---

## Usage Instructions

1. Each topic can be generated as a one-page study sheet using `main.tex`
2. Check the box [ ] when a study sheet is completed for that topic
3. Topic names are extracted from .txt filenames in each section folder
4. Section numbers and names are from the folder structure

## Study Sheet Generation Workflow

1. Choose a topic from the index above
2. Add content to the corresponding .txt file
3. Update `main.tex` with topic and section information
4. Populate the four main sections:
   - TL;DR (The Gist)
   - Detailed Explanation
   - Practical Example & Numerical
   - Key Points (Interview Focus)
5. Compile with `pdflatex main.tex`
6. Check off the topic in this index
