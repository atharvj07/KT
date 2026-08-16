//先頭の文字以外は必要ない。先頭の文字の個数をcnt[i]などで持ち、残り数が多いほうから使っていく。(未証明)

#include <iostream>
#include <string>
#include <algorithm>
#include <functional>
using namespace std;

int n, k;
string p[10000];
int cnt[26];

int main() {
	int i, j;
	
	cin >> n >> k;
	for (i = 0; i < n; i++) {
		cin >> p[i];
		cnt[p[i][0] - 'A']++;
	}
	
	for (i = 0; ; i++) {
		sort(cnt, cnt + 26, greater<int>());
		if (cnt[k - 1] <= 0) break;
		for (j = 0; j < k; j++) cnt[j]--;
	}
	cout << i << endl;
	return 0;
}