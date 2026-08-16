#define _USE_MATH_DEFINES

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <unordered_map> 
#include <unordered_set>
#include <functional>

using namespace std;

typedef pair<long long int, long long int> P;
typedef tuple<int, int, int> T;

long long int INF = 1e18;
long long int MOD = 1e9 + 7;

long long int extGCD(long long int a, long long int b, long long int &x, long long int &y){
	long long int d = a;
	if(b == 0){
		x = 1;
		y = 0;
	}else{
		d = extGCD(b, a % b, y, x);
		y -= a / b * x;
	}
	return d;
}

int main(){
	long long int a, b, x, y, G;
	cin >> a >> b;
	G = extGCD(a, b, x, y);
	cout << x << " " << y << endl;
	return 0;
}
