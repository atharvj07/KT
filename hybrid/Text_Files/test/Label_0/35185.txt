/*
If you want to aim high, aim high
Don't let that studying and grades consume you
Just live life young
******************************
What do you think? What do you think?
1st on Billboard, what do you think of it
Next is a Grammy, what do you think of it
However you think, I’m sorry, but shit, I have no fucking interest
*******************************
Higher, higher, even higher, to the point you won’t even be able to see me
https://www.a2oj.com/Ladder16.html
*******************************
NEVER DO 300IQ CONTESTS EVER
300IQ AS WRITER = EXTRA NONO
*/
import java.util.*;
import java.io.*;
import java.math.*;

   public class x1271E
   {
      public static void main(String omkar[]) throws Exception
      {
         BufferedReader infile = new BufferedReader(new InputStreamReader(System.in));  
         StringTokenizer st = new StringTokenizer(infile.readLine());
         N = Long.parseLong(st.nextToken());
         long K = Long.parseLong(st.nextToken());
         if(N == 1)
         {
            System.out.println(1);
            return;
         }
         //fill out tree
         long max = 0L; int b = 0;
         for(b=0; b < 60 && max < N; b++)
            max += (1L << b);
         bottom = b;
         //evens
         long low = 1;
         long high = N/2;
         while(low != high)
         {
            long mid = (low+high+1)/2;
            if(find(2*mid)+find(2*mid+1) >= K)
               low = mid;
            else
               high = mid-1;
         }
         long res = 1L;
         if(find(2*low)+find(2*low+1) >= K)
            res = 2*low;
         low = 0;
         high = N/2;
         if(N%2 == 0)
            high--;
         while(low != high)
         {
            long mid = (low+high+1)/2;
            if(find(2*mid+1) >= K)
               low = mid;
            else
               high = mid-1;
         }
         res = Math.max(res, 2*low+1);
         System.out.println(res);
      }
      static long N;
      static int bottom;
      public static long find(long x)
      {
         int level = 0;
         for(int b=59; b >= 0; b--)
            if((x&(1L<<b)) > 0)
            {
               level = b+1;
               break;
            }
         long res = 0L;
         int delta = bottom-level;
         for(int i=0; i <= delta; i++)
            res += (1L << i);
         long left = x;
         long right = x;
         for(int i=0; i < delta; i++)
         {
            left <<= 1;
            right <<= 1;
            right++;
         }
         if(left > N)
            res -= (1L << delta);
         else if(right > N)
            res -= right-N;
         return res;
      }
   }