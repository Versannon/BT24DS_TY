# SPPU B.Tech Data Sciences - Year 3, Semester 5: Study Guide & Resources

Welcome to your study repository for Semester 5 of B.Tech Data Sciences (Savitribai Phule Pune University). This repository is structured to help you study, practice coding, and excel in your academic exams.

---

## 📅 Curriculum & Structure

Based on the official curriculum guidelines, we have extracted the relevant syllabus and prepared in-depth resources.

### 📚 Target Subjects
This repository includes complete study materials for:
1. **[Machine Learning](Machine_Learning/Syllabus.md) (BTDS-301-PCC & Lab BTDS-301-L)**
   - 6 Units of theory (intro, supervised, unsupervised, advanced, evaluation, FAT/robustness).
   - 21 Lab Exercises with runnable python code examples.
2. **[Descriptive Analytics](Descriptive_Analytics/Syllabus.md) (BTDS-302-PCC & Lab BTDS-302-L)**
   - 6 Units of theory (BI systems, data cleaning, stats & mining, visualization tools, project management, communication/ethics).
   - 23 Lab Exercises with runnable python code examples.
3. **[Computer Organization and Architecture](Computer_Organization_and_Architecture/Syllabus.md) (BTDS-304-PCC)**
   - 5 Units of theory (computer registers, microprogrammed control, computer arithmetic, I/O & memory organization, pipelining, multiprocessors).
   - Booth's multiplication algorithm simulation.
4. **[Digital Image Enhancement](Digital_Image_Enhancement/Syllabus.md) (BTDS-305-MDM(C))** (MDM Basket - 3)
   - 6 Units of theory (DIP basics, spatial domain point/filtering, frequency filtering, edge detection, color image, wavelets/CLAHE).
   - Runnable code scripts for each mathematical filter.

### 🚫 Excluded Electives
As requested, the following courses have been omitted:
- **Professional Elective-I** (BTDS-303-PEC)
- **Open Elective-III** (BTDS-306-OE)

---

## 📁 Directory Layout

```
1st_sem/
├── README.md                                     <-- This Master Study Guide
├── Machine_Learning/
│   ├── Syllabus.md                               <-- ML Course Syllabus
│   ├── Unit_1_Introduction/                      <-- Definition, Origin, Foundational Concepts, Pipeline
│   ├── Unit_2_Supervised_Learning/               <-- Regression, Logistic Regression, Decision Tree/SVM notes & codes
│   ├── Unit_3_Unsupervised_Learning/             <-- Clustering, PCA, Advanced Clustering notes & codes
│   ├── Unit_4_Advanced_Topics/                   <-- Ensemble, Deep Learning, RL notes & codes
│   ├── Unit_5_Evaluation_and_Selection/          <-- Metrics, CV, Tuning notes & codes
│   ├── Unit_6_Advanced_Concepts/                 <-- Transfer, Meta, Adversarial ML, FAT notes
│   └── Labs/
│       └── Lab_Exercises_Guide.md                <-- All 21 Labs Explained
│
├── Descriptive_Analytics/
│   ├── Syllabus.md                               <-- DA Course Syllabus
│   ├── Unit_1_Introduction_to_DA_and_BI/         <-- Overview, BI, DSS architecture notes
│   ├── Unit_2_Data_Collection_Preparation_EDA/   <-- Sources, cleaning, stats & correlation notes & codes
│   ├── Unit_3_Statistical_Summarization_and_Mining/ <-- Probability, Hypothesis testing, Association notes & codes
│   ├── Unit_4_Data_Visualization_and_BI_Tools/   <-- Principles, Dashboards notes & codes
│   ├── Unit_5_BI_Projects_Applications/          <-- Project management & Case studies notes
│   ├── Unit_6_Communication_Storytelling_Ethics/ <-- Presentation, GDPR/HIPAA compliance, Green BI notes
│   └── Labs/
│       └── Lab_Exercises_Guide.md                <-- All 23 Labs Details
│
├── Computer_Organization_and_Architecture/
│   ├── Syllabus.md                               <-- COA Course Syllabus
│   ├── Unit_1_Digital_Computers_and_RTL/         <-- Block diagram, RTL & Microoperations notes
│   ├── Unit_2_Microprogrammed_Control_and_CPU/   <-- MCU & Addressing modes notes
│   ├── Unit_3_Data_Representation_and_Arithmetic/ <-- Fixed/Floating point, Booth notes & codes
│   ├── Unit_4_IO_and_Memory/                     <-- DMA, Handshaking, Cache mapping notes
│   └── Unit_5_RISC_Pipeline_and_Multiprocessors/ <-- RISC/CISC, Hazards, Coherence notes
│
└── Digital_Image_Enhancement/
    ├── Syllabus.md                               <-- DIE Course Syllabus
    ├── Unit_1_Introduction/                      <-- Basics & PSNR/MSE metrics notes
    ├── Unit_2_Spatial_Domain/                    <-- Point processing & Filter notes & codes
    ├── Unit_3_Frequency_Domain/                  <-- Fourier & FFT filter notes & codes
    ├── Unit_4_Edge_Detection/                    <-- Sobel & Canny notes & codes
    ├── Unit_5_Color_Image/                       <-- Color models, balancing notes & codes
    └── Unit_6_Modern_Techniques/                 <-- Wavelets & CLAHE notes & codes
```

---

## 🚀 Strategy for Academic Excellence (Get 90%+)

To excel in both the theoretical (In-Sem & End-Sem) and practical exams, follow this study roadmap:

### 1. Master the Theory (For In-Sem & End-Sem Exams)
- **Use Active Recall**: Don't just re-read the notes. Ask yourself questions like:
  - *What is the difference between Star Schema and Snowflake Schema?* (Unit 1, Descriptive Analytics)
  - *Describe the five steps of Canny edge detection.* (Unit 4, Digital Image Enhancement)
  - *How does Booth's algorithm handle a multiplier of negative numbers?* (Unit 3, COA)
- **Practice Diagrams**: Draw CPU general register organization, DWH schemas, and DMA data transfer architectures by hand. Exams heavily reward neat block diagrams!
- **Understand Math & Equations**: Derive the 2s complement subtraction formula, the Pearson correlation coefficient, and the Bayes theorem.

### 2. Master the Practicals (For Lab Audits)
- **Run the Code**: Navigate to the respective unit folders and run each topic's Python script (e.g. `Topic_2_Linear_Regression.py`). Read the outputs carefully and understand each line of code.
- **Implement from Scratch**: Practice writing linear regression, k-means distance updates, or convolution kernels manually using NumPy to build solid foundational skills.
- **Learn standard libraries**: Master `sklearn`, `pandas`, `scipy.stats`, `matplotlib`, and `numpy` as they are standard requirements in B.Tech practical exams.

---

## 🛠️ Code Verification
We have included a verification script in the root directory:
```bash
python verify_code.py
```
Run this to automatically test all python scripts and make sure they operate without compilation errors.
