### **Problem Statement**  
Extracting precise and accurate information from the vast amount of web content can be challenging. Users often need answers to specific questions, but the relevant context might either be hidden within lengthy web pages or not present at all. This process becomes even more cumbersome when users have to perform manual searches for additional information.  

There is a need for an automated system that can seamlessly combine searching, retrieving, and generating context-aware answers to user queries.  

---

### **Proposed Solution**  
The **Agentic RAG System** addresses this problem by leveraging advanced retrieval-augmented generation (RAG) techniques. It works as follows:  
1. **Contextual Search**: The system scans the content of the provided URLs to identify relevant context for answering the user query.  
2. **Dynamic Web Search**: If the required context is not available in the provided URLs, the system performs a web search using the DuckDuckGo module to find relevant information online.  
3. **Accurate Response Generation**: Using the retrieved context, the system generates concise, contextually accurate answers tailored to the user query.  

This dual-layered approach ensures efficient and accurate information retrieval, saving users time and effort while delivering high-quality results.

---

### **Example Input**  
**URLs**:  
- https://em360tech.com/tech-article/what-is-llama-3

**Question**:  
What is Llama 3?

**Output**:
Device set to use cpu
Question: what is llama 3
Context can answer the question
Answer: <class 'str'>
In this article, we will explore Meta Llama 3, how to use it and the differences between Llama 2 and Llama 3. What is Meta Llama 3? ---------------------

Meta Llama 3 is a large language model (LLM) developed by Meta that's trained on a massive amount of text data. This allows it to understand and respond to language in a comprehensive way, making it suitable for tasks like writing different kinds of creative content, translating languages, and answering your questions in an informative way. Compared to previous versions like Llama 2, Llama 3 boasts better reasoning abilities, code generation, and can follow instructions more effectively. It also outperforms other open models on benchmarks that measure language understanding and response (ARC, DROP and MMLU). One of the most intriguing new feature of Llama 3 compared to Llama 2 is its integration into Meta's core products. The AI assistant is now accessible through chat functions in Facebook Messenger, Instagram, and WhatsApp. This translates to a more helpful and more accessible AI assistant. Imagine asking Facebook for a summary of a research paper, or requesting creative writing prompts on Instagram – Llama 3 aims to be there for these tasks and more.
