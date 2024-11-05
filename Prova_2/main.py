import argparse
from teacher_crud import Database, TeacherCRUD

class TeacherCLI:
    def __init__(self, db):
        self.teacher_crud = TeacherCRUD(db)

    def create_teacher(self, name, ano_nasc, cpf):
        self.teacher_crud.create(name, ano_nasc, cpf)
        print(f"Teacher {name} criado com sucesso.")

    def read_teacher(self, name):
        result = self.teacher_crud.read(name)
        if result:
            for record in result:
                print(f"Teacher encontrado: {record['t']['name']}, {record['t']['ano_nasc']}, {record['t']['cpf']}")
        else:
            print("Teacher não encontrado.")

    def update_teacher(self, name, new_cpf):
        self.teacher_crud.update(name, new_cpf)
        print(f"Teacher {name} atualizado com sucesso.")

    def delete_teacher(self, name):
        self.teacher_crud.delete(name)
        print(f"Teacher {name} deletado com sucesso.")

def main():
    db = Database("")
    cli = TeacherCLI(db)

    parser = argparse.ArgumentParser(description='Operações CRUD de Teacher CLI')
    parser.add_argument('operation', choices=['create', 'read', 'update', 'delete'], help='Operação CRUD')
    parser.add_argument('name', help='Nome do Teacher')
    parser.add_argument('--ano_nasc', type=int, help='Ano de nascimento do Teacher')
    parser.add_argument('--cpf', help='CPF do Teacher')
    parser.add_argument('--new_cpf', help='Novo CPF do Teacher')

    args = parser.parse_args()

    if args.operation == 'create':
        cli.create_teacher(args.name, args.ano_nasc, args.cpf)
    elif args.operation == 'read':
        cli.read_teacher(args.name)
    elif args.operation == 'update':
        cli.update_teacher(args.name, args.new_cpf)
    elif args.operation == 'delete':
        cli.delete_teacher(args.name)

    db.close()

if __name__ == "__main__":
    main()