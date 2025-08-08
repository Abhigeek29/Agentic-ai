# AI‐based Code Authenticity and Feedback System

## 🧠 Project Overview

**Title**: AI‐based Code Authenticity and Feedback System  
**Goal**: To create an intelligent platform that analyzes code to verify originality/authenticity, identify coding convention compliance, and deliver actionable feedback to developers.

---

## 📚 Background & Rationale

Modern development workflows are increasingly impacted by AI-generated code and code copied from online sources. This raises concerns about:

- **Plagiarism**
- **Inconsistent coding style**
- **Low maintainability**

Manual code reviews are costly, error-prone, and time-consuming. Previous tools like **NATURALIZE** and **AUGER** have demonstrated the potential of ML in learning project-specific styles and generating automated feedback.

This system aims to **merge code quality assurance with developer education**, leveraging recent advancements in machine learning and code analysis.

---

## 🎯 Key Objectives

1. **Authenticity Detection**  
   - Identify copied or AI-generated code using stylometry, AST analysis, and similarity detection.
2. **Style Learning & Enforcement**  
   - Learn and enforce team-specific coding styles including naming conventions, formatting, and usage patterns.
3. **Automated Feedback Generation**  
   - Generate natural-language feedback on code quality, logic, security, and maintainability using fine-tuned ML models.
4. **Trustworthy Feedback Loop**  
   - Provide explanations and community signals to foster trust and relevance in feedback.

---

## 🏗️ System Architecture

- **Code Ingestion**: Accepts code via Git hooks, CI pipeline, or IDE plugin.
- **Authenticity Engine**: Analyzes code using stylometry, lexical features, and public corpus comparison.
- **Style Learner**: Trains on project history to infer conventions and flag inconsistencies.
- **Feedback Generator**: LLM-based model generates human-like review comments during pull requests.
- **User Interface**: Includes IDE plugin and web dashboard with interactive feedback and override controls.

---

## 💡 Use Cases & Impact

- Maintain consistent and high-quality codebases.
- Discourage plagiarism and unreviewed AI code usage.
- Accelerate developer onboarding through meaningful feedback.
- Reduce human reviewer workload, allowing focus on high-level architecture.

---

## ⚙️ Technical Stack & Research Foundation

- **ML Models**: Stylometric analyzers, code embeddings, Transformer-based LLMs.
- **Data Sources**: Private repositories, open-source code, and AI-generated datasets.
- **Evaluation Metrics**:
  - Suggestion accuracy
  - Authenticity flag precision
  - Developer satisfaction with feedback

---

## 🗓️ Project Phases & Timeline

### 🔍 Research & Planning
- Study existing tools like NATURALIZE and AUGER.
- Finalize scope, architecture, and stack (Python, LLM APIs).
- Implement initial code ingestion module.

### 🧱 Core Development
- Build authenticity detection (code similarity + stylometry).
- Train basic style learner on project code samples.
- Start feedback generation (rule-based + ML components).

### 🧪 Integration & Testing
- Finalize LLM-based feedback engine.
- Create code review dashboard/interface.
- Conduct internal testing and feedback collection.

### 📘 Finalization & Reporting
- Refine outputs and UX based on test results.
- Write full documentation and user guide.
- Prepare for presentation, demo, and submission.

---

## 🚧 Risks & Mitigations

- **False Positives**: Manual confirmation thresholds and adjustable sensitivity.
- **Model Drift**: Allow retraining and team-specific overrides.
- **Over-reliance on AI**: Offer clear explanations, transparency, and disclaimers.

---

## 🚀 Scalability & Extensions

- Add support for multiple programming languages.
- Enable learning analytics for code evolution.
- Integrate with modern AI-assisted development tools and workflows.

---

## ✅ Conclusion

This project unifies **authenticity detection**, **style consistency**, and **intelligent feedback** into a single system. It empowers development teams to:
- Maintain integrity
- Accelerate learning
- Improve code quality and consistency

---

## ⚠️ Note

> If the system is not responding as expected, the API key limit may have been reached. Please try again after 24 hours.

---

=======
# 🧠 Agentic AI Code Mentor

> 🌟 *Empowering Education Through Code Feedback*  
> Contributing to **UN SDG 4: Quality Education**

Agentic AI is a smart code analysis and feedback tool designed to help learners and developers improve their programming skills. Using advanced AI models like **Gemini** and **OpenAI**, it provides intelligent code analysis, highlights errors, and offers actionable suggestions to improve your code quality.

---

## ✨ Features

- ✅ **Intuitive UI** – Clean and user-friendly interface to paste and analyze code.
- 🤖 **Intelligent Analysis** – Understands code logic using LLMs.
- 🐞 **Error Detection** – Detects syntax errors, logical bugs, and common pitfalls.
- 🔧 **Code Quality Improvement** – Suggests improvements on style, performance, and best practices.
- 📋 **Comprehensive Feedback Report** – Summarizes requirements met and gives improvement suggestions.

---

## 🛠️ Technology Stack

### Frontend
- HTML / CSS / JavaScript

### Backend
- Flask (Python)

### AI Integration
- **OpenAI GPT**
- **Google Gemini**
