#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

#define MOD 1000000007
long long N;
string s;
bool ans[100000];

int main() {
    cin >> N >> s;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            ans[0] = (bool)i;
            ans[1] = (bool)j;
            for (int k = 2; k < N; k++) {
                if (s[k-1] == 'o') ans[k] = ans[k-1] ^ ans[k-2];
                else ans[k] = !(ans[k-1] ^ ans[k-2]);
            }
            if (((s[N-1] == 'o' && ans[0] == ans[N-1] ^ ans[N-2]) || (s[N-1] == 'x' && ans[0] == !(ans[N-1] ^ ans[N-2]))) 
            && ((s[0] == 'o' && ans[1] == ans[N-1] ^ ans[0]) || (s[0] == 'x' && ans[1] == !(ans[N-1] ^ ans[0])))) {
                for (int k = 0; k < N; k++) {
                    cout << (ans[k] ? 'W' : 'S');
                }
                cout << endl;
                return 0;
            }
        }
    }
    cout << -1 << endl;
}