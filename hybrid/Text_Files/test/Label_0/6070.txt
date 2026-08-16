#include<bits/stdc++.h>
#define rep(i,n)for(int i=0;i<n;i++)
using namespace std;

int main() {
	int n; scanf("%d", &n);
	int cnt = 0;
	rep(i, n) {
		string s; cin >> s;
		if (s == "A")cnt++;
		else cnt--;
		if (cnt < 0)break;
	}
	puts(cnt ? "NO" : "YES");
}