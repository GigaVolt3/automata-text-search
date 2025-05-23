from flask import Flask, render_template, request, jsonify
from automata import AutomataSearch
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text', '')
        pattern = request.form.get('pattern', '')
        
        if not text or not pattern:
            return jsonify({'error': 'Both text and pattern are required'})
        
        # Perform automata search
        start_time = time.time()
        automata = AutomataSearch(pattern)
        matches = automata.search(text)
        search_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        
        # Highlight matches in the text
        highlighted_text = text
        for pos in sorted(matches, reverse=True):
            end_pos = pos + len(pattern)
            highlighted_text = (
                highlighted_text[:pos] + 
                f'<span class="match">{highlighted_text[pos:end_pos]}</span>' + 
                highlighted_text[end_pos:]
            )
        
        return jsonify({
            'matches': matches,
            'search_time': f"{search_time:.4f}",
            'highlighted_text': highlighted_text,
            'automata_count': len(automata_matches),
            'regex_count': len(regex_matches)
        })
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
