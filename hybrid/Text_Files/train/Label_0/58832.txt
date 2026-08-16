import java.io.BufferedReader; 
import java.io.IOException; 
import java.io.InputStreamReader; 
import java.util.*; 
import java.util.StringTokenizer; 
 
public class Main
{
 final static int n=5000000;
 static boolean b[]=new boolean[n+2];
// static int f[]=new int[n+2];
  //static int p[]=new int[n+2];
    static class FastReader 
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
 static  FastReader sc=new FastReader();
    public static void main(String[] args) 
    { 
  int n=i();
 Long d=l();
 Long prev=l();
Long min_move=0L,x=0L;
 for(int i=1;i<n;i++)
 {
     Long curr=l();
     if(curr>prev) prev=curr;
     
     else if(prev>=curr){
         Long diff=prev-curr;
         x=diff/d;
         x++;
        min_move+=x;
         
         prev=curr+(x*d);
        
 }
 }
    
 System.out.println(min_move);
        
       

           
         
         
      
    }
        public static int i()
        {
            int s=sc.nextInt();
            return s;
        }
        public static Long l()
        {
            Long k=sc.nextLong();
            return k;
        }
        
      public static int [] input(int n)
      {
          int a[]=new int[n];
          for(int i=0;i<n;i++) a[i]=sc.nextInt();
          return a;
      }
        public static Long [] inpuut(int n)
      {
          Long a[]=new Long[n];
          for(int i=0;i<n;i++) a[i]=sc.nextLong();
          return a;
      }
      public static  int sum(int a[],int n){
          int s=0;
      for(int i=0;i<n;i++) s+=a[i];
      return s;
      }
        public static void sieve()
        {
            
     for(int i=2;i<=n;i++)
     {
         if(!b[i])
         {
             for(int j=i*i;j<=n;j+=i)
             b[j]=true;
         }
     }
              
    }} 