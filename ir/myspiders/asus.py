import os
import pickle
from flask import Flask, jsonify, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the pre-built document search index
index_file_path = os.path.join(os.path.dirname(__file__), '..' ,'spiders', 'index.pkl')
with open(index_file_path, 'rb') as f:
  search_index = pickle.load(f)

# Create a tool for converting text to numerical features
text_to_feature_converter = TfidfVectorizer()

# Preprocess document text from the index and create a feature matrix
document_features = text_to_feature_converter.fit_transform([doc['document'] for doc in search_index.values()])

# Create a Flask web application instance
web_app = Flask(__name__)

# Define a route to handle user search queries (sends data after submit)
@web_app.route('/query', methods=['POST'])
def handle_search_query():
  # Get the user's search query from the request data
  user_query_json = request.json
  user_query = user_query_json.get('query', '')

  # Convert the user query into numerical features
  user_query_features = text_to_feature_converter.transform([user_query])

  # Calculate similarity scores between the query and all documents
  similarity_scores = cosine_similarity(user_query_features, document_features).flatten()

  # Find the top K most relevant documents (maximum 10 or all if less)
  number_of_results = min(5, len(similarity_scores))
  top_documents = similarity_scores.argsort()[-number_of_results:][::-1]

  # Prepare search results with details
  search_results = []
  for document_index in top_documents:
    document = search_index[document_index]
    search_results.append({
      'similarity_score': similarity_scores[document_index],
      'document_name': document['document_name'],
    })

  # Return the search results as JSON data
  return jsonify(search_results)

# Run the web application (set to debug mode for automatic code updates)
if __name__ == '__main__':
  web_app.run(debug=True)