/**
 *   Author: Ridam Nagar
 *   Date: 04 February 2019
 *   Time: 12:59:59
**/
/* 
package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
public class Codechef
{

      
    public static void main (String[] args) throws java.lang.Exception
    {
       Scanner sc=new Scanner(System.in);
       long n=sc.nextLong();
       long a=sc.nextLong();
       long b=sc.nextLong();
       long x=Math.abs(a-1)+Math.abs(b-1);
       long y=Math.abs(n-a)+Math.abs(n-b);
       if(x<=y){
        System.out.println("White");
       }else{
        System.out.println("Black");
       }


 }
}
