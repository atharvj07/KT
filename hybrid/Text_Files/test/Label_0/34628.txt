import java.util.*;
import java.math.BigInteger; 
public class asd
{
         static Scanner s=new Scanner(System.in);
         static String str=" ";
         static ArrayList<Integer>[] list=new ArrayList[26];
         public static void main(String args[])
         {
             
             int t=1;
             
                  while(t-->0)
                  {
                           solve();
                          
                  }
                  
         }
         public static void solve( )
         {
             int m=s.nextInt();
             int n=s.nextInt();
             BigInteger f = new BigInteger("2");
             for (int i = 2; i <= m+n; i++) 
            f = f.multiply(BigInteger.valueOf(2)); 
            
             System.out.println(f.mod(BigInteger.valueOf(998244353 )));
                
         }
}