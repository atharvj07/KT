
//package javaapplication3;





import java.util.Scanner;
import java.util.Arrays;

/**
 *
 * @author Mahmoud
 */
public class StringCodeforces {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
             

        Scanner sc=new Scanner(System.in);
        
        byte x=sc.nextByte();
        
        for(int i=0;i<x;i++)
        {
            char []a=sc.next().toCharArray();
           
            Arrays.sort(a);
              
           if(a[0] != a[a.length-1]){
               for(char w :a)System.out.print(w);
                System.out.println();
           }
           
           else
           {
                System.out.println(-1);
           }
          
        }
            
        
        
        
         
}


}
      
      
       
   
      
       
       
      
        
        
    
    

