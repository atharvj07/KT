import java.util.Scanner;
import java.util.ArrayList;

class ProblemB{
  ArrayList<ArrayList<Integer>> g = new ArrayList<ArrayList<Integer>>();//graph
  ArrayList<ArrayList<Integer>> rg = new ArrayList<ArrayList<Integer>>();//greverse graph
  ArrayList<Integer> vs = new ArrayList<Integer>();
  boolean visited[] = null;
  int cmp[] = null;

  void solve(){
    Scanner scan = new Scanner(System.in);
    int v = scan.nextInt();
    int e = scan.nextInt();

    visited = new boolean[v];
    cmp = new int[v];

    for(int i=0 ; i<v ; ++i){
      g.add(new ArrayList<Integer>());
      rg.add(new ArrayList<Integer>());
    }

    int s=-1, t=-1;
    for(int i=0 ; i<e ; ++i){
      s = scan.nextInt();
      t = scan.nextInt();
      g.get(s).add(t);
      rg.get(t).add(s);
    }

    if(scc(v)<v) System.out.println("1");
    else System.out.println("0");

  }

  void dfs(int v){
    visited[v] = true;
    for(int i=0 ; i<g.get(v).size() ; ++i){
      if(!visited[g.get(v).get(i)]) dfs(g.get(v).get(i));
    }
    vs.add(v);
  }

  void rdfs(int i, int k){
    visited[i] = true;
    cmp[i] = k;
    for(int j=0 ; j<rg.get(i).size() ; ++j){
      if(!visited[rg.get(i).get(j)]) rdfs(rg.get(i).get(j), k);
    }
  }

  int scc(int v){
    visitedClear();
    vs.clear();

    for(int i=0 ; i<v ; ++i){
      if(!visited[i]) dfs(i);
    }

    visitedClear();
    int k = 0;
    for(int i = vs.size()-1 ; i>=0 ; --i){
      if(!visited[vs.get(i)]) rdfs(vs.get(i), ++k);
    }
    return k;
  }

  void visitedClear(){
    for(int i=0 ; i<visited.length ; ++i) visited[i] = false;
  }
}

public class Main{
  public static void main(String[] args){
    new ProblemB().solve();
  }
}

