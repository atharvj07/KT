import java.util.*;
import java.math.*;
import java.io.*;

import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;



public class Main{
    
    // ArrayList<Integer> lis = new ArrayList<Integer>();
    // ArrayList<String> lis = new ArrayList<String>();
    // PriorityQueue<P> que = new PriorityQueue<P>();
    // PriorityQueue<Integer> que = new PriorityQueue<Integer>();
    //  Stack<Integer> stack = new Stack<Integer>();
    //HashMap<Long,Long> map = new HashMap<Long,Long>();
    //  static long sum=0;
    // 1000000007 (10^9+7)
    //static int mod = 1000000007;
    static long mod = 1000000007;
    //static int mod = 1000000009; ArrayList<Integer> l[]= new ArrayList[n];
    // static int dx[]={1,-1,0,0};
    // static int dy[]={0,0,1,-1};
    // //static int dx[]={1,-1,0,0,1,1,-1,-1};
    //static int dy[]={0,0,1,-1,1,-1,1,-1};
    
    //static Set<Integer> set = new HashSet<Integer>();
    //static ArrayList<Integer> l[];
    //static int parent[][],depth[],node,max_log;
    //static ArrayList<Integer> l[];
 

public  static void main(String[] args)   throws Exception, IOException{

    //Scanner sc =new Scanner(System.in);
    
    Reader sc = new Reader(System.in);
    PrintWriter out=new PrintWriter(System.out);

    


    int n=sc.nextInt(),m=sc.nextInt();
n++;

    TreeSet <Long> ts=new TreeSet<Long>();
    long mx=n;
    int sf=31,bt=1<<30; bt--;
    
            ts.add(1L);
            ts.add(mx<<sf);

    
    for( int i=0; i<m; i++ ){

        long x=sc.nextInt(), y=sc.nextInt();
        char c=sc.nextString().toCharArray()[0];
        long h=x<<sf,g=0,yy=0,d=0;

        if( x==(ts.ceiling(h)>>sf)  ){ out.println(0); continue; }

        if(c=='U'){
            g=ts.ceiling(h);
            if(g%2==1){ g>>=1; long f=g&bt;  g>>=30; yy=abs(n-g); d=f+(-yy+y);  }
            else { g>>=sf;  yy=abs(n-g);  d=-yy+y+1; }
            g=x<<sf; g+=d<<1; g+=1;
            ts.add(g);
            out.println(d-1);
        }else {
    
            g=ts.floor(h);
            if(g%2==0){ g>>=1; long f=g&bt;  g>>=30;  d=f+(x-g);  }
            else { g>>=sf;   d=x-g+1; }
            g=x<<sf; g+=d<<1; 
            ts.add(g);
            out.println(d-1);
        }
    }

   // out.println();
    out.flush();
//  System.out.println();

}




 static long gcd(long a, long b){
                 if(min(a,b) == 0) return max(a,b);
                 return gcd(max(a, b) % min(a,b), min(a,b));
         }
        


static void db(Object... os){
    System.err.println(Arrays.deepToString(os));

}

static boolean validpos(int x,int y,int r, int c){
    
    return x<r && 0<=x && y<c && 0<=y;
    
}

static boolean bit(long x,int k){
    // weather k-th bit (from right) be one or zero
    return  ( 0 < ( (x>>k) & 1 )  )  ? true:false;
}


}



    

class Reader
{ 
    private BufferedReader x;
    private StringTokenizer st;
    
    public Reader(InputStream in)
    {
        x = new BufferedReader(new InputStreamReader(in));
        st = null;
    }
    public String nextString() throws IOException
    {
        while( st==null || !st.hasMoreTokens() )
            st = new StringTokenizer(x.readLine());
        return st.nextToken();
    }
    public int nextInt() throws IOException
    {
        return Integer.parseInt(nextString());
    }
    public long nextLong() throws IOException
    {
        return Long.parseLong(nextString());
    }
    public double nextDouble() throws IOException
    {
        return Double.parseDouble(nextString());
    }
}

