#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	map<string, vector<int> > dict;
	
	string s;
	int p;
	while (cin >> s >> p) {
		dict[s].push_back(p);
	}
	
	map<string, vector<int> >::iterator it;
	for (it = dict.begin(); it != dict.end(); it++) {
		vector<int> v = (*it).second;
		int size = v.size();
		
		sort(v.begin(), v.end());
		
		cout << (*it).first << endl;
		for (int i = 0; i < size - 1; i++) {
			cout << v[i] << " ";
		}
		cout << v[size - 1] << endl;
	}
	
	return 0;
}