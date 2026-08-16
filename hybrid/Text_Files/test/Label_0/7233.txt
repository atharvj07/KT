#include <bits/stdc++.h>
using namespace std;

int main() {
long long x;
cin >> x;
long long ansone=(x/11)*2;
if(x%11>6)ansone+=2;
else if(x%11>0)ansone++;

cout << ansone << endl;
}
