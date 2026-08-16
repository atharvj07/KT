#include<iostream>
#include<vector>
#include<utility>
#include<algorithm>
#include<string>
#include<cstdio>
#include<queue>
#include<functional>
#include<tuple>
#include<iomanip>
#include<stack>
#include<cmath>
#define ll long long
using namespace std;
int main() {
	double d,m; cin >> d;
	m = sqrt(2)*d;
	if (sqrt(d*d - floor(d)*floor(d)) <= 1.0) m = max(m, floor(d) + 1);
	printf("%.10f\n", m);
	return 0;
}
