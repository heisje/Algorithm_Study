// [BOJ]_4485_녹색 옷 입은 애가 젤다지.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

int y_ar[4] = { 0,0,-1,1 };
int x_ar[4] = { 1,-1,0,0 };
int n;
int arr[130][130];
int dist[130][130];

void bfs() {

	queue <pair<int, int>> pq;

	pq.push(make_pair(0, 0));
	dist[0][0] = arr[0][0];

	while (!pq.empty()) {

		int y = pq.front().first;
		int x = pq.front().second;
		pq.pop();

		for (int i = 0; i < 4; i++) {
			int ny = y + y_ar[i];
			int nx = x + x_ar[i];


			if (ny >= 0 && ny < n && nx >= 0 && nx < n) {
				if (dist[ny][nx] > dist[y][x] + arr[ny][nx]) {
					dist[ny][nx] = dist[y][x] + arr[ny][nx];
					pq.push(make_pair(ny, nx));
				}
			}
		}
	}

}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);

	int cnt = 1;
	int INF = 9999999999;

	while (1) {
		cin >> n;
		if (n == 0)
			break;

		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++) {
				cin >> arr[i][j];
				dist[i][j] = INF;
			}

		bfs();
		cout << "Problem " << cnt++ << ": " << dist[n - 1][n - 1] << endl;
	}

	return 0;
}