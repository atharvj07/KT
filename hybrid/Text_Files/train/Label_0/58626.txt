import java.util.*;

class State implements Comparable<State>{
  int value;
  int cost;

  State(int value, int cost){
    this.value = value;
    this.cost = cost;
  }

  public int compareTo(State st){
    return this.cost - st.cost;
  }
}

public class Main{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);

    while(sc.hasNextInt()){
      int n = sc.nextInt();
      int[][] c = new int[n + 1][n + 1];

      for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
          c[i][j] = sc.nextInt();
        }
      }

      int mask = 1;
      int firstValue = 0;

      for(int i = 1; i <= n; i++){
        firstValue *= 10;
        firstValue += i;

        if(i != 1){
          mask *= 10;
        }
      }

      PriorityQueue<State> open = new PriorityQueue<State>();
      open.add(new State(firstValue, 0));
      boolean[] closed = new boolean[10000000];
      int maxCost = -1;

      while(!open.isEmpty()){
        State st = open.poll();

        if(closed[st.value % mask]){
          continue;
        }
        closed[st.value % mask] = true;

        maxCost = Math.max(maxCost, st.cost);

        for(int i = 0; i < n; i++){
          for(int j = i + 1; j < n; j++){
            StringBuilder valueStr = new StringBuilder(Integer.toString(st.value));
            int a = valueStr.charAt(i) - '0';
            int b = valueStr.charAt(j) - '0';

            valueStr.setCharAt(i, (char)(b + '0'));
            valueStr.setCharAt(j, (char)(a + '0'));

            open.add(new State(Integer.parseInt(valueStr.toString()), st.cost + c[a][b]));
          }
        }
      }

      System.out.println(maxCost);
    }
  }
}