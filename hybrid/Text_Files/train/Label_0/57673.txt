import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
 
 public class hello2
 {static class FastReader 
       { 
           BufferedReader br; 
           StringTokenizer st; 
     
           public FastReader() 
           { 
               br = new BufferedReader(new
                        InputStreamReader(System.in)); 
           } 
     
           String next() 
           { 
               while (st == null || !st.hasMoreElements()) 
               { 
                   try
                   { 
                       st = new StringTokenizer(br.readLine()); 
                   } 
                   catch (IOException  e) 
                   { 
                       e.printStackTrace(); 
                   } 
               } 
               return st.nextToken(); 
           } 
     
           int nextInt() 
           { 
               return Integer.parseInt(next()); 
           } 
     
           long nextLong() 
           { 
               return Long.parseLong(next()); 
           } 
     
           double nextDouble() 
           { 
               return Double.parseDouble(next()); 
           } 
     
           String nextLine() 
           { 
               String str = ""; 
               try
               { 
                   str = br.readLine(); 
               } 
               catch (IOException e) 
               { 
                   e.printStackTrace(); 
               } 
               return str; 
           } 
         
       }
    public static void main(String[] args) 
    { 
       FastReader sc =new FastReader();
    int q=sc.nextInt();
       int x=sc.nextInt();
        int[] a=new int[x];
        int c=0;
            for(int i=0;i<q;i++)
           {
                  
                 a[sc.nextInt()%x]++;
                 while(true)
            {
                if(a[c%x]<=0) break;
                else
                {
                    a[c%x]--;
                    c++;
                }
            }
            System.out.println(c);
                 
           }
           
           
            
    
 }
 }