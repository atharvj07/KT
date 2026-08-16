#define _USE_MATH_DEFINES

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>

using namespace std;

//typedef pair<long long int, long long int> P;

long long int INF = 1e18;
long long int MOD = 1e9 + 7;

int main(){
	
	int N;
	cin >> N;
	
	int a[2000];
	for(int i = 0; i < N; i++){
		cin >> a[i];
	}
	
	for(int i = 0; i < N; i++){
		for(int j = i + 1; j < N; j++){
			if((a[i] - a[j]) % (N - 1) == 0){
				cout << a[i] << " " << a[j] << endl;
				return 0;
			}
		}
	}
	
	return 0;
}

