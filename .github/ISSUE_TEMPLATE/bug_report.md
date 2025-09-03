---
name: 🐛 Bug Report
about: Report a bug in xSystem
title: '[BUG] '
labels: ['bug', 'needs-triage']
assignees: ''
---

## 🐛 **Bug Description**

**Clear and concise description of the bug:**

[Provide a clear description of what the bug is]

---

## 🔍 **Reproduction Steps**

**Steps to reproduce the behavior:**

1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior:**
[Describe what you expected to happen]

**Actual behavior:**
[Describe what actually happened]

---

## 📋 **Environment Details**

**Please complete the following information:**

- **xSystem Version:** [e.g., 0.0.2]
- **Python Version:** [e.g., 3.9.7]
- **Operating System:** [e.g., Ubuntu 20.04, Windows 10, macOS 12]
- **Architecture:** [e.g., x86_64, ARM64]
- **Installation Method:** [e.g., pip, conda, source]

---

## 🚨 **Aerospace/Defense Impact**

**Does this bug affect safety-critical systems?**

- [ ] **Critical:** Could impact flight safety or mission criticality
- [ ] **High:** Could affect operational systems
- [ ] **Medium:** Could affect performance or reliability
- [ ] **Low:** Minor functionality issue
- [ ] **None:** No safety or operational impact

**If safety-critical, describe the potential impact:**
[Explain how this bug could affect aerospace/defense applications]

---

## 📊 **Additional Context**

**Add any other context about the problem:**

- **Error Messages:** [Include any error messages or stack traces]
- **Logs:** [Include relevant log output]
- **Screenshots:** [If applicable, add screenshots]
- **Related Issues:** [Link to related issues if any]

---

## 🔧 **Attempted Solutions**

**What have you tried to resolve this issue?**

- [ ] Checked documentation
- [ ] Searched existing issues
- [ ] Updated to latest version
- [ ] Reinstalled dependencies
- [ ] Other: [Describe]

---

## 📁 **Code Example**

**If applicable, provide a minimal code example:**

```python
# Minimal example demonstrating the bug
from exonware.xsystem import SomeClass

# This code causes the bug
result = SomeClass().problematic_method()
```

---

## 🎯 **Priority Assessment**

**How urgent is this fix?**

- [ ] **Immediate:** System unusable, safety impact
- [ ] **High:** Significant functionality loss
- [ ] **Medium:** Some functionality affected
- [ ] **Low:** Minor inconvenience
- [ ] **Enhancement:** Could be improved

---

## 📋 **Compliance Impact**

**Does this affect compliance with standards?**

- [ ] **NASA Standards:** NASA-STD-8719.13, 8739.7, 8739.8
- [ ] **ECSS Standards:** ECSS-E-ST-40C, ECSS-Q-ST-80C
- [ ] **DO-178C:** Aerospace software certification
- [ ] **Security Standards:** Security compliance
- [ ] **None:** No compliance impact

---

## 🔍 **Debugging Information**

**Additional debugging details:**

```bash
# System information
python -c "import sys; print(sys.version)"
python -c "import platform; print(platform.platform())"

# xSystem information
python -c "import exonware.xsystem; print(exonware.xsystem.__version__)"

# Dependencies
pip list | grep -E "(exonware|xsystem)"
```

---

## 📝 **Additional Notes**

**Any other information that might be helpful:**

[Add any other context, ideas, or suggestions]

---

## ✅ **Checklist**

**Before submitting, ensure you have:**

- [ ] **Searched** existing issues for duplicates
- [ ] **Provided** clear reproduction steps
- [ ] **Included** environment details
- [ ] **Assessed** aerospace/defense impact
- [ ] **Provided** minimal code example (if applicable)
- [ ] **Checked** compliance impact
- [ ] **Included** debugging information

---

**Thank you for helping improve xSystem's reliability for aerospace and defense applications!**

**Issue Type:** Bug Report
**Priority:** [To be set by maintainers]
**Labels:** [To be set by maintainers]
