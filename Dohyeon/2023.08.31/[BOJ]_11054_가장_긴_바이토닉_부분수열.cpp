//// [BOJ]_11054_가장_긴_바이토닉_부분수열.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
////
//#include <iostream>
//#include <algorithm>
//
//using namespace std;
//
//int main() {
//	
//	int arr[1001];
//	int dpup[1001];
//	int dpdown[1001];
//	int n;
//	int ans = 0;
//
//
//	cin >> n;
//
//	for (int i = 0; i < n; i++) {
//		int tmp;
//		cin >> tmp;
//		arr[i] = tmp;
//	}
//
//	dpup[0] = 1;
//	dpdown[n - 1] = 1;
//
//	int maxup = 0;
//	int maxdown = 0;
//
//	for (int j = 0; j < n - 1; j++) {
//		if (maxup < arr[j + 1]) {
//			dpup[j + 1] = dpup[j] + 1;
//			maxup = arr[j + 1];
//		}
//		else {
//			dpup[j + 1] = dpup[j];
//		}
//
//		if (maxdown < arr[n - j - 1 - 1]) {
//			dpdown[n - j - 1 - 1] = dpdown[n - j - 1] + 1;
//			maxdown = arr[n - j - 1 - 1];
//		}
//		else {
//			dpdown[n - j - 1 - 1] = dpdown[n - j - 1];
//		}
//	}
//	int max_val = 0;
//	for (int k = 0; k < n; k++) {
//		if (dpdown[k] + dpup[k] > max_val) {
//			max_val = dpdown[k] + dpup[k];
//		}
//	}
//	for (int q = 0; q < n; q++) {
//		cout << dpup[q] << " ";
//	}
//	cout << "\n";
//
//	for (int q = 0; q < n; q++) {
//		cout << dpdown[q] << " ";
//	}
//
//
//	cout << max_val - 1 << endl;
//
//	return 0;
//}
//
// 
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> arr(n);
    vector<int> dpup(n, 1);
    vector<int> dpdown(n, 1); 

    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }


    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (arr[j] < arr[i]) {
                dpup[i] = max(dpup[i], dpup[j] + 1);
            }
        }
    }

    for (int i = n - 1; i >= 0; --i) {
        for (int j = n - 1; j > i; --j) {
            if (arr[j] < arr[i]) {
                dpdown[i] = max(dpdown[i], dpdown[j] + 1);
            }
        }
    }

    int max_length = 0;
    for (int i = 0; i < n; ++i) {
        max_length = max(max_length, dpup[i] + dpdown[i] - 1); // 겹치는 i번째 원소를 빼줌
    }

    cout << max_length << endl;

    return 0;
}
// 
// 
//// 프로그램 실행: <Ctrl+F5> 또는 [디버그] > [디버깅하지 않고 시작] 메뉴
//// 프로그램 디버그: <F5> 키 또는 [디버그] > [디버깅 시작] 메뉴
//
//// 시작을 위한 팁: 
////   1. [솔루션 탐색기] 창을 사용하여 파일을 추가/관리합니다.
////   2. [팀 탐색기] 창을 사용하여 소스 제어에 연결합니다.
////   3. [출력] 창을 사용하여 빌드 출력 및 기타 메시지를 확인합니다.
////   4. [오류 목록] 창을 사용하여 오류를 봅니다.
////   5. [프로젝트] > [새 항목 추가]로 이동하여 새 코드 파일을 만들거나, [프로젝트] > [기존 항목 추가]로 이동하여 기존 코드 파일을 프로젝트에 추가합니다.
////   6. 나중에 이 프로젝트를 다시 열려면 [파일] > [열기] > [프로젝트]로 이동하고 .sln 파일을 선택합니다.
