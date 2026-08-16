import java.io.*;
import java.util.*;
public class B {
    
    public static int countBitFlips(int n,char[] arr){
        int r=0;
        int l=n-1;
        int ans=0;
        while(r<l){
            // out.println("hetetefte "+r+" "+l);
            if(arr[l]!=arr[r]){
                ans++;
            }
            l--;
            r++;

        }        

    return ans;
    }
    
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        FastScanner sc = new FastScanner();
        out = new PrintWriter(new BufferedOutputStream(System.out));
        
        int t=sc.nextInt();
        while(t-->0) {
            int n=sc.nextInt();
            String sr=sc.next();
            char[] arr=sr.toCharArray();
            int ans=countBitFlips(n,arr);
            // out.println("here "+ans);
            int zero_count=0;
            for(int i=0;i<n;i++){
               if(arr[i]=='0'){
                   zero_count++;
               } 

            }
            if(ans==0){
                if(zero_count==0){
                    out.println("DRAW");

                }
                else if(arr[n/2]=='0'&& n%2!=0 && zero_count>1){
                    out.println("ALICE");
                }
                else{
                    out.println("BOB");
                }
            }else{
                // int curr=zero_count-ans;
                if(n%2!=0 && arr[n/2]=='0' && zero_count==2){
                    out.println("DRAW");

                }
                else{
                    out.println("ALICE");
                }
            }

            

            // out.println(count);
            
            
        }
        out.close();
    }


    


    public static PrintWriter out;
         
       public static class FastScanner {
          BufferedReader br;
          StringTokenizer st;
    
          public FastScanner() {
             br = new BufferedReader(new InputStreamReader(System.in));
          }
    
          String next() {
              while (st == null || !st.hasMoreElements()) {
                  try {
                      st = new StringTokenizer(br.readLine());
                  } catch (IOException e) {
                      e.printStackTrace();
                  }
              }
              return st.nextToken();
          }
    
          int nextInt() {
              return Integer.parseInt(next());
          }
    
          long nextLong() {
              return Long.parseLong(next());
          }
    
          double nextDouble() {
              return Double.parseDouble(next());
          }
    
          String nextLine(){
              String str = "";
          try {
             str = br.readLine();
          } catch (IOException e) {
             e.printStackTrace();
          }
          return str;
          }

       }
}
