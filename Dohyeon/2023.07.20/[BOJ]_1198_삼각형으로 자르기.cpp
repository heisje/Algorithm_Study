// [BOJ]_1198_삼각형으로 자르기.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <cmath>

using namespace std;

double calculateTriangleArea(int x1, int y1, int x2, int y2, int x3, int y3) {
    // 세 변의 길이 계산
    double a = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
    double b = sqrt(pow(x3 - x2, 2) + pow(y3 - y2, 2));
    double c = sqrt(pow(x1 - x3, 2) + pow(y1 - y3, 2));

    // 반 둘레 계산
    double s = (a + b + c) / 2.0;

    // 넓이 계산
    double area = sqrt(s * (s - a) * (s - b) * (s - c));

    return area;
}

int main()
{
    double max_triangle = 0;

    int N;
    pair<int, int> p_arr[35];           // 페어 어레이 만들어두기
    cin >> N;
    for (int i = 0; i < N; i++) {
        int tmp1, tmp2;
        cin >> tmp1 >> tmp2;
        p_arr[i].first = tmp1;
        p_arr[i].second = tmp2;
    }

    for (int i = 0; i < N - 2; i++) {
        for (int j = i + 1; j < N - 1; j++) {
            for (int k = j + 1; k < N; k++) {
                double tmp_area = calculateTriangleArea(p_arr[i].first, p_arr[i].second, p_arr[j].first, p_arr[j].second, p_arr[k].first, p_arr[k].second);
                if (tmp_area > max_triangle) {
                    max_triangle = tmp_area;
                }
            }
        }
    }
    cout.precision(11); // 이게뭐지?
    cout << max_triangle;
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
