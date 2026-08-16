#include <iostream>
#include <string>
#include <vector>

using namespace std;



int main()
{
	string s, t = "keyence";
	cin >> s;
	
	for (int i = 0; i < s.length(); i++) {
		for (int j = i - 1; j < s.length(); j++) {
			if (s.substr(0, i) + s.substr(j + 1, s.length() - j + 1) == t) {
				cout << "YES" << endl;
				return 0;
			}
		}
	}
	cout << "NO" << endl;

	return 0;
}