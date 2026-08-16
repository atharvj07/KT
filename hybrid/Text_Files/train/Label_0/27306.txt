#include <bits/stdc++.h>

using namespace std;

const int N = 200100;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1);


int lis(int a[], int n){
	vector <int> A(n, INF);
	for(int i = 0; i < n; i++){
		*lower_bound(A.begin(), A.end(), a[i]) = a[i];
	}
	return find(A.begin(), A.end(), INF) - A.begin();
}

int main(){

	int x1, y1, x2, y2;
	scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
	int W = abs(x2-x1), H = abs(y2-y1);
	bool flipx = x1 > x2, flipy = y1 > y2;
	int N;
	scanf("%d", &N);
	vector <pair<int,int> > points;
	for(int i = 0; i < N; i++){
		int X, Y;
		scanf("%d%d", &X, &Y);
		X -= x1; Y -= y1;
		if(flipx) X = -X;
		if(flipy) Y = -Y;
		if(0 <= X && X <= W && 0 <= Y && Y <= H){
			points.push_back(make_pair(X, Y));
		}
	} 
	sort(points.begin(), points.end());
	vector <int> vy;
	for(auto p : points){
		vy.push_back(p.second);
	}
	int num = vy.empty() ? 0 : lis(vy.data(), (int)vy.size());
	double ans = (W+H)*100.0;
	if(num < min(W,H) + 1){
		ans -= num * (20 - PI*5.0);
	} 
	else{
		ans -= (num - 1) * (20 - PI*5.0);
		ans += (10*PI - 20);
	}
	printf("%.10lf", ans);
}