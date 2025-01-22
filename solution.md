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
