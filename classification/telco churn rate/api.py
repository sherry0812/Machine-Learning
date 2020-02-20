from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)
features_ = []

@app.route('/predict', methods=['Post'])
def predict():
	data=request.get_json()
	items=[data]
	features_.append(items)
	prediction = model.predict(pd.DataFrame(items))

	return jsonify({"prediction": float(prediction[0])})

@app.route('/features')
def features():
	return jsonify({"features": features_})

if __name__ == '__main__':
	model = pickle.load(open('model.pkl','rb'))
	app.run(debug=True)





# Remove empty strings
df_labeled['post_message'] = df_labeled['post_message'].apply(lambda list_words: list(filter(None, list_words)))