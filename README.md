# CryptoGrade 🛡️📚

## Overview 🌐

CryptoGrade brings the power of local grading to your fingertips! 🚀

 Designed to operate within Jupyter Notebooks, CryptoGrade allows assignments to be graded directly on the student's machine, eliminating the need for external grading servers. While this approach may not be impenetrable to a determined hacker, it's secure enough to make the average student think twice—doing the assignment just might be the easier option! 😂

## Installation 🛠️

To install CryptoGrade, you can use `pip` directly from its GitHub repository:

```bash
pip install git+https://github.com/thomaspluck/cryptograde.git
```

## Features 🌟

### RangeGrader 📏🔒

- **Grades numerical answers** within a specified range.
- Utilizes **Order-Preserving Encryption (OPE)** to provide a level of security to the grading process.
- Features **randomized salting** to further obscure the grading boundaries.
- **Special Features**:
    - **Adapts to Floating-Point Numbers**: While the underlying Order-Preserving Encryption (OPE) scheme is designed for integers, RangeGrader accommodates floating-point numbers through an optional scaling parameter. This parameter essentially quantizes the floating-point numbers into integers, where each integer step corresponds to the scale value.

### ChoiceGrader ✅🔒

- **Grades multiple-choice answers** with ease.
- Uses **SHA-256 hashing** to protect the correct answer.
- **Auto-generates a salt** for each new `ChoiceGrader` object to ensure unique hashes.

## Usage 📖

### Typical Workflow 👩‍🏫👨‍🎓

1. **Teacher-side**: A teacher creates a `RangeGrader` or `ChoiceGrader` object locally to define the grading criteria.
2. The teacher then saves this object using the `.save()` method to get a `.pkl`.
3. The saved file is included in the assignment package given to the student.

### Loading Graders 📤

On the student's end, the grader object is loaded from the saved file using the `.load()` method to perform grading.

```python
# Load the grader from the saved file
loaded_rg = RangeGrader.load('range_grader.pkl')
```

## Limitations ⚠️

While CryptoGrade employs some cryptographic techniques, it's not designed to be bulletproof. If someone spends enough time, they can probably crack it. However, the goal here is to make cheating more trouble than it's worth! 🤷‍♂️

## Contribute 🤝

Feel free to fork, open issues, or submit PRs. Any contributions are welcome! 🙏