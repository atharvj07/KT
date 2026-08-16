import java.util.*;
import java.io.*;

public class HelloWorld{

     public static void main(String []args){
  
       Scanner sc = new Scanner (System.in);
       int n = sc.nextInt();
       int []A = new int[n];
       int []B= new int[n];
       String s = sc.next();
       
       for(int i = 0; i < n; i++){
           A[i] = s.charAt(i)-'0';
       }
       int k = 0;
       for(int i = n; i < n*2; i++){
           B[k] = s.charAt(i)-'0';
           k++;
       }
       
       Arrays.sort(A);Arrays.sort(B);
       int count = 0;
       int count1 = 0;
       
       for(int i = 0; i < n; i++){
           if(A[i] > B[i])count++;
           if(B[i] > A[i])count1++;
           }
      
        if(count == n || count1 == n){
            System.out.println("YES");
        }else{
            System.out.println("NO");
        }
     }
}