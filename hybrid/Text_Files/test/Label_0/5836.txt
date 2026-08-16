#include <bits/stdc++.h>
using namespace std;
void printList(list<int>* list) {
  cout << "list : ";
  for (__typeof((*list).begin()) li = ((*list).begin()); li != (*list).end();
       ++li) {
    cout << *li << ",";
  }
  cout << endl;
}
void printT_VPII(vector<pair<int, int> > v) {
  cout << "list : ";
  for (__typeof((v).begin()) li = ((v).begin()); li != (v).end(); ++li) {
    cout << " ( " << (*li).first << " , " << (*li).second << " ) ,";
  }
  cout << endl;
}
unsigned int n, m;
map<int, list<int>*> nodeToListPointer;
set<list<int>*> listPointers;
set<pair<int, int> > oldEdges;
vector<pair<int, int> > validEdges;
bool buildValidEdgeSetFromGraph(set<pair<int, int> >& buildGraph,
                                vector<int>& graus, int lastUsedEdgeIndex) {
  if (buildGraph.size() == m) return true;
  for (__typeof(lastUsedEdgeIndex + 1) i = (lastUsedEdgeIndex + 1);
       i <= (static_cast<int>(validEdges.size()) - 1); ++i) {
    pair<int, int> edge = validEdges[i];
    if (graus[edge.first] >= 2 or graus[edge.second] >= 2) continue;
    buildGraph.insert(edge);
    graus[edge.first]++;
    graus[edge.second]++;
    bool resolved = buildValidEdgeSetFromGraph(buildGraph, graus, i);
    if (resolved) return true;
    buildGraph.erase(edge);
    graus[edge.first]--;
    graus[edge.second]--;
  }
  return false;
}
void resolveBruteForce() {
  set<pair<int, int> > validEdgeSet;
  for (__typeof(1) i = (1); i <= (n - 1); ++i)
    for (__typeof(i + 1) j = (i + 1); j <= (n); ++j) {
      validEdgeSet.insert(pair<int, int>(i, j));
    }
  for (__typeof(m) i = 0; i < (m); ++i) {
    unsigned int u, v;
    cin >> u >> v;
    if (u > v) swap(u, v);
    oldEdges.insert(pair<int, int>(u, v));
    validEdgeSet.erase(pair<int, int>(u, v));
  }
  validEdges =
      vector<pair<int, int> >((validEdgeSet).begin(), (validEdgeSet).end());
  set<pair<int, int> > result;
  vector<int> graus = vector<int>(n + 1, 0);
  bool resolved = buildValidEdgeSetFromGraph(result, graus, -1);
  if (not resolved)
    cout << "-1" << endl;
  else {
    for (__typeof((result).begin()) e = ((result).begin()); e != (result).end();
         ++e) {
      pair<int, int> edge = *e;
      cout << edge.first << " " << edge.second << endl;
    }
  }
}
int main() {
  cin >> n >> m;
  if (n < 10) {
    resolveBruteForce();
    return EXIT_SUCCESS;
  }
  for (__typeof(m) i = 0; i < (m); ++i) {
    unsigned int u, v;
    cin >> u >> v;
    list<int>* listEdgeNode_u = NULL;
    list<int>* listEdgeNode_v = NULL;
    if (nodeToListPointer.count(u)) listEdgeNode_u = nodeToListPointer[u];
    if (nodeToListPointer.count(v)) listEdgeNode_v = nodeToListPointer[v];
    if (listEdgeNode_v == NULL and listEdgeNode_u == NULL) {
      listEdgeNode_u = listEdgeNode_v = new list<int>();
      listEdgeNode_u->push_back(u);
      listEdgeNode_u->push_back(v);
      listPointers.insert(listEdgeNode_u);
      nodeToListPointer[u] = nodeToListPointer[v] = listEdgeNode_u;
    } else if (listEdgeNode_v == listEdgeNode_u) {
    } else if (listEdgeNode_v == NULL or listEdgeNode_u == NULL) {
      list<int>* listEdgeNode =
          listEdgeNode_v == NULL ? listEdgeNode_u : listEdgeNode_v;
      if (listEdgeNode->front() == u)
        listEdgeNode->push_front(v);
      else if (listEdgeNode->front() == v)
        listEdgeNode->push_front(u);
      else if (listEdgeNode->back() == v)
        listEdgeNode->push_back(u);
      else if (listEdgeNode->back() == u)
        listEdgeNode->push_back(v);
      else {
      }
      nodeToListPointer[u] = nodeToListPointer[v] = listEdgeNode;
    } else {
      if (listEdgeNode_v->front() == listEdgeNode_u->front()) {
        listEdgeNode_u->reverse();
        listEdgeNode_u->splice(listEdgeNode_u->end(), *listEdgeNode_v);
        delete (listEdgeNode_v);
        listPointers.erase(listEdgeNode_v);
        nodeToListPointer[v] = listEdgeNode_u;
      } else if (listEdgeNode_v->back() == listEdgeNode_u->back()) {
        listEdgeNode_v->reverse();
        listEdgeNode_u->splice(listEdgeNode_u->end(), *listEdgeNode_v);
        delete (listEdgeNode_v);
        listPointers.erase(listEdgeNode_v);
        nodeToListPointer[v] = listEdgeNode_u;
      } else if (listEdgeNode_v->front() == listEdgeNode_u->back()) {
        listEdgeNode_u->splice(listEdgeNode_u->end(), *listEdgeNode_v);
        delete (listEdgeNode_v);
        listPointers.erase(listEdgeNode_v);
        nodeToListPointer[v] = listEdgeNode_u;
      } else if (listEdgeNode_v->front() == listEdgeNode_u->back()) {
        listEdgeNode_v->splice(listEdgeNode_v->end(), *listEdgeNode_u);
        delete (listEdgeNode_u);
        listPointers.erase(listEdgeNode_u);
        nodeToListPointer[u] = listEdgeNode_v;
      } else {
      }
    }
  }
  list<int>* subgraph = NULL;
  {
    int numNodes = 0;
    for (__typeof((listPointers).begin()) lp = ((listPointers).begin());
         lp != (listPointers).end(); ++lp) {
      list<int>* g = *lp;
      if (g->size() > numNodes) {
        numNodes = g->size();
        subgraph = g;
      }
    }
  }
  if (m / 2 <= subgraph->size()) {
    list<int>* oddList = new list<int>();
    list<int>* evenList = new list<int>();
    bool odd = true;
    for (__typeof((*subgraph).begin()) v = ((*subgraph).begin());
         v != (*subgraph).end(); ++v) {
      if (odd)
        oddList->push_back(*v);
      else
        evenList->push_back(*v);
      odd = !odd;
    }
    oddList->splice(oddList->end(), *evenList);
    delete (evenList);
    listPointers.erase(subgraph);
    delete (subgraph);
    subgraph = oddList;
    if (subgraph->size() % 2 == 0) {
      list<int>::iterator ite1, ite2;
      ite1 = ite2 = subgraph->begin();
      ite1++;
      swap(*ite1, *ite2);
    }
  } else {
    listPointers.erase(subgraph);
  }
  list<int>::iterator it = subgraph->begin();
  for (__typeof((listPointers).begin()) listPointerIte =
           ((listPointers).begin());
       listPointerIte != (listPointers).end(); ++listPointerIte) {
    list<int>* listToMergePtr = *listPointerIte;
    for (__typeof((*listToMergePtr).begin()) uIte = ((*listToMergePtr).begin());
         uIte != (*listToMergePtr).end(); ++uIte) {
      if (it == subgraph->end()) it = subgraph->begin();
      subgraph->insert(it++, *uIte);
    }
    delete (listToMergePtr);
  }
  {
    cout << subgraph->back() << " " << subgraph->front() << endl;
    int numPrintedEdges = 1;
    int lastU = subgraph->front();
    subgraph->pop_front();
    for (__typeof((*subgraph).begin()) uIte = ((*subgraph).begin());
         uIte != (*subgraph).end(); ++uIte) {
      if (numPrintedEdges == m) break;
      cout << lastU << " " << *uIte << endl;
      lastU = *uIte;
      numPrintedEdges++;
    }
  }
}
