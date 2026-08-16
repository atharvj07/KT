#include <bits/stdc++.h>
using namespace std;
int v[5010];
int n;
int cont[5010][5010];
int solve(int x, int y) {
  int sum = 0;
  sum += cont[v[x]][n - 1] - cont[v[x]][y];
  sum += cont[v[y]][n - 1] - cont[v[y]][x];
  int interval = y - x - 1;
  int menores = cont[v[y]][y - 1] - cont[v[y]][x];
  sum -= interval - menores;
  menores = cont[v[x]][y - 1] - cont[v[x]][x];
  sum += interval - menores;
  return sum;
}
int main(void) {
  cin >> n;
  for (int i = 0; i < n; ++i) cin >> v[i];
  memset(cont, 0, sizeof cont);
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      if (v[j] < i && j > 0) {
        cont[i][j] = cont[i][j - 1] + 1;
      } else if (j > 0)
        cont[i][j] = cont[i][j - 1];
      else
        cont[i][j] = (v[j] < i);
    }
  }
  int sum = 0;
  for (int i = 0; i < n; ++i) {
    for (int j = i + 1; j < n; ++j) {
      if (v[j] < v[i]) {
        sum++;
      }
    }
  }
  int maior = 0x3f3f3f3f;
  int contador = 0;
  for (int i = 0; i < n; ++i) {
    for (int j = i + 1; j < n; ++j) {
      int cop = sum;
      cop -= cont[v[i]][n - 1] - cont[v[i]][i];
      cop -= cont[v[j]][n - 1] - cont[v[j]][j];
      cop += solve(i, j);
      if (maior > cop) {
        maior = cop;
        contador = 1;
      } else if (maior == cop) {
        contador++;
      }
    }
  }
  printf("%d %d\n", maior, contador);
  return 0;
}
