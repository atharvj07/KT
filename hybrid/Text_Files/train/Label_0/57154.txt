/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
public class Ideone
{
    public static void main (String[] args) throws java.lang.Exception
    {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int counter = 0;
        if(a==b){
            System.out.println("infinity");
        }
        else{
            for(int x = 1;x*x<=(a-b);x++){
                if((a-b)%x==0){
                    if(x*x==(a-b)){
                        if(x>b){
                        counter++;
                        }
                    }
                    else{
                        if(x>b){
                            counter++;
                        }
                        if((a-b)/x>b){
                            counter++;
                        }
                    }
                }
            }
            System.out.println(counter);
        }
        
    }
}