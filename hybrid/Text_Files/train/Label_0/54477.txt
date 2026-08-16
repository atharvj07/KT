
import java.util.*;
import java.io.*;
public class TestClass  {
  
   static InputReader sc = new InputReader(); 
   static ArrayList[] al;
   static boolean[] v;
   static long count=0;
   static long[] val;
   static void dfs(int src){
        
       v[src]=true;
       for(int i=0;i<al[src].size();i++){
          
        
           if(!v[(int)al[src].get(i)])
              {
                count+=val[(int)al[src].get(i)];
                dfs((int)al[src].get(i));
              }
       }
       return;
   }
   
   
    public static void main(String[] args) throws IOException{
         String s=s();
        int k=i();
        long l=Long.parseLong(s);
        int lol=0,ans=0;
        boolean flag=true;
          for(int i=0;i<s.length()-1;i++){
            if(s.charAt(i)!='0'){
               flag=false;
               break;
            }else{
              ans++;
            }
          }
      if(flag==true){
            System.out.println(s.length()-1);
      }else{
      
        if(s.length()<=k){
            System.out.println(s.length()-1);
        }else{
            for(int j=s.length()-1;j>=0;j--){
                if(lol==k){
                  System.out.println(ans);
                  return;
                }
                if(s.charAt(j)=='0'&&j!=0){
                  lol++;
                }else{
                  ans++;
                }


            }
           if(lol!=k){
               System.out.println(s.length()-1);
           } 
            


        }
} 
    }
    /////////////////////////////////////////////////////////// shortcuts //////////////////////////////
       static int i()  {
           
          return sc.nextInt();
        }
        static long l()  {
          return sc.nextLong();

        }
        static double d() throws IOException{
          return sc.nextDouble();
        }
        static String s() throws IOException{
          return sc.next();

        }
        static String sL() throws IOException{
          return sc.nextLine();
        }
       static void loop(int[] a) throws IOException{
          for(int j=0;j<a.length;j++){
              a[j]=i();
          }
        }
        static void eloop(int[] a) throws IOException{
          for(int i=1;i<=a.length;i++){
              a[i]=i();
          }
        }
        static void ploop(int[] a)throws IOException{
             for(int j=0;j<a.length;j++){
                System.out.println(a[j]);
             }

        }
        static void eploop(int[] a)throws IOException{
             for(int j=1;j<=a.length;j++){
                System.out.println(a[j]);
             }

        } 
  
        ////////////////////////////////////////////////////////////////////////////////////////////////////
     

   

  static class InputReader {
        BufferedReader br;
        StringTokenizer st;
 
        public InputReader() {
            br = new BufferedReader(new
                    InputStreamReader(System.in));
        }
 
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                }
                catch (IOException  e) {
                    throw new RuntimeException();
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
 
        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            }
            catch (IOException e) {
                throw new RuntimeException();
            }
            return str;
        }
    }

 }