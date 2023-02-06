import pandas as pd

def backCode():
    gabarito = pd.read_excel('Gabarito.xlsx')
    respostas = pd.read_excel('Respostas.xlsx')

    gb = list(gabarito.Gabarito)
    nome = 'X'
    #ind = 0
    #l_nome = list()
    rp = dict()
    rp_aluno = list(respostas.resp_aluno.fillna('x'))
    for i in range(len(list(respostas.aluno_nome))):
        if list(respostas.aluno_nome)[i] != nome:
            nome = list(respostas.aluno_nome)[i]
            rp[nome] = list()
            #rp.append(list(respostas.aluno_nome)[i])
            #rp[ind] = list()
            for j in range(len(gb)):
                rp[nome].append(rp_aluno[0])
                del rp_aluno[0]
                #l_nome.append(list(respostas.aluno_nome)[i])
                #ind += 1
    rp_aluno = list(respostas.resp_aluno.fillna('x'))

def menu():
    cmd = int(input("[1] Média de acertos geral\n"
                    "[2] Média de acertos de cada cada aluno\n"
                    "[3] Total de acertos de cada aluno\n"
                    "[0] Sair\n"
                    ">> "))
    if cmd == 1:
        acertosGeral()
    elif cmd == 2:
        acertosInd()
    elif cmd == 3:
        totalAcertos()
    elif cmd == 0:
        exit()
    else:
        print("Comando inválido.\n"
              "Tente novamente.")
    menu()
    

def acertosGeral():
    rp_aluno = backCode.rp_aluno
    gb = backCode.gb
    pt = 0
    j = 0
    while j < len(rp_aluno):
        i = 0
        for i in range(len(gb)):
            if gb[i].lower() == rp_aluno[j]:
                pt += 1
            j += 1
    #print(f"Acertos (abs): {pt/len(rp_aluno):.2}")
    return(f"Acertos (%): {pt/len(rp_aluno):.0%}")

def acertosInd():
    rp = backCode.rp
    gb = backCode.gb
    for key in rp:
        pt = 0
        for i in range(len(gb)):
            if gb[i].lower() == rp[key][i]:
                pt += 1
        return(f"{key}:\n"
            #f"Acertos (abs): {pt/len(gb):.2}\n"
            f"Acertos (%): {pt/len(gb):.0%}\n"
            "--=--=--=--=--=--=--=--")

def totalAcertos():
    rp = backCode.rp
    gb = backCode.gb
    pt = 0
    for key in rp:
        pt = 0
        for i in range(len(gb)):
            if gb[i].lower() == rp[key][i]:
                pt += 1
        return(f"{key}: {pt} acerto(s).\n")

menu()