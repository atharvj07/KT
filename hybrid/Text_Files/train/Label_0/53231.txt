import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;


 public   class ex{
   
       
    public static void main(String[] args) throws IOException {
        Scanner sc=new Scanner(System.in);
     String s=new String();
        s=sc.next();
        char c[]=s.toCharArray();
        int n=c.length;
        int A[]=new int[n];
        for(int i=0;i<n-1;i++){
            if(c[i]=='b' && c[i+1]=='a'){
                A[i]=1;
            }
            else if(c[i]=='a' && c[i+1]=='b'){
                A[i]=1;
            }
        }
        if(c[n-1]=='a'){
            A[n-1]=1;
        }
       for(int i=0;i<n;i++){
           System.out.print(A[i] + " ");
       }
    }
}
