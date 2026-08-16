#include <bits/stdc++.h>
using namespace std;
vector<int> dx = {1, -1, 0, 0, 0, 0};
vector<int> dy = {0, 0, 1, -1, 0, 0};
vector<int> dz = {0, 0, 0, 0, 1, -1};
int main(){
  int A, B, C, N;
  cin >> A >> B >> C >> N;
  set<tuple<int, int, int>> st;
  for (int i = 0; i < N; i++){
    int x, y, z;
    cin >> x >> y >> z;
    st.insert(make_tuple(x, y, z));
  }
  long long ans = 2 * ((long long) A * B + (long long) B * C + (long long) C * A);
  for (auto T : st){
    int x = get<0>(T);
    int y = get<1>(T);
    int z = get<2>(T);
    for (int i = 0; i < 6; i++){
      ans++;
      int x2 = x + dx[i];
      int y2 = y + dy[i];
      int z2 = z + dz[i];
      if (x2 < 0){
        ans -= 2;
      }
      if (x2 > A - 1){
        ans -= 2;
      }
      if (y2 < 0){
        ans -= 2;
      }
      if (y2 > B - 1){
        ans -= 2;
      }
      if (z2 < 0){
        ans -= 2;
      }
      if (z2 > C - 1){
        ans -= 2;
      }
      if (st.count(make_tuple(x2, y2, z2))){
        ans--;
      }
    }
  }
  cout << ans << endl;
}
