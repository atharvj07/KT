#include <bits/stdc++.h>
using namespace std;
int main(){
  int N;
  cin >> N;
  set<int> S;
  for (int i = 0; i < N; i++){
    int A;
    cin >> A;
    if (!S.count(A)){
      S.insert(A);
    } else {
      S.erase(A);
    }
  }
  cout << S.size();
}