#include <bits/stdc++.h>
using namespace std;
vector<vector<int> > arbres_somme;
void add(int idA, int id, int deb, int fin, int first, int last, int val) {
  if (deb == first and fin == last) {
    arbres_somme[idA][id] += val;
  } else if (deb < last and first < fin and deb + 1 < fin) {
    add(idA, 2 * id + 1, deb, (deb + fin) / 2, first,
        min(last, (deb + fin) / 2), val);
    add(idA, 2 * id + 2, (deb + fin) / 2, fin, max(first, (deb + fin) / 2),
        last, val);
  }
}
int lire_val(int idA, int id, int deb, int fin, int cible) {
  if (deb + 1 == fin)
    return arbres_somme[idA][id];
  else if (cible >= deb and cible < (deb + fin) / 2)
    return arbres_somme[idA][id] +
           lire_val(idA, 2 * id + 1, deb, (deb + fin) / 2, cible);
  else
    return arbres_somme[idA][id] +
           lire_val(idA, 2 * id + 2, (deb + fin) / 2, fin, cible);
}
int main() {
  int n, q, ui, vi;
  scanf("%d %d", &n, &q);
  vector<vector<int> > graphe(n);
  for (int i = 0; i < n - 1; i++) {
    scanf("%d %d", &ui, &vi);
    graphe[ui - 1].push_back(vi - 1);
    graphe[vi - 1].push_back(ui - 1);
  }
  int nbBranches = graphe[0].size();
  vector<pair<int, int> > borne(n, make_pair(-1, -1));
  vector<int> tailleBranche(nbBranches);
  borne[0] = make_pair(-2, 0);
  for (int i = 0; i < nbBranches; i++) {
    int curr = graphe[0][i], prof;
    borne[curr] = make_pair(i, 0);
    for (prof = 1; graphe[curr].size() == 2; prof++) {
      if (borne[graphe[curr][0]].first == -1)
        curr = graphe[curr][0];
      else
        curr = graphe[curr][1];
      borne[curr] = make_pair(i, prof);
    }
    tailleBranche[i] = prof;
  }
  arbres_somme.resize(nbBranches + 1);
  for (int i = 0; i < nbBranches; i++)
    arbres_somme[i].resize(4 * tailleBranche[i], 0);
  arbres_somme[nbBranches].resize(4 * n, 0);
  int nod, val, dis, type;
  for (int i = 0; i < q; i++) {
    scanf("%d", &type);
    if (type == 0) {
      scanf("%d %d %d", &nod, &val, &dis);
      nod--;
      if (nod != 0) {
        add(borne[nod].first, 0, 0, tailleBranche[borne[nod].first],
            max(0, borne[nod].second - dis),
            min(tailleBranche[borne[nod].first], borne[nod].second + dis + 1),
            val);
        if (dis > borne[nod].second)
          add(nbBranches, 0, 0, n, 0, dis - borne[nod].second, val);
        if (dis > borne[nod].second + 1)
          add(borne[nod].first, 0, 0, tailleBranche[borne[nod].first], 0,
              min(dis - borne[nod].second - 1, tailleBranche[borne[nod].first]),
              -val);
      } else
        add(nbBranches, 0, 0, n, 0, dis + 1, val);
    } else {
      scanf("%d", &nod);
      nod--;
      if (nod != 0)
        printf("%d\n",
               lire_val(borne[nod].first, 0, 0, tailleBranche[borne[nod].first],
                        borne[nod].second) +
                   lire_val(nbBranches, 0, 0, n, borne[nod].second + 1));
      else
        printf("%d\n", lire_val(nbBranches, 0, 0, n, 0));
    }
  }
  return 0;
}
