                                            INFORMATION RETRIEVAL 
                                               Project Report:

**Abstract:**

The project's goal is to create a complete online content retrieval and search engine utilising Flask, Scikit-Learn, and Scrapy modules in combination with Python 3.10+. The main goals were to develop a query processor to handle free-text queries, an indexer to construct an inverted index, and a web crawler to obtain HTML content. This report provides an overview of the development process, lists the goals that were met, and makes recommendations for possible future improvements.


**Overview:**

The approach is a multi-step procedure that involves document indexing, web crawling, and query processing. A pertinent literature analysis highlights the significance of effective information retrieval systems across several domains, such as digital libraries, data mining applications, and web search engines. The suggested system uses cutting edge methods for web crawling, indexing, and query processing in an effort to speed up the retrieval process.

**Design:**

Easy incorporation of new features or improvements is made possible by the system's modular and scalable design. With respect to maximum pages and depth, the web crawler, which was constructed with Scrapy, is in charge of retrieving HTML content from seed URLs/domains. The indexer, implemented using Scikit-Learn, constructs an inverted index in pickle format, enabling efficient retrieval of documents based on TF-IDF scores and cosine similarity. The Flask-developed query processor ranks results according to relevancy and verifies and handles free-text searches.

**Architecture:**

The web document retrieval system's architecture is made to effectively manage duties like web crawling, indexing, and query processing, guaranteeing smooth operation and seamless integration. The three primary parts of the architecture are the processor, which is based on Flask, the indexer, which is based on Scikit-Learn, and the crawler, which is based on Scrapy.

Scrapy-based Crawler:

The crawler component is in charge of browsing websites, obtaining material, and downloading HTML-formatted online documents. In order to regulate the crawling process, it is initialised using parameters like maximum pages and maximum depth, in addition to seed URLs or domains. Additional features that improve efficiency and scalability include distributed crawling using scrapyd and concurrent crawling with AutoThrottle. The crawler follows web crawling best practices, which guarantees courteous behaviour and effective resource use.

Flask-based Processor:

The processing part responds to user inquiries, verifies data, and provides search results that are rated highly. It makes available a RESTful API that can integrate with other apps and takes JSON-formatted requests. Error-checking and query validation are carried out to guarantee robustness and stop fraudulent input. By offering more precise and pertinent search results, optional tools like query expansion using WordNet and spelling correction/suggestions using NLTK improve the user experience.

Scikit-Learn-based Indexer:

Using the online content that have been crawled, the indexer component creates an inverted index to facilitate effective search and retrieval. It uses methods like cosine similarity and TF-IDF score/weight representation to index and rank pages according to how relevant they are to user queries. Neural/semantic search kNN similarity using FAISS and vector embedding representation using word2vec are examples of optional features. Fast indexing and retrieval times are ensured by the indexer's effective handling of massive amounts of data.

**Operation:**

Install Python and Install Linux in windows
wsl –install
Install required libraries
Pip install scrapy
Pip install sckit-learn
pip install beautifulsoup4
pip install flask
pip install requests
Instructions for completing the project:
Step 1:Navigate to the spiders folder in the terminal and type "Scrapy crawl " to launch the project.
The html pages' cosine similarity and TF-IDF scores will be computed and saved in an index.pkl file.
Step2: Go to the access pickle folder in the terminal, run the Python file, and the contents of the file will appear in the terminal to view the index.pkl file.
step3: Navigate to the Flask folder in the terminal and run the Python file there to launch the Flask server.
step 4:The flask server has now been started. Launch a new terminal window and send the flask server a request using the syntax shown below:
curl -X POST http://localhost:5000/query -H "Content-Type: application/json" -d '{"query": "python introduction"}'

You may now see the server's answer in JSON format, which includes the document name and cosine similarity of the top k results.

**Conclusion:**

The project's goal of creating a web search and content retrieval system has been accomplished. The components that have been deployed exhibit effective crawling, indexing, and query processing capability. Scalability and performance optimisation, particularly when managing large-scale datasets, might use some work, nevertheless. To further improve system capabilities, next stages may involve adding sophisticated features like distributed crawling, semantic search, and real-time indexing.

**Test cases:**

![image](https://github.com/TSP24SCM33T/ir-project/assets/164950312/67482298-dbb6-4029-89bf-0e23ffb5edcb)
![image](https://github.com/TSP24SCM33T/ir-project/assets/164950312/22f09a87-de1e-4267-9231-37f4fd4a6dfa)
![image](https://github.com/TSP24SCM33T/ir-project/assets/164950312/c77135fc-d44e-4c30-85a7-6c5f01aeacde)


**Data Sources:**

Scrapy (version: 2.9.0) for web crawling 

Flask (version: 3.0.3) for building the query processor module

Beautiful Soup (version 4) for parsing HTML content.

Scikit-learn (version 1.4.2) for TF-IDF indexing and advanced search functionalities.

Flask (version 3.0.3) for building the query processor module


**Bibliography:**

https://scrapy.org/

https://requests.readthedocs.io/en/latest/

https://scikit-learn.org/stable/

https://flask.palletsprojects.com/en/3.0.x/


