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
Shining through the city with a little funk and soul
*******************************
300iq as writer = Sad!
*/
import java.util.*;
import java.io.*;
import java.math.*;

   public class x1194F
   {
      static long MOD = 1000000007L;
      public static void main(String hi[]) throws Exception
      {
         long inv2 = power(2, MOD-2, MOD);
         fac = new long[200001];
         invfac = new long[200001];
         fac[0] = invfac[0] = 1L;
         for(int i=1; i <= 200000; i++)
            fac[i] = (fac[i-1]*i)%MOD;
         invfac[200000] = power(fac[200000], MOD-2, MOD);
         for(int i=199999; i >= 1; i--)
            invfac[i] = (invfac[i+1]*(i+1))%MOD;
         BufferedReader infile = new BufferedReader(new InputStreamReader(System.in));
         StringTokenizer st = new StringTokenizer(infile.readLine());
         int N = Integer.parseInt(st.nextToken());
         long T = Long.parseLong(st.nextToken());
         int[] arr = new int[N];
         st = new StringTokenizer(infile.readLine());
         for(int i=0; i < N; i++)
            arr[i] = Integer.parseInt(st.nextToken())+1;
         long res = 0L;
         long sum = 0L;
         long denom = 1L;
         int dex = 0;
         while(dex < N && sum+arr[dex] <= T)
         {
            sum += arr[dex++];
            denom = (denom*inv2)%MOD;
         }
         for(int ones=0; ones <= dex; ones++)
         {
            long temp = (comb(dex, ones)*denom)%MOD;
            long addend = (temp*dex)%MOD;
            if(dex < N && sum+arr[dex]-1 == T)
               addend = (addend*inv2)%MOD;
            res += addend;
            if(res >= MOD)
               res -= MOD;
            sum--;
            if(dex < N && sum+arr[dex] <= T)
            {
               sum += arr[dex++];
               denom = (denom*inv2)%MOD;
            }
         }
         System.out.println(res%MOD);
      }
      static long[] fac, invfac;
      public static long comb(int a, int b)
      {
         long res = (fac[a]*invfac[b])%MOD;
         return (res*invfac[a-b])%MOD;
      }
      public static long power(long x, long y, long p) 
      { 
         //0^0 = 1
         long res = 1L;      
         x = x%p;  
         while(y > 0) 
         { 
            if((y&1)==1) 
               res = (res*x)%p;
            y >>= 1;
            x = (x*x)%p;  
         } 
         return res; 
      } 
   }