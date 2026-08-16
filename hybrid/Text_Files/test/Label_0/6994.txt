#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
//#include <sstream>
#include <vector>
#include <set>
#include <string>
#include <cmath>
#include <algorithm>
#include <map>
#include <queue>
#include <iomanip>
#include <cstring>
#include <stdio.h>
#include <cassert>
using namespace std;



void solve() {
	int n;
	cin >> n;
	vector<int>all(n);
	for (int i = 0; i < n; i++)
		cin >> all[i];
	if (n == 1) {
		cout << "YES" << '\n';
		return;
	}
	set<int>f;
	f.insert(all[0]);
	for (int i = 1; i < n; i++) {
		if (all[i] == all[i - 1]) {
			f.insert(all[i]);
			continue;
		}
		if (all[i] > all[i - 1]) {
			if (*f.rbegin() > all[i - 1]) {
				int x = *f.upper_bound(all[i - 1]);
				if (x < all[i]) {
					cout << "NO" << '\n';
					return;
				}
			}
		}
		if (all[i] < all[i - 1]) {
			if (*f.rbegin() > all[i]) {
				int x = *f.upper_bound(all[i]);
				if (x < all[i - 1]) {
					cout << "NO" << '\n';
					return;
				}
			}
		}
		f.insert(all[i]);
	}
	cout << "YES" << '\n';
}

int main() {
	#ifdef _DEBUG
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif // _DEBUG
	int t;
	cin >> t;
	//t = 1;
	while (t) {
		t--;
		solve();
	}
}