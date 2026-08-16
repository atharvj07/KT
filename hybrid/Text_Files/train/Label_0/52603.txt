/*
If you want to aim high, aim high
Don't let that studying and grades consume you
Just live life young
******************************
If I'm the sun, you're the moon
Because when I go up, you go down
*******************************
I'm working for the day I will surpass you
https://www.a2oj.com/Ladder16.html
*/
import java.util.*;
import java.io.*;
import java.math.*;

   public class x1141F
   {
      public static void main(String omkar[]) throws Exception
      {
         BufferedReader infile = new BufferedReader(new InputStreamReader(System.in));  
         StringTokenizer st = new StringTokenizer(infile.readLine());
         int N = Integer.parseInt(st.nextToken());
         int[] arr = new int[N];
         st = new StringTokenizer(infile.readLine());
         for(int i=0; i < N; i++)
            arr[i] = Integer.parseInt(st.nextToken());
         HashMap<Long, ArrayList<Integer>> map = new HashMap<Long, ArrayList<Integer>>();
         for(int r=0; r < N; r++)
         {
            long sum = 0L;
            for(int i=r; i >= 0; i--)
            {
               sum += arr[i];
               if(!map.containsKey(sum))
                  map.put(sum, new ArrayList<Integer>());
               map.get(sum).add(i);
               map.get(sum).add(r);
            }
         }
         ArrayList<Integer> res = new ArrayList<Integer>();
         for(long key: map.keySet())
         {
            ArrayList<Integer> ls = map.get(key);
            ArrayList<Integer> temp = new ArrayList<Integer>();
            temp.add(ls.get(0));
            temp.add(ls.get(1));
            int r = ls.get(1);
            for(int i=2; i < ls.size(); i+=2)
               if(r < ls.get(i))
               {
                  r = ls.get(i+1);
                  temp.add(ls.get(i));
                  temp.add(ls.get(i+1));
               }
            if(res.size() < temp.size())
               res = temp;
         }
         System.out.println(res.size()/2);
         StringBuilder sb = new StringBuilder();
         for(int i=0; i < res.size(); i+=2)
         {
            sb.append((1+res.get(i))+" "+(1+res.get(i+1)));
            sb.append("\n");
         }
         System.out.print(sb);
      }
   }