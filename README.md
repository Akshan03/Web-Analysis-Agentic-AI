# Agentic RAG-Based Web App  

This is a web-based application that uses an Agentic Retrieval-Augmented Generation (RAG) pipeline to answer user questions based on a provided URL. The project allows users to input a webpage URL and a question. The application processes the webpage content and generates a context-relevant answer using advanced Natural Language Processing (NLP) techniques.

This project is inspired by concepts taught in the video [Agentic RAG Explained](https://youtu.be/LzG_Vkd30Kg?si=Nzav1MMhRJtvksNf) and has been further modified to include a custom RAG model for question answering.

---

## Features  
- Users can input a webpage URL and a query.  
- The backend extracts content from the webpage and processes the question using a RAG model.  
- Provides a context-aware response or conducts an online search if the context is insufficient.  
- Built with Flask for the backend and a responsive HTML/CSS frontend.

---

## Libraries and Models Used  

### **Python Libraries**  
1. **Flask** - For building the backend of the web application.  
2. **BeautifulSoup (bs4)** - For extracting and parsing webpage content.  
3. **Transformers** - For loading pre-trained models and tokenizers.  
4. **SentenceTransformers** - For creating text embeddings.  
5. **DuckDuckGoSearch (duckduckgo_search)** - For performing online searches when the context is not relevant.  
6. **Markdown** - For rendering the output in Markdown format.  
7. **Jinja2** - For rendering the HTML templates in Flask.

### **Models**  
1. **BAAI/bge-large-en-v1.5** - A pre-trained embedding model from SentenceTransformers for generating text embeddings.  
2. **Hugging Face Transformers** - Used for generation and processing tasks within the application.  

---

## How to Run the Flask App  

Follow these steps to set up and run the Flask application on your local machine:

### **1. Clone the Repository**  
```bash
git clone <repository-url>
cd <repository-name>
```

### **2. Set Up a Virtual Environment**  
It is recommended to use a virtual environment to manage dependencies.  
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### **3. Install Required Libraries**  
Install all necessary libraries from the `requirements.txt` file.  
```bash
pip install -r requirements.txt
```

### **4. Run the Flask App**  
Start the Flask development server.  
```bash
python app.py
```

### **5. Access the Web App**  
Open your web browser and go to:  
```
http://127.0.0.1:5000
```

---

## Folder Structure  

```
agentic_rag/
├── app.py                 # Flask backend script  
├── templates/             # HTML templates folder  
│   ├── index.html         # Main user interface  
├── static/                # Static files like CSS and images  
│   ├── styles.css         # CSS for styling the app  
├── agentic_rag.ipynb      # Python notebook with the RAG pipeline  
├── requirements.txt       # List of dependencies  
└── README.md              # Project documentation (this file)  
```

---

## Future Improvements  
- Add support for more advanced transformer models like GPT-4 or LLaMA for better answers.  
- Enhance the UI with more interactive elements like charts or tooltips.  
- Deploy the app to a cloud service like AWS, Heroku, or Google Cloud for broader access.
- Reading and analysing PDFs using this Agentic RAG.

---

## License  
This project is open-source and available under the MIT License.  

---

Feel free to contribute or suggest improvements!
```  
