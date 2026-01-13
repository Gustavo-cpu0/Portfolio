from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS produtos 
                      (id INTEGER PRIMARY KEY, nome TEXT, qtd INTEGER)''')
    # Inserir dados iniciais se estiver vazio
    cursor.execute("SELECT count(*) FROM produtos")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO produtos (nome, qtd) VALUES ('Laptop', 10), ('Mouse', 50)")
    conn.commit()
    conn.close()

@app.route('/produtos', methods=['GET'])
def get_produtos():
    conn = sqlite3.connect('estoque.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = [{'id': row[0], 'nome': row[1], 'qtd': row[2]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(produtos)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)