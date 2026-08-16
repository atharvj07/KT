#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>
#include <utility>

using namespace std;

int gcd(int a, int b){
	if(a < b) swap(a,b);
	if(a == 0 || b == 0) return max(a,b);
	else return gcd(b, a % b);
}

int eulerPhi(int n){
	if(n == 0) return 0;
	int ans = n;
	for(int i = 2; i * i <= n; i++){
		if(n % i == 0){
			ans -= ans / i;
			while(n % i == 0) n /= i;
		}
	}
	if(n > 1) 
		ans -= ans / n;
	return ans;
}


int main(){
	int n, cnt = 0;
	cin >> n;
	cout << eulerPhi(n) << endl;
	return 0;
}