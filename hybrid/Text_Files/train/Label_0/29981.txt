#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


vector<int> prime;
int ps[10000];


bool judge(int n){
	if (n == 2) return true;
	for (int i = 2; i*i <= n; i++)
		if (n % i == 0) return false;
	return true;
}


void pgen(){
	for (int i = 2; prime.size() != 10000; i++)
		if (judge(i)) prime.push_back(i);
}


void acc(){
	ps[0] = prime[0];
	for (int i = 1; i < 10000; i++)
		ps[i] = ps[i - 1] + prime[i];
}


int main(){
	int n;

	pgen();
	acc();

	while (cin >> n, n != 0) cout << ps[n - 1] << endl;

	return 0;
}