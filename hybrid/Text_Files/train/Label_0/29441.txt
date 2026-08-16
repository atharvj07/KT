//sort(a,b, std::greater<>()); 降順
//vector a = b はDeepCopy
//sort(a,b,[](const fruit& x, const fruit& y) { return x.price > y.price;});
//#define PI 3.14159265359
#include <iostream> // cout, endl, cin
#include <string> // string, to_string, stoi
#include <vector> // vector
#include <algorithm> // min, max, swap, sort, reverse, lower_bound, upper_bound
#include <utility> // pair, make_pair
#include <tuple> // tuple, make_tuple
#include <cstdint> // int64_t, int*_t
#include <cstdio> // printf
#include <map> // map
#include <queue> // queue, priority_queue
#include <set> // set
#include <stack> // stack
#include <deque> // deque
#include <unordered_map> // unordered_map
#include <unordered_set> // unordered_set
#include <bitset> // bitset
#include <cctype> // isupper, islower, isdigit, toupper, tolower
using namespace std;
bool Data[1009];
bool Data2[1009];
int main()
{	
	int t;
	cin >> t;
	for (int ii = 0; ii < t; ii++) {
		int n, m;
		cin >> n >> m;
		for (int i = 1; i <= n; i++) {
			char a;
			cin >> a;
			if (a == '0') {
				Data[i] = false;
			}
			else {
				Data[i] = true;
			}
		}
		Data[0] = false;
		Data[n + 1] = false;
		for (int i = 0; i < m; i++) {
			bool flag = false;
			vector<int> add;
			for (int j = 1; j <= n; j++) {
				if (Data[j] == false) {
					if ((Data[j - 1] == false && Data[j + 1] == true) || (Data[j - 1] == true && Data[j + 1] == false)) {
						add.push_back(j);
						flag = true;
					}
				}
			}
			for (int j = 0; j < add.size(); j++) {
				Data[add[j]] = true;
			}
			if (flag == false) {
				break;
			}
		}
		for (int i = 1; i <= n; i++) {
			if (Data[i] == true) {
				cout << 1;
			}
			else {
				cout << 0;
			}
		}
		cout << endl;
	}
}