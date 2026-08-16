import java.util.*;
import java.io.*;

public class Sol{
 
static class Pair implements Comparable<Pair>{
        int id;long value;
        public Pair(int id,long value) {
         
          this.id=id;this.value=value;
        }
        @Override
        public int compareTo(Pair p){return Long.compare(value,p.value);}
        //public int compareTo(Pair p){return id-p.id;}
       }


static void record(int n,int m,ArrayList<Integer> adj[],int p[],HashSet<Integer> hs[]){
   p[0]=0;boolean visited[]=new boolean[m];
   visited[0]=true;

   for(int u=1;u<m;u++){
       ArrayList<Integer> neighbours=new ArrayList<>();
       for(int i=0;i<n;i++){
         int v=u^1<<i;if(v<u)neighbours.add(v);
       } 
  
       if(neighbours.size()==1){
             int v=neighbours.get(0);
             for(int i:adj[p[v]]){if(visited[i])continue; p[u]=i;visited[i]=true;break;}
         }
   
       else{
          int v=neighbours.get(0);
          for(int i:adj[p[v]]){
             if(visited[i])continue;
             if(hs[i].contains(p[neighbours.get(1)])){p[u]=i;visited[i]=true;break;}
         }  
      }
 
   }

 }
public static void main(String []args){
 
//  ************     n==1  ***************** important test case

int times=ni();
while(times-->0){
  int n=ni();int m=1<<n;
  ArrayList<Integer> adj[]=new ArrayList[1<<n];
  int color[]=new int[1<<n];
  int p[]=new int[1<<n];
  HashSet<Integer> hs[]=new HashSet[1<<n];
  for(int i=0;i<m;i++){hs[i]=new HashSet<Integer>();adj[i]=new ArrayList<Integer>();}
  for(int i=0;i<(n<<n-1);i++){int u=ni();int v=ni();adj[u].add(v);adj[v].add(u);hs[u].add(v);hs[v].add(u);}
  
  record (n,m,adj,p,hs); 
  for(int i=0;i<m;i++){out.print(p[i]+" ");}out.println();
  
  if(good(n)){
      
      int[] r = new int[m];
			for(int i = 1;i < m;i++){
				if(Integer.bitCount(i) == 1){
					r[i] = Integer.numberOfTrailingZeros(i);
				}else{
					for(int j = 0;j < n;j++){
						if(i<<~j<0){
							r[i] = r[i^1<<j] ^ r[1<<j];
							break;
						}
					}
				}
			}
      for(int i=0;i<m;i++)color[p[i]]=r[i];
      for(int i=0;i<m;i++){out.print(color[i]+" ");}out.println();
   
  } 
  else out.println(-1);

}out.close();}

static boolean good(int n){
   if(n==1 || n==2 || n==4 || n==8 || n==16)return true;
   return false;
 }
//-----------------Utility--------------------------------------------

static long Comb[][]=new long[505][505];
static long p2[]=new long[505];
static long inv[]=new long[505];
static long factorial[]=new long[505];

static void precomp(){
 
inv[0]=1;factorial[0]=1l;
 
for(long i=1;i<505;i++){factorial[(int)i]=i*factorial[(int)i-1];factorial[(int)i]%=mod;}
 
for(int i=1;i<505;i++){ inv[i]=power(factorial[i],mod-2);}
 
for(int i=0;i<505;i++){
 
   for(int j=0;j<=i;j++){
     Comb[i][j]=(((factorial[i]*inv[j])%mod)*inv[i-j])%mod;
   }
 }
 
for(int i=0;i<505;i++)p2[i]=power(2,i);
 
}
static long gcd(long a,long b){if(b==0)return a; return gcd(b,a%b);}
static int Max=Integer.MAX_VALUE; static long mod=998244353;
static int v(char c){return (int)(c-'A');}
public static long power(long x, long y )
    {
        //0^0 = 1
        long res = 1L;
        x = x%mod;
        while(y > 0)
        {
            if((y&1)==1)
                res = (res*x)%mod;
            y >>= 1;
            x = (x*x)%mod;
        }
        return res;
    }
//--------------------------------------------------------------------
 
static InputStream inputStream = System.in;
static OutputStream outputStream = System.out;
static FastReader in=new FastReader(inputStream);
static PrintWriter out=new PrintWriter(outputStream);
 
static class FastReader 
{ 
  BufferedReader br; 
  StringTokenizer st; 
 
        FastReader(InputStream is) {
            br = new BufferedReader(new InputStreamReader(is));
        }
 
  public String next() 
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
 
  public int nextInt() 
  { 
      return Integer.parseInt(next()); 
  } 
 
  public long nextLong() 
  { 
      return Long.parseLong(next()); 
  } 
 
 public  double nextDouble() 
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
static int ni(){return in.nextInt();}
static long nl(){return in.nextLong();}
static String ns(){return in.nextLine();}

}