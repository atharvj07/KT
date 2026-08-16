#include <bits/stdc++.h>

using namespace std;

string Input, Output;
const char ChangeTable[5][6] = { 'a','f','k','p','u','z',
								 'b','g','l','q','v','.',
								 'c','h','m','r','w','?', 
								 'd','i','n','s','x','!', 
								 'e','j','o','t','y',' ', };

bool solve(int len) {
	for (int i = 0; i < len; i += 2) {
		//cout << Input[i];
		if (Input[i]>'6' || Input[i]<'1' || Input[i + 1]>'5' || Input[i + 1] < '1') {
			return false;
		}
		//cout << ChangeTable[Input[i + 1] - '0' - 1][Input[i] - '0' - 1] << endl;
		Output += ChangeTable[Input[i+1] - '0'-1][Input[i] - '0'-1];
	}
	return true;
}

int main() {
	int len;

	while (cin >> Input) {
		len = Input.size();
		Output = "";
		if (len % 2 == 0 && solve(len)) {
			cout << Output << endl;
		}
		else {
			cout << "NA" << endl;
		}
		
	}

	return 0;
}
