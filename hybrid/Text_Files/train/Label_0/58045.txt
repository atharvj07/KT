//make sure to make new file!
import java.io.*;
import java.util.*;

public class D68{
   
   public static void main(String[] args)throws IOException{
      BufferedReader f = new BufferedReader(new InputStreamReader(System.in));
      PrintWriter out = new PrintWriter(System.out);
      
      int t = Integer.parseInt(f.readLine());
      
      for(int q = 0; q < t; q++){
      
         StringTokenizer st = new StringTokenizer(f.readLine());
      
         int n = Integer.parseInt(st.nextToken());
         int m = Integer.parseInt(st.nextToken());
         
         if(solve(n,m)){
            out.println("Alice");
         } else {
            out.println("Bob");
         }
      
      }
      
      
      
      
      out.close();
   }
   
   public static boolean solve(int n, int k){
      //if(n==0) return false;
      if(k % 3 == 0){
         return !((n%(k+1)) % 3 == 0 && n%(k+1) != k);
      } else {
         return n%3 != 0;
      }
   }
      
}