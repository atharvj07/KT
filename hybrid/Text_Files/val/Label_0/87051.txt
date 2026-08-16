import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.List;
 import java.util.*;
 public class realfast implements Runnable 
  {
    private static final int INF = (int) 1e9;
    long in= 998244353;
    long fac[]= new long[3000];
    public  void solve() throws IOException 
    {
      

      
           int n = readInt();
           Random rd = new Random();
           long hash[]=new long[n+1];

           for(int i=1;i<=n;i++)
            hash[i]= rd.nextLong();

           int arr[]=new int[n+1];
           
           for(int i=1;i<=n;i++){
            arr[i]= readInt();
           
           }
           
          HashMap<Long,Integer> map =new HashMap<>();
          map.put((long)0,1);
          Queue<Integer> l[] =new Queue[n+1];

          for(int i=1;i<=n;i++)
            l[i]=new LinkedList<Integer>(); 

          
          long cal[]=new long[n+1];
          int start=0;
          int last=-1;
          int count[]=new int[n+1];
          long ans=0;
         // out.println(map.get((long)0));
          for(int i=1;i<=n;i++)
          {
             //l[arr[i]].add(i);
             
             if(l[arr[i]].size()>=3)
             {
                int p= l[arr[i]].poll();
                last=Math.max(last,p);
             }
             
             while(start<last)
             {
                int kl = map.get(cal[start]);
               // out.println(start+" "+kl);
                map.put(cal[start],kl-1);
                start++;
             }
             int before = count[arr[i]];

             count[arr[i]]= (count[arr[i]]+1)%3;
             cal[i]= cal[i-1]+ (count[arr[i]]-before)*hash[arr[i]];
             int pal=0;
             if(map.containsKey(cal[i]))
             pal = map.get(cal[i]);
             // out.println(last+" "+pal);
              ans= ans + pal;
             // out.println(pal);
              map.put(cal[i],pal+1);
              l[arr[i]].add(i);
          } 
          
          out.println(ans);
          




      

    }
   
    
    public int value (int seg[], int left , int right ,int index, int l, int r)
    {
            
            if(left>right)
            {
              return -100000000;
            }
            if(right<l||left>r)
                return -100000000;
            if(left>=l&&right<=r)
                return seg[index];
            int mid = left+(right-left)/2;
            int val = value(seg,left,mid,2*index+1,l,r);
            int val2 = value(seg,mid+1,right,2*index+2,l,r);
            return Math.max(val,val2);

    }
   
    public int gcd(int a , int b )
    {
      if(a<b)
      {
        int t =a;
        a=b;
        b=t;
      }
      if(a%b==0)
        return b ;
      return gcd(b,a%b);
    }
    public long pow(long n , long p,long m)
    {
         if(p==0)
            return 1;
        long val = pow(n,p/2,m);;
        val= (val*val)%m;
        if(p%2==0)
            return val;
        else
            return (val*n)%m;
    }
    
    
    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    public static void main(String[] args) {
        new Thread(null, new realfast(), "", 128 * (1L << 20)).start();
    }
 
    private static final boolean ONLINE_JUDGE = System.getProperty("ONLINE_JUDGE") != null;
    private BufferedReader reader;
    private StringTokenizer tokenizer;
    private PrintWriter out;
 
    @Override
    public void run() {
        try {
            if (ONLINE_JUDGE || !new File("input.txt").exists()) {
                reader = new BufferedReader(new InputStreamReader(System.in));
                out = new PrintWriter(System.out);
            } else {
                reader = new BufferedReader(new FileReader("input.txt"));
                out = new PrintWriter("output.txt");
            }
            solve();
        } catch (IOException e) {
            throw new RuntimeException(e);
        } finally {
            try {
                reader.close();
            } catch (IOException e) {
                // nothing
            }
            out.close();
        }
    }
 
    private String readString() throws IOException {
        while (tokenizer == null || !tokenizer.hasMoreTokens()) {
            tokenizer = new StringTokenizer(reader.readLine());
        }
        return tokenizer.nextToken();
    }
 
    @SuppressWarnings("unused")
    private int readInt() throws IOException {
        return Integer.parseInt(readString());
    }
 
    @SuppressWarnings("unused")
    private long readLong() throws IOException {
        return Long.parseLong(readString());
    }
 
    @SuppressWarnings("unused")
    private double readDouble() throws IOException {
        return Double.parseDouble(readString());
    }
}
class edge implements Comparable<edge>{
    int val ;
    int color;
    
    edge(int u, int v)
    {
       this.val=u;
       this.color=v;
    }
    public int compareTo(edge e)
    {
        return this.val-e.val;
    }
}