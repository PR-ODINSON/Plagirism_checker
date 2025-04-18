
# 🧠 Plagiarism Checker using SBERT + Deep Learning

A robust, deep learning-based plagiarism detection tool that analyzes **semantic similarity** between two texts. Unlike traditional keyword-matching tools, this system leverages **Sentence-BERT (SBERT)** for deep sentence embeddings and a **custom-trained neural network model** to determine if the suspect text is plagiarized from the source.

> 📌 Built with Flask • TensorFlow • SBERT • NumPy  
> 🎓 Developed by [Prithviraj Verma](https://github.com/PR-ODINSON), B.Tech CSE @ IITRAM  

---

## 🎥 Video Demo

> 📽️ [Click here to watch the demo](https://www.youtube.com/watch?v=YOUR_VIDEO_LINK)

<!-- Replace the link above with your actual video link -->

---

## 🖼️ Screenshot

![Web Interface](static/demo_screenshot.png)

> A simple and clean UI to check plagiarism with one click.

---

## 🛠️ Features

- ✅ Semantic-based plagiarism detection using SBERT
- ✅ Lightweight Flask-based web interface
- ✅ Displays both **result (Plagiarized / Not Plagiarized)** and **confidence score**
- ✅ Trained deep learning model (.h5 format)
- ✅ Easy to customize or extend with more advanced NLP models

---

## 🧩 How It Works

1. User inputs **source text** and **suspect text** via the web UI.
2. Both texts are converted into **512-dimensional SBERT embeddings**.
3. A trained neural network receives these embeddings (concatenated) and returns a **probability score**.
4. If probability > 0.5 → **Plagiarized**, else → **Not Plagiarized**.

---

## 📁 Directory Structure

```
Plagirism_checker/
├── app.py                        # Flask application
├── plagiarism_detector_model.h5  # Trained deep learning model
├── requirements.txt              # Required Python packages
├── templates/
│   └── index.html                # Frontend HTML (Bootstrap)
├── static/
│   └── demo_screenshot.png       # Optional image for documentation
└── README.md                     # Project documentation
```

---

## 🧪 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/PR-ODINSON/Plagirism_checker.git
cd Plagirism_checker
```

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, manually install:
```bash
pip install flask tensorflow sentence-transformers numpy
```

### 4. Run the Web App

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser to use the app.

---

## ⚙️ Model Details

- **Embedding Model**: `sentence-transformers` (SBERT)
- **Custom Neural Network**: Built with TensorFlow/Keras  
- **Input**: Concatenated embeddings of both texts  
- **Output**: Probability of plagiarism (0.0 to 1.0)  
- **Decision Threshold**: `0.5` (can be adjusted for stricter/looser detection)

---

## 🧠 Training Overview

> Want to replicate or improve the model?

- **Dataset**: Custom dataset containing pairs of source and modified texts (plagiarized vs. original)
- **Embedding**: Used SBERT to extract dense semantic vectors
- **Architecture**: Fully connected neural network trained on pairs of SBERT embeddings
- **Loss Function**: Binary Crossentropy
- **Optimizer**: Adam
- **Performance**: Achieved ~95% accuracy on the validation set

---

## 🧩 Future Improvements

- 🔍 Add explanation using LIME/SHAP for interpretability
- 📊 Display similarity heatmap or visual difference
- 🧠 Train on a larger academic dataset (e.g., PAN plagiarism corpus)
- 🌐 Add language support for non-English texts

---

## 🙋‍♂️ Author

**Prithviraj Verma**  
👨‍🎓 B.Tech in Computer Science, IITRAM  
💼 AI/ML Intern | Data Scientist  
🔗 [LinkedIn](https://linkedin.com/in/pr-verma)  
🐙 [GitHub](https://github.com/PR-ODINSON)

---

## 📄 License

This project is open-source under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to fork the repository and submit a pull request.

---

## ⭐ If you found this useful...

Leave a ⭐ on [GitHub](https://github.com/PR-ODINSON/Plagirism_checker) — it helps a lot!
