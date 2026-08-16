#include <bits/stdc++.h>
using namespace std;

const int N = 1005, K = 105;

template <class T>
void read(T &x) {
	int sgn = 1;
	char ch;
	x = 0;
	for (ch = getchar(); (ch < '0' || ch > '9') && ch != '-'; ch = getchar()) ;
	if (ch == '-') ch = getchar(), sgn = -1;
	for (; '0' <= ch && ch <= '9'; ch = getchar()) x = x * 10 + ch - '0';
	x *= sgn;
}
template <class T>
void write(T x) {
	if (x < 0) putchar('-'), write(-x);
	else if (x < 10) putchar(x + '0');
	else write(x / 10), putchar(x % 10 + '0');
}

int n = 0, k, a[K], b[N];
bool tag[K], valid[N];
// validity check
// last denotes the largest index i such that i <= pre and valid[i] = false.
// len denotes the largest length of suffix such that b[pre], b[pre - 1], ..., b[pre - len + 1] are distinct.
bool pre_valid[N];
bool solve1(int pre, int last, int len, int num) {
	for (int i = 1; i <= k; i++) {
		if (!tag[i] && !(a[i] - 1 <= num && num <= (a[i] << 1) - 1)) return false;
	}
	pre_valid[pre - len] = true;
	for (int i = pre - len + 1; i <= pre; i++) {
		pre_valid[i] = pre_valid[i - 1];
		if (!(a[b[i]] - 1 <= num && num <= (a[b[i]] << 1) - 1)) pre_valid[i] = false;
	}
	for (int i = pre; i > pre - len; i--) {
		if (!(a[b[i]] <= num && num <= (a[b[i]] << 1))) break;
		if (i <= last && pre_valid[i - 1]) return true;
	}
	return false;
}
bool solve2(int pre, int last, int len, int num) {
	for (int i = 1; i <= k; i++) {
		if (!tag[i] && !(a[i] <= num && num <= (a[i] << 1) - 1)) return false;
	}
	pre_valid[pre - len] = true;
	for (int i = pre - len + 1; i <= pre; i++) {
		pre_valid[i] = pre_valid[i - 1];
		if (!(a[b[i]] <= num && num <= (a[b[i]] << 1) - 1)) pre_valid[i] = false;
	}
	int pos1 = 0, pos2 = n + 1;
	for (int i = pre; i > pre - len; i--) {
		if (a[b[i]] <= num && num <= (a[b[i]] << 1 | 1)) {
			if (num == a[b[i]]) {
				if (!pos1) pos1 = i; 
			}
			if (num == (a[b[i]] << 1 | 1)) pos2 = i;
		} else break;
		if (i <= last && pos1 <= pos2 && pre_valid[i - 1]) return true;
	}
	return false;
}
bool solve(int pre, int last, int len, int num) {
	return solve1(pre, last, len, num) || solve2(pre, last, len, num);
}

bool check(int pre) {
	for (int i = 1; i <= k; i++) tag[i] = false;
	int len = min(pre, k);
	for (int i = pre; i && i > pre - k; i--) {
		if (tag[b[i]]) {
			len = pre - i;
			break;
		}
		tag[b[i]] = true;
	}
	int last = pre + 1;
	if (len < k) {
		for (int i = pre; i && i > pre - k; i--) {
			if (!valid[i]) last = i;
		}
	}
	int mx = 0;
	for (int i = 1; i <= k; i++) mx = max(mx, a[i] - 1);
	for (int i = 1; i <= k; i++) tag[i] = false;
	for (int i = pre; i > pre - len; i--) tag[b[i]] = true;
	return solve(pre, last, len, mx) || solve(pre, last, len, mx + 1);
}

int main() {
	read(k);
	for (int i = 1; i <= k; i++) read(a[i]), n += a[i];
	bool flag = true;
	for (int i = 1; i <= n; i++) {
		bool chk = false;
		for (int j = 1; j <= k; j++) {
			b[i] = j, a[j]--, valid[i] = false;
			if (check(i)) {
				chk = true;
				break;
			} else a[j]++;
		}
		bool k_distinct = i >= k;
		for (int j = 1; j <= k; j++) tag[j] = false;
		for (int j = i; j && j > i - k; j--) {
			if (tag[b[j]]) k_distinct = false;
			tag[b[j]] = true;
		}
		if (k_distinct) {
			for (int j = i; j > i - k; j--) valid[j] = true;
		}
		if (!chk) {
			flag = false;
			break;
		}
	}
	if (flag) {
		for (int i = 1; i <= n; i++) write(b[i]), putchar(' ');
		putchar('\n');
	} else puts("-1");
	return 0;
}