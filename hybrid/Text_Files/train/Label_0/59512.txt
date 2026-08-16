import java.io.*;
import java.util.*;
import java.math.*;
import java.lang.*;
 
import static java.lang.Math.*;
 
public class Solution implements Runnable 
{
	static class InputReader 
	{
		private InputStream stream;private byte[] buf = new byte[1024];
		private int curChar;
		private int numChars;
		private SpaceCharFilter filter;
		private BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        public InputReader(InputStream stream){this.stream = stream;}
		public int read(){if (numChars==-1) throw new InputMismatchException();if (curChar >= numChars){curChar = 0;try{numChars = stream.read(buf);}catch (IOException e){throw new InputMismatchException();	}if(numChars <= 0)return -1;}return buf[curChar++];}
     	public String nextLine(){String str = "";try{str = br.readLine();}catch (IOException e){e.printStackTrace();}return str;}
		public int nextInt(){int c = read();	while(isSpaceChar(c))c = read();	int sgn = 1; if (c == '-'){sgn = -1;c = read();	}int res = 0;do{if(c<'0'||c>'9') throw new InputMismatchException();res *= 10;res += c - '0';c = read();}while (!isSpaceChar(c));return res * sgn;}
        public long nextLong(){int c = read();while (isSpaceChar(c))c = read();int sgn = 1;if (c == '-'){sgn = -1;c = read();}long res = 0;do{if (c < '0' || c > '9')throw new InputMismatchException();res *= 10;res += c - '0';c = read();}while (!isSpaceChar(c));return res * sgn;}
		public double nextDouble(){int c = read();while (isSpaceChar(c))c = read();int sgn = 1;if (c == '-'){sgn = -1;c = read();}double res = 0;while (!isSpaceChar(c) && c != '.'){if (c == 'e' || c == 'E')return res * Math.pow(10, nextInt());if (c < '0' || c > '9')
		throw new InputMismatchException();res *= 10;res += c - '0';c = read();}if (c == '.'){c = read();double m = 1;while (!isSpaceChar(c)){if (c == 'e' || c == 'E')return res * Math.pow(10, nextInt());if (c < '0' || c > '9')throw new InputMismatchException();m /= 10;res += (c - '0') * m;c = read();}}return res * sgn;}
        public String readString(){int c = read();while (isSpaceChar(c))c = read();StringBuilder res = new StringBuilder();do{res.appendCodePoint(c);c = read();}while (!isSpaceChar(c));return res.toString();}
		public boolean isSpaceChar(int c){if (filter != null)return filter.isSpaceChar(c);return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;}
		public String next(){return readString();}
        public interface SpaceCharFilter{public boolean isSpaceChar(int ch);}
	}
		
	public static void main(String args[]) throws Exception{new Thread(null, new Solution(),"Main",1<<27).start();}

	public static long gcd(long a, long b) { 	if (a == 0) return b; return gcd(b % a, a);} 
  
	public static long findGCD(long arr[], int n) { 	long result = arr[0]; for (int i = 1; i < n; i++) result = gcd(arr[i], result);return result; }	 
	
	static void sortbycolomn(long arr[][], int col)
    { 
        Arrays.sort(arr, new Comparator<long[]>() { 
        @Override              
        public int compare(final long[] entry1,final long[] entry2) { 
            if (entry1[col] > entry2[col])return 1; 
            else return -1; 
        } 
        });   
    } 
	static int common(ArrayList<Integer>[] arr,int[] visited,int a,int b){
	    for(int i=0;i<arr[a].size();i++){
	        int x=arr[a].get(i);
	        if(visited[x]==0){
	            for(int j=0;j<arr[b].size();j++){
	                if(visited[arr[b].get(j)]==0 && arr[b].get(j)==x){
	                    visited[a]=1;
	                    visited[b]=1;
	                    return x;
	                }
	            }
	        }
	    }
	    return -1;
	}
	public void run()
    {
        InputReader in = new InputReader(System.in);
        PrintWriter w = new PrintWriter(System.out);
		
		int n=in.nextInt();
		ArrayList<Integer>[] arr=new ArrayList[n+1];
		for(int i=0;i<=n;i++)   arr[i]=new ArrayList<>();
		int a=0,b=0,c=0;
		for(int i=0;i<n-2;i++){
		    a=in.nextInt(); b=in.nextInt(); c=in.nextInt();
		    arr[a].add(b); arr[a].add(c);
		    arr[b].add(a); arr[b].add(c);
		    arr[c].add(a); arr[c].add(b);
		}
		
	/*	for(int i=1;i<=n;i++){
		    w.println(i);
		    for(int j=0;j<arr[i].size();j++)
		        w.print(arr[i].get(j)+" ");
		        w.println();
		}
		*/
		int[] visited=new int[n+1];
		int[] ans=new int[n];
		for(int i=1;i<=n;i++) if(arr[i].size()==2){ ans[0]=i; b=arr[i].get(0); c=arr[i].get(1); break;  }
		visited[ans[0]]=1;
		a=common(arr,visited,b,c);
		//w.println(a);
        int x=common(arr,visited,a,b);
        //w.println(x);
        if(x==-1){
            x=common(arr,visited,a,c);
            //w.println(x);
            ans[1]=b;
            ans[2]=c;
            ans[3]=a;
        }
        else{
            ans[1]=c;
            ans[2]=b;
            ans[3]=a;
        }
        for(int i=4;i<n;i++)
            ans[i]=common(arr,visited,ans[i-1],ans[i-2]);
        
        for(int i=0;i<n;i++)
            w.print(ans[i]+" ");
            w.println();
		
		
	    w.flush();
        w.close();
    }
}