import java.io.*;
import java.util.*;
import java.*;
import java.math.BigInteger;

public class zad {
    private static BufferedReader in;
    private static StringTokenizer tok;
    private static PrintWriter out;

    private static String readToken() throws IOException {
        while (tok == null || !tok.hasMoreTokens()) {
            tok = new StringTokenizer(in.readLine());
        }
        return tok.nextToken();
    }
    
    private static int readInt() throws IOException {
        return Integer.parseInt(readToken());
    }
    private static double readDouble() throws IOException {
        return Double.parseDouble(readToken());
    }
    private static long readLong() throws IOException {
        return Long.parseLong(readToken());
    }
     static  int partition (int[] array, int start, int end) {
           int marker = start;
     
           for ( int i = start; i <= end; i++ ) {
               if ( array[i] <= array[end] ) {
                   int temp = array[marker];
     
                   array[marker] = array[i];
                   array[i] = temp;
                   marker += 1;
               }
           }
           return marker - 1;
       }
     
      static void quicksort (int[] array, int start, int end) {
           int pivot;
     
           if ( start >= end ) {
               return;
           }
     
           pivot = partition (array, start, end);
           quicksort (array, start, pivot-1);
           quicksort (array, pivot+1, end);
       }
      
      
      public static void Solve() throws IOException{
      int n=readInt();
      int m = readInt();
      int s = readInt();
      int f = readInt();
      
      char x ='m';
      int p = 0;
      if(s>f) {
          p=-1;
          x='L';
      }
     
      else{
          p=1;
          x='R';
      }
      StringBuilder st= new StringBuilder();
      int en =0;
      int time =0;
      boolean e = false;
      for(int i =0;i<m;i++){
          time++;
          int t=readInt();
          int l= readInt();
          int r = readInt();
          if(e) continue;
          for(;time<t;time++){
              s+=p;
              st.append(x);
              if(s==f){
                  en= time;
                  e = true;
                  break;
              }
              
              
          }
          time =t;
          if (e) continue;
          int need=s+p;
          if (need>=l && need<=r || s>=l && s <=r){
              st.append('X');
          }else{
              st.append(x);
              s=need;
              if(s==f){
                  en= time;
                  e = true;
                  break;
              }
          }
          
      }
      while(s!=f){
          st.append(x);
          s+=p;
      }
      out.println(st);
      
          
          
          
          
      }
    

    public static void main(String[] args) throws IOException {
        in = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(System.out);
        
        
        
        Solve();
        
       
        in.close();
        out.close();
    }
}