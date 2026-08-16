#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <functional>
using namespace std;
 
typedef long long ll;
 
const int MAXN = 200005;
const int EPS = 1e-8;
const int INF = 1e9+7;
 
ll a[MAXN], b[MAXN];
ll s[MAXN];
 
bool cmp(ll a,ll b){
	return a > b;
}
 
int main(){
	int t;
	scanf("%d", &t);
	while(t--){
		ll n, m;
		scanf("%lld %lld", &n, &m);
		ll ans = 0;
		for (int i = 0; i < n;i++){
			scanf("%lld", &s[i]);
			ans += s[i];
		}
		if(ans<m){
			for (int i = 0; i < n;i++){
				int k;
				scanf("%d", &k);
			}
			printf("-1\n");
			continue;
		}
		int sa = 0, sb = 0;
		for (int i = 0; i < n;i++){
			int k;
			scanf("%d", &k);
			if(k==1) a[sa++] = s[i];
			else b[sb++] = s[i];
		}
		sort(a, a + sa, cmp);
		sort(b, b + sb, cmp);
		ans = 0;
		int sum = 0;
		int smin = INF;
		int i, j;
		for (i = 0; i < sa;i++){
			if(ans>=m){
				smin = min(smin, sum);
				break;
			}
			ans += a[i];
			sum++;
		}
		i--;
		if(ans>=m) smin = min(smin, sum);
		for (j = 0; j < sb;j++){
			ans += b[j];
			sum += 2;
			if(ans>=m&&i>=0){
				while(ans>=m&&i>=0){
					ans -= a[i];
					sum--;
					i--;
				}
				if(ans<m){
					i++;
					ans += a[i];
					sum++;
				}
			}
			if(ans>=m) smin = min(smin, sum);
		}
		printf("%d\n", smin);
	}
	return 0;
}