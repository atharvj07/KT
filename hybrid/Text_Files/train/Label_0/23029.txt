#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 7;

char s[N];

int main(){
	int n, m = 0;
	scanf("%d%s", &n, s);
	for (int i = 0; i < n; i++) if (s[i] == 'R') m ++;

	if (m > n - m) printf("Yes");
	else printf("No");
	return 0;
}