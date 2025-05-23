from flask import Blueprint, render_template, request
from projeto_flask import database
from projeto_flask.model.models import Aluno

aluno_bp = Blueprint('aluno', __name__)

@aluno_bp.route("/alunos", methods=["GET"])
def listar_alunos():
    busca = request.args.get("busca")
    if busca:
        alunos = Aluno.query.filter(Aluno.nome.like(f"%{busca}%")).all()
    else:
        alunos = Aluno.query.all()
    return render_template("alunos.html", lista_alunos=alunos, busca=busca)
