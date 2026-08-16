#include<iostream>
using namespace std;
int main() {
char S;
int N,R=0,i;
cin >> N;
for(i=0;i<N;i++) {
cin >> S;
if(S == 'R')R++;
}
if(R*2 > N)cout << "Yes" << endl;
else cout << "No" << endl;
}