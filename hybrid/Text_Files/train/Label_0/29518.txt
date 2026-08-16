#include <bits/stdc++.h>
using namespace std;

int main() {
  int A;
  string M;
  cin>>A>>M;
  int N = M.size();
  for(int i=0; i<N; i++){
    M.at(i) = (M.at(i)-'A'+A)%26 +'A';
  }
  cout<<M<<endl;
}