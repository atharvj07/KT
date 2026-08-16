#include<bits/stdc++.h>
using namespace std;
#define ll long long
const int N = 1e6 + 10;
const int INF = 0x3f3f3f3f;
int n;
int a[N], tw = 1;
int cal() {
	int res = 0;
	for (int i = 0; i < n; i++) {
		if (((n - 1)&i) == i)
			res ^= a[i];
	}
	return (res & 1);
}
int main() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		char c;
		scanf(" %c", &c);
		a[i] = c - '1';
		if (a[i] == 1)tw = 0;
	}
	if (cal())puts("1");
	else {
		if (!tw)puts("0");
		else {
			for (int i = 0; i < n; i++)a[i] /= 2;
			if (cal())puts("2");
			else puts("0");
		}
	}
	return 0;
}