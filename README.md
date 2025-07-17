# 📊 Radix Sort Visualizer

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python 3.x">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/UI-Tkinter-orange.svg" alt="Tkinter">
</div>

<div align="center">
  <img width="700" alt="Radix Sort Visualizer Screenshot" src="https://user-images.githubusercontent.com/your-username/radix-sort-visualizer/main/screenshot.png">
</div>

## 🔍 Overview

An interactive, educational tool that visualizes the Radix Sort algorithm step-by-step. This application helps students and developers understand how Radix Sort works by displaying each pass of the algorithm with detailed intermediate results.

## 🧮 What is Radix Sort?

Radix Sort is a non-comparative sorting algorithm that processes integers digit by digit. Unlike comparison-based algorithms (like Quick Sort or Merge Sort), Radix Sort:

- Has a time complexity of O(d*(n+k)), where d is the number of digits, n is the number of elements, and k is the range of input (10 for decimal digits)
- Is stable and efficient for integers and strings
- Works by sorting numbers based on individual digit positions, from least significant to most significant

## ✨ Features

- 📋 Step-by-step visualization of the Radix Sort algorithm
- 🔢 Support for arrays of any size with positive integers
- 📝 Detailed display of intermediate results after each pass
- 🔄 Dynamic calculation of required passes based on the largest number
- 🎯 Sample data loader for quick demonstrations
- 🧩 Clean, intuitive user interface

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- Tkinter (usually comes pre-installed with Python)

### Installation

#### Option 1: Clone and Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/radix-sort-visualizer.git
   cd radix-sort-visualizer
   ```

2. Set up a virtual environment:
   ```bash
   # Create a virtual environment
   python -m venv venv

   # Activate the virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Run the application:
   ```bash
   python run.py
   ```

#### Option 2: Install as a Package

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/radix-sort-visualizer.git
   cd radix-sort-visualizer
   ```

2. Install the package:
   ```bash
   pip install -e .
   ```

3. Run the application:
   ```bash
   radix-sort-visualizer
   ```

## 💻 How to Use

1. Enter the size of your array in the "Enter size of the array" field
2. Input your array elements (space-separated integers) in the "Enter the array" field
3. Click "Start Sorting" to begin the visualization
4. Observe each pass of the Radix Sort algorithm in the text area
5. Use "Reset" to clear all inputs and results
6. Try the "Load Sample" button for a quick demonstration

## 🔬 Understanding the Output

The visualizer shows:

1. The original unsorted array
2. Each pass of the algorithm, processing one digit position at a time
3. The intermediate state of the array after each pass
4. The final sorted array

## 🧪 Example

For the array `[170, 45, 75, 90, 802]`:

1. **First pass**: Sort by the 1's digit (rightmost)
   - Result: `[170, 90, 802, 45, 75]`

2. **Second pass**: Sort by the 10's digit
   - Result: `[802, 45, 170, 75, 90]`

3. **Third pass**: Sort by the 100's digit
   - Result: `[45, 75, 90, 170, 802]`

The final sorted array is `[45, 75, 90, 170, 802]`.

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- This project was created as an educational tool for understanding sorting algorithms
- Inspired by various algorithm visualization projects 