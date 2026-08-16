#include<bits/stdc++.h>
typedef long double db;
int n,l;
int a[3000];
int main()
{
	std::ios::sync_with_stdio(false),std::cin.tie(0);
	std::cin >> n >> l;
	db x = 0,y = 0;
	for(int i = 0;i < n;++i) std::cin >> a[i];
	const db pi = std::acos(-1);
	for(int i = 0;i < n;++i){
		for(int j = 0;j < i;++j){
			x += std::cos(pi * (a[i] + a[j]) / l) * (n - (i - j) * 2);
			y += std::sin(pi * (a[i] + a[j]) / l) * (n - (i - j) * 2);
		}
	}
	x /= (db) n * (n - 1) * (n - 2) / 6;
	y /= (db) n * (n - 1) * (n - 2) / 6;
	printf("%.18Lf %.18Lf\n",x,y);
}
