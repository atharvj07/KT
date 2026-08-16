#include <iostream>
using namespace std;

int main() {

	int n;
	int key[100];
	
	while(cin >> n, n) {
		for (int i = 0; i < n; i++) {
			cin >> key[i];
		}
		
		string str;
		cin >> str;
		
		for (int i = 0; i < str.size(); i++) {
			char c;
			if (str[i] >= 'A' && str[i] <= 'Z') {
				c = str[i] - 'A';
			} else {
				c = str[i] - 'A' - 6;
			}
			c -= key[i % n];
			if (c < 0) c += 52;
			
			if (c >= 0 && c <= 25) {
				cout << (char)(c + 'A');
			} else {
				cout << (char)(c + 'A' + 6);
			}
		}
		cout << endl;
	}
}