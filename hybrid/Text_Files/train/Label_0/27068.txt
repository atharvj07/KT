#include "bits/stdc++.h"
#include<unordered_map>
#include<unordered_set>
#pragma warning(disable:4996)
using namespace std;
using ld = long double;
template<class t>
using table = vector<vector<t>>;
const ld eps = 1e-9;

//// < "d:\d_download\visual studio 2015\projects\programing_contest_c++\debug\a.txt" > "d:\d_download\visual studio 2015\projects\programing_contest_c++\debug\b.txt"
  
void getnum(const int l, const int r, const vector<pair<ld, ld>>&armonds, const vector<pair<ld, ld>>&lines,vector<pair<int,ld>>&areas) {
	if (l + 1 == r) {
		areas[l].first = armonds.size();
	}
	else {
		int m = (l + r) / 2;
		pair<ld, ld>line(lines[m]);
		vector<pair<ld, ld>>larmonds, rarmonds;
		for (auto armond : armonds) {
			ld ay = line.first + line.second*armond.first;
			if (ay > armond.second) {
				larmonds.emplace_back(armond);
			}
			else {
				rarmonds.emplace_back(armond);
			}
		}
		getnum(l, m, larmonds, lines, areas);
		getnum(m, r, rarmonds, lines, areas);
	}
}

int main() {
	while (1) {
		int N, M, W, H, S; cin >> N >> M >> W >> H >> S;
		if (!N)break;
		vector<pair<ld, ld>>lines;
		lines.emplace_back(0, 0);
		for (int i = 0; i < M; ++i) {
			ld l, r; cin >> l >> r;
			lines.emplace_back(l, (r - l) / W);
		}
		vector<pair<ld, ld>>armonds;
		for (int i = 0; i < N; ++i) {
			ld x, y; cin >> x >> y;
			armonds.emplace_back(x, y);
		}
		vector<pair<int, ld>>areas(M);
		{
			ld asum = 0;
			for (int i = 0; i < M; ++i) {
				ld sum= (2 * lines[i + 1].first + W*lines[i + 1].second)*W / 2;
				areas[i].second = sum - asum;
				asum = sum;
			
			}
		}
		getnum(0, M, armonds, lines, areas);
		int l = 0;
		int r = 0;
		ld needarea = W*H - S + eps;
		ld sum = 0;
		int num = 0;
		int ans = 0;
		bool flag = true;
		while (1) {
			while (sum < needarea) {
				ans = max(ans, num);
				if (r == M) {
					flag = false;
					break;
				}
				else {
					sum += areas[r].second;
					num += areas[r].first;
				}
				r++;
			}
			if (!flag)break;
			while (sum > needarea) {
				sum -= areas[l].second;
				num -= areas[l].first;
				l++;
			}
		}
		cout << N-ans << endl;

	}
	return 0;
}