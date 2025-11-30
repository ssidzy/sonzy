import os

def create_course_structure():
    # Define the base directory
    base_dir = "electronics-hw"
    
    # Define all sections and their subsections
    course_structure = {
        "Section 01 - Welcome to Electronics I": [
            "01 - Introduction",
            "02 - The Story of Electricity",
            "03 - What is Electricity",
            "04 - What is Electric Current",
            "05 - What is Electronics",
            "06 - Looking inside Electronic Devices"
        ],
        "Section 02 - Understanding Electricity": [
            "07 - What you will learn",
            "08 - Pondering the Wonder of Electricity",
            "09 - Atoms Introduction",
            "10 - Examining the Elements - Periodic Table",
            "11 - Charge and Electromagnetism",
            "12 - Conductors and Insulators",
            "13 - Electric Current Flow"
        ],
        "Section 03 - Simulator Tutorial": [
            "14 - Setting up the simulator",
            "15 - How to get started !"
        ],
        "Section 04 - FUNDAMENTALS": [
            "16 - So, what is voltage anyway",
            "17 - Direct Current(DC) vs Alternating Current(AC)",
            "18 - How to measure voltage and current in a circuit",
            "19 - Resistor Introduction",
            "20 - Resistors in Series & Parallel",
            "21 - Ohm's Law",
            "22 - What is voltage drop in an electric circuit",
            "23 - Voltage Divider",
            "24 - Voltage Divider under Load",
            "25 - Light Emitting Diode (LED)",
            "26 - Current Limiting Resistor with LED"
        ],
        "Section 05 - Kirchhoff's circuit laws": [
            "27 - Why we need Kirchhoff's circuit laws",
            "28 - Kirchhoff's Rules",
            "29 - Kirchhoff's Current Law",
            "30 - Kirchhoff's Voltage Law",
            "31 - Problem-Solving Strategy - Kirchhoff's Rules",
            "32 - Circuit Analysis using Kirchhoff's Rules - Part I",
            "33 - Circuit Analysis using Kirchhoff's Rules - Part II"
        ],
        "Section 06 - Electric Power P[W] Fundamentals": [
            "34 - Electric Power - Introduction",
            "35 - Wattage",
            "36 - Calculating Power",
            "37 - Resistor Power Ratings"
        ],
        "Section 07 - Alternating Current (AC)": [
            "38 - Why we get AC signal from the wall-socket",
            "39 - AC - Important Characteristics",
            "40 - Root mean square voltage (Vrms)"
        ],
        "Section 08 - Capacitors": [
            "41 - Capacitor Introduction",
            "42 - How a Capacitor is Made",
            "43 - Types of Capacitors",
            "44 - How a Capacitor Works (in a DC circuit)",
            "45 - Calculating Charge, Voltage, and Current",
            "46 - Capacitor in an AC circuit",
            "47 - Impedance and Reactance of a Capacitor",
            "48 - Caps w Various Frequencies (Impedance Overview)",
            "49 - Caps of Various Capacitances",
            "50 - Coupling capacitors",
            "51 - Decoupling capacitors",
            "52 - Why to place multiple bypass capacitors in parallel",
            "53 - Smoothing capacitors"
        ],
        "Section 09 - RC Time Constant": [
            "54 - RC Time Constant",
            "55 - RC Circuits - Charging,Discharging,Signal Filtering",
            "56 - Application Examples"
        ],
        "Section 10 - Inductors": [
            "57 - Inductor - Introduction",
            "58 - Types of Inductors",
            "59 - Inductors in Series and Parallel",
            "60 - Inductor Behavior in a DC circuit",
            "61 - What is back E.M.F and how to control it",
            "62 - Inductor Behavior in an AC circuit",
            "63 - Inductive Reactance",
            "64 - Inductors w Various Frequencies",
            "65 - Inductors of Various Inductances",
            "66 - Impedances of Same Magnitude",
            "67 - Series RLC Resonance",
            "68 - Transformers - (Step-Down, Step-Up, Isolation)",
            "69 - Long-Distance Power Transmission"
        ],
        "Section 11 - Diodes": [
            "70 - Diode Introduction",
            "71 - Operating Regions of a Diode",
            "72 - Looking into the datasheet",
            "73 - Types of Diodes",
            "74 - Current through a diode",
            "75 - Diode as voltage reference",
            "76 - Identifying the terminals of a real-life diode",
            "77 - Half-Wave Rectifier Circuit _w Filter Capacitor",
            "78 - Full-Wave Rectifier - Center Tapped and Diode Bridge",
            "79 - Voltage Multiplier, Voltage Doublet, Tripler",
            "80 - Signal Rectifier, Diode Gates, Diode Clamp circuits",
            "81 - Zener diodes and its applications"
        ],
        "Section 12 - More Circuits with Diodes !": [
            "82 - Diode Limiter (Clapping Circuit)",
            "83 - Clamper Circuit (DC Restoration)",
            "84 - Spike Generator (Using RC Circuit)",
            "85 - Voltage Doubler _ Tripler"
        ],
        "Section 13 - Input and Output Impedance of a Circuit": [
            "86 - Input Impedance of a Circuit",
            "87 - Output Impedance of a Circuit",
            "88 - Impedance Matching (Transmission Line)",
            "89 - How to measure the input impedance",
            "90 - How to measure the output impedance"
        ],
        "Section 14 - First order filters": [
            "91 - What is a filter",
            "92 - RC Low Pass Filter",
            "93 - RL Low Pass Filter",
            "94 - What is the -3db point",
            "95 - How to calculate filter response",
            "96 - Second order Low Pass Filter",
            "97 - High-pass RC filter",
            "98 - High-pass RL filter",
            "99 - Band-pass filter - Introduction",
            "100 - RLC Band-pass filter"
        ],
        "Section 15 - More Advanced Filters": [
            "101 - Band-Pass Filter - Review",
            "102 - Notch Filter and Twin-T Filter",
            "103 - L, T and π topology filters",
            "104 - Crossover Filter",
            "105 - Butterworth , Bessel , Chebyshev , Elliptic filter"
        ],
        "Section 16 - Radio and Signal Modulation": [
            "106 - What is a communication channel",
            "107 - What are Radio Waves",
            "108 - Introduction to Radio Communications Principles",
            "109 - How do repeaters work",
            "110 - Radio Transmission",
            "111 - Radio Receiver",
            "112 - The purpose of modulation",
            "113 - AM Modulation",
            "114 - AM Transmitter and Receiver Circuit",
            "115 - Types of Modulation - Part I",
            "116 - Types of Modulation - Part II",
            "117 - Types of Modulation - Part III"
        ],
        "Section 17 - Miscellaneous stuff": [
            "118 - Relays (Mechanical Relays and MOS FET Relays)",
            "119 - RC Differentiator",
            "120 - Wheatstone Bridge Explained",
            "121 - Series RLC (Oscillating vs Dumped)"
        ],
        "Section 18 - Transistors Fundamentals": [
            "122 - Why were transistors invented",
            "123 - Looking inside a transistor",
            "124 - Basic NPN transistor circuit",
            "125 - Basic PNP transistor circuit",
            "126 - What's the advantage of using a transistor as a switch",
            "127 - Operation Modes - Saturation",
            "128 - Operation Modes - Cut off",
            "129 - Operation Modes - Forward Active",
            "130 - Current Gain_Amplification Factor",
            "131 - How to counter the differences in β",
            "132 - Variations on a theme - High Side Switching",
            "133 - Pulse generator - part I",
            "134 - Pulse generator - part II",
            "135 - Pulse generator - part III (Adding Schmitt Trigger)",
            "136 - Emitter Follower",
            "137 - Impedance of sources and loads",
            "138 - How to build an emitter follower  - Part I",
            "139 - How to build an emitter follower  - Part II",
            "140 - Emitter follower drives high-power LED",
            "141 - Emitter Follower as Voltage Regulator"
        ],
        "Section 19 - Review + More Circuits with Transistors!": [
            "142 - Beginning - NPN vs PNP (Similarities + Differences)",
            "143 - NPN Transistor How it works (Diode Model)",
            "144 - PNP Transistor- How it works (Diode Model)",
            "145 - Emitter Follower (INPUT AND OUTPUT IMPEDANCE) Part 1",
            "146 - Emitter Follower (INPUT AND OUTPUT IMPEDANCE) Part 2",
            "147 - Input and Output Coupling Capacitor",
            "148 - Bypass Capacitor in Common-Emitter Amplifiers PART I",
            "149 - Bypass Capacitor in Common-Emitter Amplifiers PART II"
        ],
        "Section 20 - Transistor Circuits": [
            "150 - Current Source - Introduction",
            "151 - How to design a current source",
            "152 - How to design a common-emitter amplifier",
            "153 - Current Mirror",
            "154 - Differential amplifier - Part 1",
            "155 - Differential amplifier - Part 2"
        ],
        "Section 21 - Audio amplifier classes": [
            "156 - Decibel",
            "157 - Power amplifier classes - Introduction",
            "158 - Class A,B,AB,C,D - Theory",
            "159 - Simulation - PART I (Class A and introduction to Class B)",
            "160 - Simulation - PART 2 (Class B and AB)",
            "161 - Simulation - PART 3 (Class D)"
        ],
        "Section 22 - Other circuits using BJT": [
            "162 - Astable Multivibrator",
            "163 - Monostable Multivibrator",
            "164 - Bistable Multivibrator",
            "165 - Schmitt Trigger",
            "166 - Colpitts Oscillator (Postive Feedback explained)"
        ],
        "Section 23 - Linear Power Supply Design": [
            "167 - Power Supplies Introduction (Block Diagram of a Linear Power Supply)",
            "168 - How NOT to design a power supply",
            "169 - Emitter Follower using Darlington Pair",
            "170 - Transistor Based Power Supply (1.3V - 50V) Part I",
            "171 - Transistor Based Power Supply (1.3V - 50V) Part II",
            "172 - Split Power Supply Design (+12V & -12V)"
        ],
        "Section 24 - Operational Amplifier (Op-Amp) - Fundamentals": [
            "173 - Introduction (Op-Amp as Comparator)",
            "174 - Op-Amp Buffer Circuit",
            "175 - When a Circuit Needs Buffering",
            "176 - How to increase the current of a buffer circuit",
            "177 - Non-Inverting Amplifier",
            "178 - Inverting Amplifier",
            "179 - Single Ended Inverting Amplifier",
            "180 - Gain-BandWidth Product",
            "181 - Cascading Op-amps For Improved Bandwidth"
        ],
        "Section 25 - Op-Amp Arithmetic Circuits": [
            "182 - Inverting Op-Amp Adder",
            "183 - Non-Inverting Op-Amp Adder",
            "184 - What is the use of an op-amp adder",
            "185 - Differential amplifier _with and without improvement_",
            "186 - What are differential amplifier used for",
            "187 - Op-Amp Integrator PART I",
            "188 - Op-Amp Integrator PART II",
            "189 - Op-Amp Differentiator"
        ],
        "Section 26 - Op-Amp Based Precision Rectifiers": [
            "190 - Regular Rectifier vs Precision Rectifier",
            "191 - Basic Half-Wave Precision Rectifier",
            "192 - Gain Controller Precision Half-Wave Rectifier"
        ],
        "Section 27 - BONUS! - Common Op-Amp Based Circuits": [
            "193 - Peak Detector Circuit",
            "194 - I-V Converter",
            "195 - Building a Schmitt Trigger using Op-Amp"
        ],
        "Section 28 - Linear Voltage Regulator": [
            "196 - Linear Voltage Regulator ICs",
            "197 - LM317 Based Variable Power Supply",
            "198 - Different circuits that you can build with LM317",
            "199 - Building a linear voltage regulator"
        ],
        "Section 29 - MOSFETs": [
            "200 - Types of Transistors",
            "201 - MOSFET General Overview",
            "202 - N-channel Mostet (enhancement)"
        ],
        "Section 30 - N-channel MOSFET Characteristic Curve": [
            "203 - Cutoff Region",
            "204 - Ohmic_Linear Region",
            "205 - Saturation Region",
            "206 - Breakdown Region",
            "207 - DATASHEET REVIEW"
        ],
        "Section 31 - DC-to-DC Switching Converters": [
            "208 - Types of switching regulators",
            "209 - Buck Converter (Working Principle)",
            "210 - Buck Converter (Simulation + Datasheet)",
            "211 - Boost Converter (Working Principle)",
            "212 - Boost Converter (Simulation + Datasheet)",
            "213 - Linear vs Switching Regulator Efficiency"
        ]
    }
    
    # Create base directory
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        print(f"Created base directory: {base_dir}")
    else:
        print(f"Base directory already exists: {base_dir}")
    
    # Create all sections and files
    total_files = 0
    for section, subsections in course_structure.items():
        section_path = os.path.join(base_dir, section)
        
        # Create section directory
        if not os.path.exists(section_path):
            os.makedirs(section_path)
            print(f"Created section: {section}")
        
        # Create subsection files
        for subsection in subsections:
            file_path = os.path.join(section_path, f"{subsection}.txt")
            if not os.path.exists(file_path):
                with open(file_path, 'w', encoding='utf-8') as f:
                    # You can add initial content here if needed
                    f.write(f"# {subsection}\n\n")
                total_files += 1
            else:
                print(f"File already exists: {file_path}")
    
    print(f"\n✅ Course structure created successfully!")
    print(f"📁 Base directory: {base_dir}")
    print(f"📂 Total sections: {len(course_structure)}")
    print(f"📄 Total files created: {total_files}")
    
    # Print summary
    print(f"\n📊 Summary by section:")
    for section, subsections in course_structure.items():
        print(f"   {section}: {len(subsections)} files")

if __name__ == "__main__":
    create_course_structure()