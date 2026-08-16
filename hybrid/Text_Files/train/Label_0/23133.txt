#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main() {
	vector<pair<int, char>> *vx = new vector<pair<int, char>>[200001];
	vector<pair<int, char>> *vx_puls_y = new vector<pair<int,char>>[400001];
	int n;
	cin >> n;
	int* x = new int[n];
	int* y = new int[n];
	int min_collision_time = 1e9;
	char* muki = new char[n];
	for (int i = 0;i < n;i++) {
		cin >> x[i] >> y[i] >> muki[i];	
	}
	for (int rot = 0;rot < 4;rot++) {
		vx = new vector<pair<int, char>>[200001];
		vx_puls_y = new vector<pair<int, char>>[400001];
		for (int i = 0;i < n;i++) {
			int nx = 200000 - y[i];
			int ny = x[i];
			switch (muki[i])
			{
			case 'U':
				muki[i] = 'L';
				break;
			case 'R':
				muki[i] = 'U';
				break;
			case 'D':
				muki[i] = 'R';
				break;
			case 'L':
				muki[i] = 'D';
				break;
			default:
				break;
			}
			x[i] = nx;
			y[i] = ny;
			if (muki[i] == 'U' || muki[i] == 'D') {
				vx[x[i]].push_back(make_pair(y[i], muki[i]));
			}
			if (muki[i] == 'U' || muki[i] == 'R') {
				vx_puls_y[x[i] + y[i]].push_back(make_pair(y[i], muki[i]));
			}
			
		}
		for (int i = 0;i < 200001;i++) {
			sort(vx[i].begin(), vx[i].end());
			for (int j = 0;j < (signed)vx[i].size() - 1;j++) {
				if (vx[i][j].second == 'U' && vx[i][j + 1].second == 'D') {
					min_collision_time = min(min_collision_time, (vx[i][j + 1].first - vx[i][j].first) * 5);
				}
			}
		}
		for (int i = 0;i < 400001;i++) {
			sort(vx_puls_y[i].begin(), vx_puls_y[i].end());
			for (int j = 0;j < (signed)vx_puls_y[i].size() - 1;j++) {
				if (vx_puls_y[i][j].second == 'U' && vx_puls_y[i][j + 1].second == 'R') {
					min_collision_time = min(min_collision_time, (vx_puls_y[i][j + 1].first - vx_puls_y[i][j].first) * 10);
				}
			}
		}
	}
	if (min_collision_time == 1e9) {
		cout << "SAFE\n";
	}
	else {
		cout << min_collision_time << endl;
	}
}