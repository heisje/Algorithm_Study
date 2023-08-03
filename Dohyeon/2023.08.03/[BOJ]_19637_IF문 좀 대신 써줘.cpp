// [BOJ]_19637_IF문 좀 대신 써줘.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M;
	cin >> N >> M;
	vector<pair<int, string>> chingho(N);
	for (int i = 0; i < N; i++) {
		int tmp1;
		string tmp2;	
		cin >> tmp2 >> tmp1;
		chingho[i] = make_pair(tmp1, tmp2);
	}
	for (int j = 0; j < M; j++) {
		int tmp;
		cin >> tmp;
		for (int k = 0; k < N; k++) {
			if (tmp <= chingho[k].first) {
				cout << chingho[k].second << "\n";
				break;
			}
		}
	}

	return 0;
}

/*
정답코드
#include <bits/stdc++.h>
#define INF 987654321
using namespace std;

int n, m;
int power[100000];
string title[100000];

int binsearch(int p){
	int mid = 0, left = 0, right = n-1;
	while(left <= right){
		mid = (left+right)/2;
		if(p <= power[mid])
			right = mid-1;
		else
			left = mid+1;
	}
	if(p > power[mid])
		return mid+1;
	else
		return mid;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n >> m;
	for(int i = 0; i < n; i++)
		cin >> title[i] >> power[i];
	int p;
	for(int i = 0; i < m; i++){
		cin >> p;
		cout << title[binsearch(p)] << "\n";
	}
	return 0;
}

*/




// 프로그램 실행: <Ctrl+F5> 또는 [디버그] > [디버깅하지 않고 시작] 메뉴
// 프로그램 디버그: <F5> 키 또는 [디버그] > [디버깅 시작] 메뉴

// 시작을 위한 팁: 
//   1. [솔루션 탐색기] 창을 사용하여 파일을 추가/관리합니다.
//   2. [팀 탐색기] 창을 사용하여 소스 제어에 연결합니다.
//   3. [출력] 창을 사용하여 빌드 출력 및 기타 메시지를 확인합니다.
//   4. [오류 목록] 창을 사용하여 오류를 봅니다.
//   5. [프로젝트] > [새 항목 추가]로 이동하여 새 코드 파일을 만들거나, [프로젝트] > [기존 항목 추가]로 이동하여 기존 코드 파일을 프로젝트에 추가합니다.
//   6. 나중에 이 프로젝트를 다시 열려면 [파일] > [열기] > [프로젝트]로 이동하고 .sln 파일을 선택합니다.
