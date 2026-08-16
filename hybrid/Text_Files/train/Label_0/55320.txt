import java.util.*;
import java.io.*;
import java.math.*;
 
 
import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;
 
public class Main{ 
 
 
    static long mod=1000000007;
    // static int dx[]={1,-1,0,0};
    // static int dy[]={0,0,1,-1};
    // // static int dx[]={1,-1,0,0,1,1,-1,-1};
    // static int dy[]={0,0,1,-1,1,-1,1,-1};
    // PriorityQueue<Integer> que = new PriorityQueue<Integer>(); 
    // HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
    // ArrayList<Integer> lis = new ArrayList<Integer>();
    // ArrayList<Integer> map[]=new ArrayList[26];
    // static HashMap<Integer,Long> map = new HashMap<Integer,Long>();

    public  static void main(String[] args)   throws Exception, IOException{
        Reader sc = new Reader(System.in);
        PrintWriter out=new PrintWriter(System.out);
        // int n=sc.nextInt();
        // long n=sc.nextLong();
        // char c[][] = new char[h][w];
        // long a[] = new long [n];
        // char c[]=sc.nextString().toCharArray();
        // for(int i=0; i<n; i++) {a[i]=sc.nextInt();}
        
        int n = sc.nextInt();
        int m = sc.nextInt();
        Cake a[] = new Cake[n];
        long w[][] = new long[n][3];

        for(int i=0; i<n; i++){
            long x=sc.nextLong();
            long y=sc.nextLong();
            long z=sc.nextLong();
            w[i][0] = x;
            w[i][1] = y;
            w[i][2] = z;
        }

        long ans = 0;
        for(int t=0; t<1<<3; t++){
            int b=t;
            int b1= (b%2==0 )? 1:-1;
            b/=2;
            int b2= (b%2==0 )? 1:-1;
            b/=2;
            int b3= (b%2==0 )? 1:-1;

            for(int i=0; i<n; i++){
                a[i] = new Cake(i,b1*w[i][0] + b2*w[i][1] + b3*w[i][2]);
            }
            sort(a);
            long s=0;
            for(int i=0; i<m; i++){
                s+=a[i].x;
            }
            ans=max(abs(s),ans);
        }

        out.println(ans);
        out.flush();
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

class Cake implements Comparable<Cake>{
    int id;
    long x;
    Cake(int id, long x) {
        this.id=id;
        this.x=x;
    } 
      
    public int compareTo(Cake p){
        return (- x + p.x)>=0 ? 1:-1;//des
    } 
}


class P implements Comparable<P>{
    int x,y;
    P(int x, int y) {
        this.x=x;
        this.y=y;
    } 
      
    public int compareTo(P p){
        return -x + p.x;//des
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