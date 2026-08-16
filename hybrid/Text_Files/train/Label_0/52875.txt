//make sure to make new file!
import java.io.*;
import java.util.*;

public class C520{

   public static long MOD = 1000000007L;
   
   public static void main(String[] args)throws IOException{
      BufferedReader f = new BufferedReader(new InputStreamReader(System.in));
      PrintWriter out = new PrintWriter(System.out);
      
      
      long[] pow2 = new long[100005];
      pow2[0] = 1L;
      for(int k = 1; k < 100005; k++){
         pow2[k] = (2L*pow2[k-1] + MOD)%MOD;
      }
      
      
      StringTokenizer st = new StringTokenizer(f.readLine());
      
      int n = Integer.parseInt(st.nextToken());
      int m = Integer.parseInt(st.nextToken());
      
      char[] sarray = f.readLine().toCharArray();
      int[] array = new int[n];
      for(int k = 0; k < n; k++){
         if(sarray[k] == '1') array[k] = 1;
         else array[k] = 0;
      }
         
      int[] psum = new int[n+1];
         
      psum[0] = 0;
      for(int k = 1; k <= n; k++){
         psum[k] = psum[k-1] + array[k-1];
      }
         
      for(int k = 0; k < m; k++){
         st = new StringTokenizer(f.readLine());
         int l = Integer.parseInt(st.nextToken());
         int r = Integer.parseInt(st.nextToken());
            
         int b = psum[r] - psum[l-1];
         int a = r-l+1-b;
            
         long answer = ((pow2[b]-1)*pow2[a] + MOD)%MOD;
         out.println(answer);
      }
      
      
      
      
      
      out.close();
   }
   
      
}