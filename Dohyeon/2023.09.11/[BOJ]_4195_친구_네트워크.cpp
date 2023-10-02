// [BOJ]_4195_친구_네트워크.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;


class UnionFind {

public:
    UnionFind() {}

    // 초기화 함수
    void init() {
        parent.clear();
        size.clear();
    }

    // 루트 노드를 찾는 함수
    string findRoot(string x) {
        if (!parent.count(x)) {
            parent[x] = x;
            size[x] = 1;
        }
        if (parent[x] == x) return x;
        return parent[x] = findRoot(parent[x]);
    }

    // 두 그룹을 합치는 함수
    void unionGroups(string x, string y) {
        string rootX = findRoot(x);
        string rootY = findRoot(y);

        if (rootX != rootY) {
            parent[rootX] = rootY;
            size[rootY] += size[rootX];
        }
    }

    // 그룹의 크기를 반환하는 함수
    int getSize(string x) {
        return size[findRoot(x)];
    }

private:
    unordered_map<string, string> parent;
    unordered_map<string, int> size;
};

int main() {

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;

    while (T--) {
        int F;
        cin >> F;

        UnionFind uf;
        uf.init();

        while (F--) {
            string friend1, friend2;
            cin >> friend1 >> friend2;

            uf.unionGroups(friend1, friend2);
            cout << uf.getSize(friend1) << endl;
        }
    }

    return 0;
}
// 프로그램 실행: <Ctrl+F5> 또는 [디버그] > [디버깅하지 않고 시작] 메뉴
// 프로그램 디버그: <F5> 키 또는 [디버그] > [디버깅 시작] 메뉴

// 시작을 위한 팁: 
//   1. [솔루션 탐색기] 창을 사용하여 파일을 추가/관리합니다.
//   2. [팀 탐색기] 창을 사용하여 소스 제어에 연결합니다.
//   3. [출력] 창을 사용하여 빌드 출력 및 기타 메시지를 확인합니다.
//   4. [오류 목록] 창을 사용하여 오류를 봅니다.
//   5. [프로젝트] > [새 항목 추가]로 이동하여 새 코드 파일을 만들거나, [프로젝트] > [기존 항목 추가]로 이동하여 기존 코드 파일을 프로젝트에 추가합니다.
//   6. 나중에 이 프로젝트를 다시 열려면 [파일] > [열기] > [프로젝트]로 이동하고 .sln 파일을 선택합니다.
