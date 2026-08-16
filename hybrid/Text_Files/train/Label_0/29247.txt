#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;
#define REP(i, a, n) for(int i=a; i<n; i++)
#define F first
#define S second
#define MP(a, b) make_pair(a, b)

int main()
{
	int M, N;
	char field[501][501];
	vector<vector<pair<int, int>>> v(26);
	cin >> M >> N;
	REP(i, 0, M) REP(j, 0, N) {
		cin >> field[i][j];
		if (field[i][j] != '.') {
			v[field[i][j] - 'A'].push_back(MP(i, j));
		}
	}

	int point = 0;
	bool flag = true;
	while (flag) {
		flag = false;
		
		REP(k, 0, 26) {
			if (v[k].size() == 0) continue;
			
			bool del_flag = false;
			int y1 = v[k][0].F, y2 = v[k][1].F;
			int x1 = v[k][0].S, x2 = v[k][1].S;
			int ymin = min(y1, y2), ymax = max(y1, y2);
			int xmin = min(x1, x2), xmax = max(x1, x2);

			if (y1 == y2) {
				REP(l, xmin + 1, xmax) {
					if (field[y1][l] == '.') {
						del_flag = true;
					}
					else {
						del_flag = false;
						break;
					}
				}
			}

			else if (x1 == x2) {
				REP(l, ymin + 1, ymax) {
					if (field[l][x1] == '.') {
						del_flag = true;
					}
					else {
						del_flag = false;
						break;
					}
				}
			}

			else {
				if (field[ymin][xmin] == '.') {
					REP(i, ymin, ymax) {
						if (field[i][xmin] != '.') {
							del_flag = false;
							break;
						}
						else del_flag = true;
					}
					if (del_flag) {
						REP(j, xmin, xmax) {
							if (field[ymin][j] != '.') {
								del_flag = false;
								break;
							}
							else del_flag = true;
						}
					}
				}

				if (!del_flag && field[ymin][xmax] == '.') {
					REP(i, ymin, ymax) {
						if (field[i][xmax] != '.') {
							del_flag = false;
							break;
						}
						else del_flag = true;
					}
					if (del_flag) {
						REP(j, xmin + 1, xmax + 1) {
							if (field[ymin][j] != '.') {
								del_flag = false;
								break;
							}
							else del_flag = true;
						}
					}
				}

				if (!del_flag && field[ymax][xmin] == '.') {
					REP(i, ymin + 1, ymax + 1) {
						if (field[i][xmin] != '.') {
							del_flag = false;
							break;
						}
						else del_flag = true;
					}
					if (del_flag) {
						REP(j, xmin, xmax) {
							if (field[ymax][j] != '.') {
								del_flag = false;
								break;
							}
							else del_flag = true;
						}
					}
				}

				if (!del_flag && field[ymax][xmax] == '.') {
					REP(i, ymin + 1, ymax + 1) {
						if (field[i][xmax] != '.') {
							del_flag = false;
							break;
						}
						else del_flag = true;
					}
					if (del_flag) {
						REP(j, xmin + 1, xmax + 1) {
							if (field[ymax][j] != '.') {
								del_flag = false;
								break;
							}
							else del_flag = true;
						}
					}
				}
			}

			if (del_flag) {
				field[y1][x1] = '.';
				field[y2][x2] = '.';
				v[k].pop_back();
				v[k].pop_back();
				point += 2;
				flag = true;
			}
		}
	}

	cout << point << endl;
	return 0;
}