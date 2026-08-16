
import java.io.BufferedInputStream;
import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author AL_DEEB
 */
public class two_button {
     public static void main(String[] args) {
		StringBuilder sb = new StringBuilder();
		        BufferedInputStream bs = new BufferedInputStream(System.in);
		Scanner sc = new Scanner(bs);
                
                int n=sc.nextInt();
                int m=sc.nextInt();
                
                int num=0;
            
             
                    
                    while(true)
                    {
                        if(n>=m)
                        {
                        num+=n-m;
                        break;
                        }
                        else
                        {
                            if(m%2==0)
                                m=m/2;
                            else
                                m++;
                         num++;
                            
                            
                        }
                        
                        
                    }
                    System.out.println(num);
              
                
                
                
     }
}
