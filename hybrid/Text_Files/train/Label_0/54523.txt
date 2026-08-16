import java.util.*;
import java.io.*;
public class lp{ 
static PrintWriter out = new PrintWriter(System.out);
static int mod =1000000007;
static int max = 1000000000;
static int fun(int a[],int n,int x){

int min = 0;

 for(int i=0;i<n;i++){
     if(a[i]==-1){
        if((i-1)>=0&&a[i-1]!=-1&&abs(a[i-1]-x)>min)
              min = abs(a[i-1]-x);
        if((i+1)<n&&a[i+1]!=-1&&abs(a[i+1]-x)>min)
              min = abs(a[i+1]-x);
    }
   else{
          if((i-1)>=0&&a[i-1]!=-1&&abs(a[i-1]-a[i])>min)
              min = abs(a[i-1]-a[i]);
        if((i+1)<n&&a[i+1]!=-1&&abs(a[i+1]-a[i])>min)
              min = abs(a[i+1]-a[i]);
    }
 }
      return min;
}
static int fun1(Integer a[],int n,int x){

int min = 0;

 for(int i=0;i<n;i++)
      min = Math.max(min,abs(a[i]-x));   
      return min;
}
public static void main(String[] args){
   
    int t =ni();
for(int o=1;o<=t;o++){
    long n = nl();
    long m = nl();
    if(m==0)
       { out.println("0"); continue;}
    long rem = n-m;
   long tot = (n*(n+1))/2;
   long ans=0;
    if(rem<=(m+1))
       ans = rem;
    else{
          long x = rem/(m+1);
          long md = rem%(m+1); // x+1
          long md1 = m+1-md;    // x;
          ans = ((x*(x+1))/2)*md1 + (((x+1)*(x+2))/2)*md; 
   }
   ans = tot-ans;
     out.println(ans);
}

                out.flush();
}
static int abs(int x){
  if(x<0) x=-x;
   return x;

}
static long gcd(long a,long b){

            if(b%a==0)
                 return a;
                 return gcd(b%a,a);
} 
static long min(long a,long b){
 
         return Math.min(a,b);
}
static long max(long a,long b){

         return Math.max(a,b);
}
static long pow(long a,long b,long md){

          long ans =1;
           while(b>0){
                if(b%2==1)
                   ans=(ans*a)%md;
                   a=(a*a)%md;
                   b=b/2;
           }
        return ans;
}
static FastReader sc=new FastReader(); 
 
      static int ni(){
                 int x = sc.nextInt();
                 return(x);
        }
      static long nl(){
              long x = sc.nextLong();
              return(x);
         }
      static String n(){
                 String str = sc.next();
                     return(str);
       }
     static String ns(){
                 String str = sc.nextLine();
                   return(str);
      }
     static double nd(){
               double d = sc.nextDouble();
                 return(d);
       }
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
}