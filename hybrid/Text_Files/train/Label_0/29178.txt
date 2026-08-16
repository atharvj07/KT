#include<bits/stdc++.h>
using namespace std;

char M(char a,char b){
    if(a=='T'&&b=='T')
        return 'T';
    if(a=='T'&&b=='F')
        return 'F';
    if(a=='F'&&b=='T')
        return 'T';
    if (a == 'F' && b == 'F')
        return 'T';
}

int main(){
    int N;
    cin >> N;
    vector<char> P(N);
    for (int i = 0; i < N;i++)
        cin >> P[i];
    char res = P[0];
    for(int i=1;i<N;i++){
        res = M(res, P[i]);
    }
    cout << res << endl;
}
