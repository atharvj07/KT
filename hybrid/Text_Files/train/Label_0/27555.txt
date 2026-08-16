#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<map>
#include<cmath>
using namespace std;
typedef long long ll;
 
const int INF = 0x3f3f3f3f;
ll cal(ll x, ll y) {
	return x * x + y * y;
}
bool check(ll x, ll y, ll d) {
	return cal(x,y) <= d * d;
}
int main()
{
	int t;
	cin >> t;
	while (t--) {
		ll d, k;
		cin >> d >> k;
		ll now = 0;
		ll cnt = 0;
		ll x = 0, y = 0;
		while (now <= d * d) {
			x += k;
			y += k;
			now = cal(x, y);
			cnt++;
		}
		now -= k * k * 2;
		cnt--;
		if (check(cnt * k + k, cnt * k, d)) {
			cout << "Ashish\n";
		}
		else {
			cout << "Utkarsh\n";
		}
	}
	return 0;
}