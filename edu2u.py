from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
#CORS(app)
CORS(app, resources={r"/*": {"origins": "https://subtle-kashata-737166.netlify.app"}})


# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')


@app.route('/generate-content', methods=['POST'])
def generate_content():
    try:
        data = request.json
        prompt = data.get('prompt')

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are an educational content generator."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=3000,
            temperature=0.7,
        )

        content = response.choices[0]['message']['content'].strip()
        return jsonify({"success": True, "content": content})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
