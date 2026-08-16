#include "bits/stdc++.h"
using namespace std;
using ld = long double;
const ld eps = 1e-9;

int N;

bool check(const vector<pair<ld, ld>>&cs, const ld amid) {
	map<ld, int>mp;
	for (auto c : cs) {
		const ld r = c.second;
		const ld x = c.first;
		if (r > amid) {
			ld dis = sqrt(r*r - amid*amid);
			mp[x - dis]++;
			mp[x + dis]--;
		}
	}
	ld pre = -1;
	int num = 0;
	ld len = 0;
	bool preok = false;
	for (auto m : mp) {
		num += m.second;
		if (num) {
			if (!preok) {
				pre = m.first;
			}
		}
		else {
			if (preok) {
				len = max(len, m.first - pre);
			}
		}
		preok = num;
	}
	return amid*2 < len;
}
int main() { 
	while (1) {
		cin >> N;
		if (!N)break;
		vector<pair<ld, ld>>cs;
		for (int i = 0; i < N; ++i) {
			int x, r; cin >> x >> r;
			cs.push_back(make_pair(x, r));
		}
		ld amin = 0;
		ld amax = 1e6;
		int atime = 40;
		while (atime--) {
			ld amid = (amin + amax) / 2;
			if (check(cs, amid)) {
				amin = amid;
			}
			else {
				amax = amid;
			}
		}
		cout << setprecision(22) << fixed << amin*2 << endl;
	}
	
	return 0;
}