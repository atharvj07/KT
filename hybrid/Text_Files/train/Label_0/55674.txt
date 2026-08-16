//make sure to make new file!
import java.io.*;
import java.util.*;

public class C675{
   
   public static long MOD = 1000000007L;
   public static long[] fac;
   public static long[] ifac;
   public static long i2;
   public static int MAX = 100005;
   
   public static void main(String[] args)throws IOException{
      BufferedReader f = new BufferedReader(new InputStreamReader(System.in));
      PrintWriter out = new PrintWriter(System.out);
      /*
      fac = new long[MAX];
      ifac = new long[MAX];
      fac[0] = 1L;
      for(int k = 1; k < MAX; k++){
         fac[k] = (fac[k-1]*(long)k + MOD)%MOD;
      }
      for(int k = 0; k < MAX; k++){
         ifac[k] = modInverse(fac[k],MOD);
      }*/
      
      long[] pow10 = new long[MAX];
      pow10[0] = 1L;
      for(int k = 1; k < MAX; k++){
         pow10[k] = (pow10[k-1]*10L + MOD)%MOD;
      }
      
      long i81 = modInverse(81L,MOD);
      i2 = modInverse(2L,MOD);
      
      char[] chs = f.readLine().toCharArray();
      int n = chs.length;
      long[] array = new long[n];
      for(int k = 0; k < n; k++){
         array[k] = (long)Character.getNumericValue(chs[k]);
      }
      
      long answer = 0L;
      for(int k = 0; k < n; k++){
         long addfront = (array[k]*c2((long)(k+1)) + MOD)%MOD;
         addfront = (addfront*pow10[n-k-1] + MOD)%MOD;
         long addback = (9L*pow10[n-k-1]*(long)(n-k-1) + MOD)%MOD;
         addback = (addback - pow10[n-k-1] + 1L + MOD)%MOD;
         addback = (addback * array[k] + MOD)%MOD;
         addback = (addback * i81 + MOD)%MOD;
         answer = (answer + addfront + addback + MOD)%MOD;
         //out.println(k + " " + addfront + " " + addback);
      }
      
      out.println(answer);
         
      
      
      
      
      
      
      
      
      out.close();
   }
   
   public static long c2(long x){
      if(x < 2) return 0L;
      long prod = (x*(x-1L) + MOD)%MOD;
      return (prod*i2 + MOD)%MOD;
   }
   
   public static long choose(int n, int r){
      if(n < r) return 0L;
      long prod = (fac[n] * ifac[n-r] + MOD)%MOD;
      return (prod * ifac[r] + MOD)%MOD;
   }
   
   //from geeksforgeeks
   public static long modInverse(long a, long m) 
   { 
       long m0 = m; 
       long y = 0, x = 1; 
     
       if (m == 1L) 
         return 0L; 
     
       while (a > 1) 
       { 
           // q is quotient 
           long q = a / m; 
           long t = m; 
     
           // m is remainder now, process same as 
           // Euclid's algo 
           m = a % m;
           a = t; 
           t = y; 
     
           // Update y and x 
           y = x - q * y; 
           x = t; 
       } 
     
       // Make x positive 
       if (x < 0) 
          x += m0; 
     
       return x; 
   } 

      
}