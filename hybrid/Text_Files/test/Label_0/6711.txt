#include <bits/stdc++.h>
using namespace std;
const int maxn = 1<<18;
int a[maxn];
int rec(int l, int r){
	if(l == r) return a[l];
	int mid = (l + r) >> 1;
	int x = rec(l, mid);
	int y = rec(mid + 1, r);
	if(x > y) return x - y;
	if(x == y) return x;
	if(x < y) return y - x;
	return -1;
}
int main(){
	int n; cin >> n;
	for(int i = 0; i < 1<<n; i++) cin >> a[i];
	cout << rec(0, (1<<n) - 1) << endl;
	return 0;
}
