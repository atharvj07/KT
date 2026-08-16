/*
If you want to aim high, aim high
Don't let that studying and grades consume you
Just live life young
******************************
What do you think? What do you think?
1st on Billboard, what do you think of it
Next is a Grammy, what do you think of it
However you think, I’m sorry, but shit, I have no fcking interest
*******************************
I'm standing on top of my Monopoly board
That means I'm on top of my game and it don't stop
til my hip don't hop anymore
https://www.a2oj.com/Ladder16.html
*******************************
300iq as writer = Sad!
*/
import java.util.*;
import java.io.*;
import java.math.*;

   public class x1394B
   {
      public static void main(String hi[]) throws Exception
      {
         BufferedReader infile = new BufferedReader(new InputStreamReader(System.in));
         StringTokenizer st = new StringTokenizer(infile.readLine());
         int N = Integer.parseInt(st.nextToken());
         int M = Integer.parseInt(st.nextToken());
         K = Integer.parseInt(st.nextToken());
         ArrayList<Edge>[] edges = new ArrayList[N+1];
         for(int i=1; i <= N; i++)
            edges[i] = new ArrayList<Edge>();
         for(int i=0; i < M; i++)
         {
            st = new StringTokenizer(infile.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            edges[a].add(new Edge(b, c));
         }
         for(int i=1; i <= N; i++)
            Collections.sort(edges[i]);
         //xorshing trick
         long[] vals = new long[N+1];
         long target = 0L;
         for(int i=1; i <= N; i++)
         {
            vals[i] = (long)(Math.random()*Long.MAX_VALUE);
            target ^= vals[i];
         }
         hash = new long[K+1][K+1];
         for(int v=1; v <= N; v++)
         {
            int deg = edges[v].size();
            int tag = 1;
            for(Edge e: edges[v])
               hash[deg][tag++] ^= vals[e.to];
         }
         res = 0;
         recur(0L, target, 1);
         System.out.println(res);
      }
      static long[][] hash;
      static int K;
      static int res;
      public static void recur(long currhash, long target, int i)
      {
         if(i > K && currhash == target)
            res++;
         else if(i <= K)
         {
            for(int j=1; j <= i; j++)
               recur(currhash^hash[i][j], target, i+1);
         }
      }
   }
   class Edge implements Comparable<Edge>
   {
      public int to;
      public int weight;
      
      public Edge(int a, int b)
      {
         to = a;
         weight = b;
      }
      public int compareTo(Edge oth)
      {
         return weight-oth.weight;
      }
   }