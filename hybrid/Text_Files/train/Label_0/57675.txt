//make sure to make new file!
import java.io.*;
import java.util.*;

public class A660{
   
   public static void main(String[] args)throws IOException{
      BufferedReader f = new BufferedReader(new InputStreamReader(System.in));
      PrintWriter out = new PrintWriter(System.out);
      
      int t = Integer.parseInt(f.readLine());
      
      for(int q = 1; q <= t; q++){

         int n = Integer.parseInt(f.readLine());
      
         if(n <= 30){
            out.println("NO");
         } else {
            
               
            out.println("YES");
            if(n == 36 || n == 40 || n==44){
               out.print("6 10 15 ");
               out.println(n-31);
            } else {
               out.print("6 10 14 ");
               out.println(n-30);
            }
         }
      

      }
      
      
      
      
      out.close();
   }
   
      
}