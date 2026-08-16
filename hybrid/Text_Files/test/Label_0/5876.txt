#include <iostream>
#include <math.h>
#include <string>
using namespace std;

int main() {
    int t, n, a, b;
    string s;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> n >> a >> b >> s;
        if (b >= 0) {
            cout << (a + b) * n << "\n";
        } 
        else {
            int min;
            int i = 1;
            while (i < s.length()) {
                if (s.at(i) == s.at(i - 1)) {
                    s.erase(i,1);
                } else i++;
            }
            min = s.length() / 2 + 1;
            cout << a * n + b * min << "\n";
        }
    }
}