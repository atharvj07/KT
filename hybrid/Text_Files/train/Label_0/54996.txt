import java.util.*;
import java.io.*;

public class Main {

  public static void main (String[] args) {

    Scanner sc = new Scanner(System.in);

    int N = Integer.parseInt(sc.next());
    int M = Integer.parseInt(sc.next());
    int[][] p = new int[M][3];

    for (int i = 0; i < M; i++) {
      p[i][0] = i;
      p[i][1] = Integer.parseInt(sc.next());
      p[i][2] = Integer.parseInt(sc.next());
    }

    sc.close();

    Arrays.sort(p, (o1, o2) -> o1[1] == o2[1] ? o1[2] - o2[2] : o1[1] - o2[1]);

    Map<Integer, Integer[]> map = new HashMap<>();

    int now = 0;
    int count = 1;

    for (int i = 0; i < M; i++) {
      if(now == p[i][1]){
        count++;
      } else {
        now = p[i][1];
        count = 1;
      }
      Integer[] c = {p[i][1], count};
      map.put(p[i][0],c);
    }

    PrintWriter out = new PrintWriter(System.out);
    
    for (int i = 0; i < M; i++) {
      Integer[] r = map.get(i);
      out.println(String.format("%06d%06d", r[0], r[1]));
    }
    
    out.flush();

  }

}