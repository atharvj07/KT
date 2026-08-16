#define _USE_MATH_DEFINES

#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

typedef pair<long long int, int> P;

long long int INF = 100000000000000000LL;

int main(){
	
	long long int K, A, B;
	cin >> K >> A >> B;
	
	if(K <= A){
		cout << "1" << endl;
		return 0;
	}
	K -= A;
	
	if(A <= B){
		cout << "-1" << endl;
		return 0;
	}
	
	cout << (K / (A - B) + (K % (A - B) != 0)) * 2 + 1 << endl;
	
	return 0;
}