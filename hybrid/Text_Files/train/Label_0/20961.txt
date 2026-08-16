#define  _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <algorithm>
#include <utility>
#include <functional>
#include <cstring>
#include <queue>
#include <stack>
#include <math.h>
#include <iterator>
#include <vector>
#include <string>
#include <set>
#include <math.h>
#include <iostream>
#include <random>
#include<map>
#include <iomanip>
#include <time.h>
#include <stdlib.h>
#include <list>
#include <typeinfo>
#include <list>
#include <set>
#include <cassert>
#include<fstream>
#include <unordered_map>
#include <cstdlib>
using namespace std;
#define Ma_PI 3.141592653589793
#define eps 0.00000001
#define LONG_INF 3000000000000000000
#define GOLD 1.61803398874989484820458
#define MAX_MOD 1000000007
#define MOD 998244353
#define REP(i,n) for(long long i = 0;i < n;++i)    
#define seg_size 524288
long long geko[100000] = {};
long long dodo[100000] = {};
long long solve(long long now,long long hoge) {
	if (dodo[now]) return geko[now];
	dodo[now] = 1;
	if (hoge % now == 0) {
		return geko[now] = 0;
	}
	return geko[now] = solve(now + 1, hoge) + 1;
}
int main(){
#define int long long
	int n;
	cin >> n;
	vector<int> input;
	REP(i, n) {
		int a;
		cin >> a;
		input.push_back(a);
	}
	sort(input.begin(), input.end());
	int ans = 0;
	REP(i, n) {
		ans += solve(input[i], input[n - 1]);
	}
	cout << ans << endl;
	return 0;
}
