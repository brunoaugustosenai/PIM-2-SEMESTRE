#include <iostream>
#include <windows.h>
#include <string>
#include <iostream>

using namespace std;

bool criarDiretorio(const wstring& caminho) {
    return CreateDirectoryW(caminho.c_str(), NULL);
}

bool diretorioExiste(const wstring& caminho) {
    DWORD atributos = GetFileAttributesW(caminho.c_str());
    return (atributos != INVALID_FILE_ATTRIBUTES && 
           (atributos & FILE_ATTRIBUTE_DIRECTORY));
}

void copiarPasta(const wstring& origem, const wstring& destino) {
    wstring comando = L"xcopy \"" + origem + L"\" \"" + destino + L"\" /E /I /Y /H";
    _wsystem(comando.c_str());
}

int main() {
    // Usar wstring para suporte a Unicode
    wstring origem = L"C:\\Users\\josericardo\\Desktop\\PIM 2° SEMESTRE";
    wstring destino = L"D:\\BKP_PIM";
    
    wcout << L"Verificando pasta de origem..." << endl;
    
    if (!diretorioExiste(origem)) {
        wcout << L"ERRO: Pasta de origem nao existe!" << endl;
        wcout << L"Caminho: " << origem << endl;
        wcout << L"Pressione Enter para sair...";
        cin.get();
        return 1;
    }
    
    wcout << L"Pasta de origem encontrada!" << endl;
    wcout << L"Criando pasta de destino..." << endl;
    
    if (!diretorioExiste(destino)) {
        if (!criarDiretorio(destino)) {
            wcout << L"ERRO: Nao foi possivel criar pasta de destino!" << endl;
            wcout << L"Pressione Enter para sair...";
            cin.get();
            return 1;
        }
        wcout << L"Pasta de destino criada: " << destino << endl;
    } else {
        wcout << L"Pasta de destino ja existe!" << endl;
    }
    
    wcout << L"\nINICIANDO BACKUP..." << endl;
    wcout << L"De: " << origem << endl;
    wcout << L"Para: " << destino << endl;
    wcout << L"Aguarde...\n" << endl;
    
    copiarPasta(origem, destino);
    
    wcout << L"\nBACKUP CONCLUIDO COM SUCESSO!" << endl;
    wcout << L"Pressione Enter para sair...";
    cin.get();
    
    return 0;
} 