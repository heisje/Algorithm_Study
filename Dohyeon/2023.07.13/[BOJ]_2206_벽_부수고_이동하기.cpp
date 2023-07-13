// [BOJ]_2206_벽_부수고_이동하기.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//
#include <iostream>
#include <queue>
#include <tuple>
#define MAX 1001

using namespace std;

int N, M;                       // 미로 크기
int maze[MAX][MAX];             // 미로 표현용 2차원 배열
int visited[MAX][MAX][2] = {0};  // 0으로 초기화, 3번째값이 0이면 벽부숨 x 1이면 벽부숨o
int dist[MAX][MAX];             // 이동칸 기록용 2차원 배열 

int x_dir[4] = { -1, 1, 0, 0 };   // 상화좌우 x축 방향
int y_dir[4] = { 0, 0, -1, 1 };   // 상화좌우 y축 방향

queue<tuple<int, int, int> > q;        // 탐색 좌표 저장용 queue

// 미로 경로 탐색
void bfs(int start_x, int start_y) {

    visited[start_x][start_y][0] = 0;          // 입력 받은 시작 좌표를 방문, 3번째의 첫번째는 방문수
    visited[start_x][start_y][0] = 0;         // 두번째는 벽 부순것을 확인

    visited[start_x][start_y][1] = 0;          // 입력 받은 시작 좌표를 방문, 3번째의 첫번째는 방문수
    visited[start_x][start_y][1] = 0;

    q.push(make_tuple(start_x, start_y, 0));     // queue 에 삽입  0이면 파괴이력 없음 1이면 있음으로 구별할 예정
    
    //std::cout << "왔니" << endl;
    // 모든 좌표를 탐색할 때까지 반복
    while (!q.empty()) {

        // queue 의 front 좌표를, 현재 좌표로 지정
        int x = get<0>(q.front());
        int y = get<1>(q.front());
        int destroyed = get<2>(q.front());


        if (x == N - 1 && y == M - 1) {

            if (destroyed == 1) {
                std::cout << visited[x][y][1] + 1 << endl;
            }
            else {
                std::cout << visited[x][y][0] + 1 << endl;
            }

            return;
        }
        
        // qeueu 의 front 좌표 제거
        q.pop();


        //cout << x << " " << y << endl;
        //cout << visited[x][y] << endl;
        // 현재 좌표와 상하좌우로 인접한 좌표 확인
        for (int i = 0; i < 4; ++i) {
            //std::cout << "몇번" << endl;

            // 현재 좌표와 상하좌우로 인접한 좌표
            int x_new = x + x_dir[i];
            int y_new = y + y_dir[i];
            //cout << "다음 위치" << endl;
            //cout << x_new << y_new << endl;
            // 인접한 좌표가, 미로 내에 존재하는지, 방문한 적이 없는지, 이동이 가능한지 확인
            if ((0 <= x_new && x_new < N) && (0 <= y_new && y_new < M)){        // 일단 범위안에 있는지 확인
                if (maze[x_new][y_new] == 1) {                              // 벽일 경우
                    if (visited[x_new][y_new][1] == 0 && destroyed == 0) {     // 방문이력 없고, 벽을 부술수 있다면
                        q.push(make_tuple(x_new, y_new, 1));                    // 파괴이력 추가
                        visited[x_new][y_new][1] = visited[x][y][destroyed] + 1;         // 방문길이 추가
                        //cout << "추가됨1" << endl;
                        //cout << visited[x_new][y_new] << endl;
                    }
                }
                else {                                                      // 벽이 아닐 경우
                    if (visited[x_new][y_new][destroyed] == 0 && (x_new != 0 or y_new != 0)) {       // 방문기록 없고, 처음이 아닐 경우
                        q.push(make_tuple(x_new, y_new, destroyed));
                        visited[x_new][y_new][destroyed] = visited[x][y][destroyed] + 1;
                        //cout << "추가됨2" << endl;
                    }
                }
                /*
                && !visited[x_new][y_new] && maze[x_new][y_new] == 1) {

                visited[x_new][y_new] = 1;              // 인접 좌표는 방문한 것으로 저장
                q.push(make_pair(x_new, y_new));        // 인접 좌표를 queue 에 삽입
                dist[x_new][y_new] = dist[x][y] + 1;    // 인접 좌표까지 이동한 거리 저장
                */
            }
        }
    }
    cout << -1 << endl;
    return;
    
}

int main() {

    cin >> N >> M;                      // 미로 크기 입력

    for (int i = 0; i < N; ++i) {            // 미로 입력

        string row;                     // 행 입력
        cin >> row;

        for (int j = 0; j < M; ++j) {        // 행 별 좌표값 저장
            maze[i][j] = row[j] - '0';    // 행 별 좌표값들은 문자 형태이기 때문에, 숫자로 변환
        }
    }

    bfs(0, 0);                          // 미로 탐색 시작

    
}


// 벽뚫고 방문이랑 그냥 방문 차이있음 이부분 추가