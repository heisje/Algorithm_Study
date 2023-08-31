// [BOJ]_20006_랭킹전_대기열.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

// 실시간은 벡터로 관리

#include <iostream>
#include <string>
#include <vector>
#include <tuple>

#include <algorithm>

using namespace std;

int main()
{
	vector < tuple<int, int, vector<string>>> real_time_rooms;		// 방번호, 레벨, 이름들
	vector<pair<bool, vector<pair<int, string>> >> rooms_record;							// 생성된 방들 기록용


	int n, m;			// 이름 수, 정원
	int abs_room_num = 0;

	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		int level;
		string new_name;
		bool found_room = false;

		
		cin >> level >> new_name;
		//cout << level << " " << new_name << " 입력합니다." << endl;

		for (int j = 0; j < real_time_rooms.size(); j++) {
			if (level - 10 <= get<1>(real_time_rooms[j]) && get<0>(real_time_rooms[j]) <= level + 10) {	// 있는 방 중에 적정 레벨 발견
				//cout << "찾음" << endl;
				get<2>(real_time_rooms[j]).push_back(new_name);	// 인원추가
				
				//rooms_record[get<0>(real_time_rooms[j])].push_back(new_name);	// 방 기록의 절대 위치에 집어넣어야함 
				rooms_record[get<0>(real_time_rooms[j])].second.push_back(make_pair(level, new_name));
				if (get<2>(real_time_rooms[j]).size() == m) {	// 최대인원 확인시 삭제
					//cout << "최대인원" << endl;
					rooms_record[get<0>(real_time_rooms[j])].first = true;
					real_time_rooms.erase(real_time_rooms.begin() + j);	// 그냥 j로 사용 불가능... iterator를 넣어주어야함
				}
				found_room = true;
				break;
			}
		}
		if (!found_room) {		// 못찾았을 경우 새로 만들자
			//cout << "못찾음" << endl;
			vector<pair<int, string>> tmp1;
			vector<string> tmp2;
			tmp1.push_back(make_pair(level, new_name));
			tmp2.push_back(new_name);
			
			if (m == 1) {	// 방인원이 1인경우
				rooms_record.push_back(make_pair(true, tmp1));
			}
			else {
				rooms_record.push_back(make_pair(false, tmp1));
				real_time_rooms.push_back(make_tuple(abs_room_num, level, tmp2));
				abs_room_num++;
			}
			
		}
	}

	for (int k = 0; k < rooms_record.size(); k++) {
		if (rooms_record[k].first) {
			cout << "Started!" << endl;
		}
		else {
			cout << "Waiting!" << endl;
		}
		sort(rooms_record[k].second.begin(), rooms_record[k].second.end(), [](const auto& a, const auto& b) {
			return a.second < b.second;
			});
		for (int p = 0; p < rooms_record[k].second.size(); p++) {
			cout << rooms_record[k].second[p].first << " " << rooms_record[k].second[p].second << endl;
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
