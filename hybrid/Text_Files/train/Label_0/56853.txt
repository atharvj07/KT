
import java.util.Scanner;

/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Xeyyam
 */
public class Main {
   
    
   static boolean[][] flag = new boolean[100][100];
   static String s[] = new String[101];
   static int n ,  m;
    
   
   
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
                
        n = sc.nextInt();
        m = sc.nextInt();
        
        
        for( int i = 0 ; i<n ; i++ )
            s[i] = sc.next();
        
        
        
        for( int i = 0 ; i<n ; i++  )
        {
            for( int j = 0 ; j<m ; j++ )
            {
                if( !flag[i][j] )
                    check(  i , j );
            }
        }
        
        
        
        String ans = "";
        
        for( int i = 0 ; i<n ; i++  )
        {
            for( int j = 0 ; j<m ; j++ )
            {
                if( !flag[i][j] )
                    ans = ans  + s[i].charAt(j);
            }
        }
        
        System.out.println(ans);
        
        
        
        
        
    }
    
    
    
   static void check( int i , int j )
   {
       for( int k = 0 ; k < m  ; k++ )
           if( k != j && s[i].charAt(j)==s[i].charAt(k) )
           {
               flag[i][j] = true;
               flag[i][k] = true;
           }
       
       for( int k = 0 ; k < n ; k++ )
           if( k != i && s[i].charAt(j)==s[k].charAt(j) )
           {
               flag[i][j] = true;
               flag[k][j] = true;
           }
      
       
   }
    
    
    
}
