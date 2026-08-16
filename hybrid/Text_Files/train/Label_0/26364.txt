#include <iostream>
#include <vector>

#define MAX_N 50000

using namespace std;

bool isprime(int n) {
	for (int i = 2; i * i <= n; i++)
		if (n % i == 0)
			return false;
	return n != 1;
}

int main() {
	int n;
	int g, l;
	vector<int> prime;
	for (int i = 2; i < MAX_N * 2; i++)
		if (isprime(i) == true)
			prime.push_back(i);
	while (cin >> n) {
		g = l;
		vector<int>::iterator it = prime.begin();
		while (it != prime.end()) {
			if (*it < n)
				g = *it;
			if (*it > n) {
				l = *it;
				break;
			}
			it++;
		}
		cout << g << " " << l << endl;
	}
	return 0;
}