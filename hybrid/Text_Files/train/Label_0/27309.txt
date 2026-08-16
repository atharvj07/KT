#include <iostream>

using namespace std;

int main(){
  int N, M, a;
  cin >> N >> M;
  for (int i=0; i<M; i++){
    cin >> a;
    N -= a;
  }
  cout << (N >= 0 ? N : -1) << "\n";
  return 0;
}