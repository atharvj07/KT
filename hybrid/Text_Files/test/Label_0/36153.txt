//make sure to make new file!
import java.io.*;
import java.util.*;

public class E669{
   
   public static void main(String[] args)throws IOException{
      BufferedReader f = new BufferedReader(new InputStreamReader(System.in));
      PrintWriter out = new PrintWriter(System.out);
      
      StringTokenizer st = new StringTokenizer(f.readLine());
      
      int n = Integer.parseInt(st.nextToken());
      int m = Integer.parseInt(st.nextToken());
      
      ArrayList<ArrayList<Edge>> adj = new ArrayList<ArrayList<Edge>>(n+1);
      for(int k = 0; k <= n; k++) adj.add(new ArrayList<Edge>());
      
      for(int k = 0; k < m; k++){
         st = new StringTokenizer(f.readLine());
      
         int a = Integer.parseInt(st.nextToken());
         int b = Integer.parseInt(st.nextToken());
         int i = Integer.parseInt(st.nextToken());
         if(a == b) continue;
         adj.get(b).add(new Edge(a,i));                        //put the edge in backwards
      }
      
      int[] answer = new int[n+1];
      Arrays.fill(answer,-1);
      
      int[] dists = new int[n+1];
      Arrays.fill(dists,Integer.MAX_VALUE);
      
      
      Queue<Integer> q = new LinkedList<Integer>();
      HashSet<Integer> seen = new HashSet<Integer>();
      q.add(n);
      seen.add(n);
      dists[n] = 0;
      
      while(!q.isEmpty()){
         int v = q.poll();
         
         for(Edge e : adj.get(v)){
            if(answer[e.to] ==  e.i){
               if(dists[e.to] > dists[v]+1){
                  q.add(e.to);
                  dists[e.to] = dists[v]+1;
               }
            } else if(answer[e.to] == -1){
               answer[e.to] = 1-e.i;
            }
         }
      }
      
      if(dists[1] == Integer.MAX_VALUE){
         out.println(-1);
      } else {
         out.println(dists[1]);
      }
      
      StringJoiner sj = new StringJoiner("");
      for(int k = 1; k <= n; k++){
         if(answer[k] == -1){
            sj.add("0");
         } else {
            sj.add("" + answer[k]);
         }
      }
      
      out.println(sj.toString());
      
      
      
      
      
      
      
      
      out.close();
   }
   
   public static class Edge{
      int to;
      int i;
      
      public Edge(int a, int b){
         to = a;
         i = b;
      }
   }
      
}