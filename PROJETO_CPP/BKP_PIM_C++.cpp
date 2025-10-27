#include <iostream>
#include <windows.h>
#include <string>
#include <iostream>

using namespace std;

bool criarDiretorio(const string& caminho) {
    return CreateDirectoryA(caminho.c_str(), NULL);
}

bool diretorioExiste(const string& caminho) {
    DWORD atributos = GetFileAttributesA(caminho.c_str());
    return (atributos != INVALID_FILE_ATTRIBUTES && 
           (atributos & FILE_ATTRIBUTE_DIRECTORY));
}

void copiarPasta(const string& origem, const string& destino) {
    string comando = "xcopy \"" + origem + "\" \"" + destino + "\" /E /I /Y /H";
    system(comando.c_str());
}

int main() {
    string origem = "C:\\Users\\josericardo\\Desktop\\PIM 2° SEMESTRE";
    string destino = "D:\\bkp_PIM";
    
    cout << "Verificando pasta de origem..." << endl;
    
    if (!diretorioExiste(origem)) {
        cout << "ERRO: Pasta de origem nao existe!" << endl;
        cout << "Caminho: " << origem << endl;
        cout << "Pressione Enter para sair...";
        cin.get();
        return 1;
    }
    
    cout << "Pasta de origem encontrada!" << endl;
    cout << "Criando pasta de destino..." << endl;
    
    if (!diretorioExiste(destino)) {
        if (!criarDiretorio(destino)) {
            cout << "ERRO: Nao foi possivel criar pasta de destino!" << endl;
            cout << "Pressione Enter para sair...";
            cin.get();
            return 1;
        }
        cout << "Pasta de destino criada: " << destino << endl;
    } else {
        cout << "Pasta de destino ja existe!" << endl;
    }
    
    cout << "\nINICIANDO BACKUP..." << endl;
    cout << "De: " << origem << endl;
    cout << "Para: " << destino << endl;
    cout << "Aguarde...\n" << endl;
    
    copiarPasta(origem, destino);
    
    cout << "\nBACKUP CONCLUIDO COM SUCESSO!" << endl;
    cout << "Pressione Enter para sair...";
    cin.get();
    
    return 0;
}