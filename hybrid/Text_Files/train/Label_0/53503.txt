import java.util.*;
import java.io.*;
import java.math.*;
import java.text.*;
public class Main
{
    static class Reader 
    { 
        private InputStream mIs;private byte[] buf = new byte[1024];private int curChar,numChars;public Reader() { this(System.in); }public Reader(InputStream is) { mIs = is;} 
        public int read() {if (numChars == -1) throw new InputMismatchException();if (curChar >= numChars) {curChar = 0;try { numChars = mIs.read(buf);} catch (IOException e) { throw new InputMismatchException();}if (numChars <= 0) return -1; }return buf[curChar++];} 
        public String nextLine(){int c = read();while (isSpaceChar(c)) c = read();StringBuilder res = new StringBuilder();do {res.appendCodePoint(c);c = read();}while (!isEndOfLine(c));return res.toString() ;} 
        public String s(){int c = read();while (isSpaceChar(c)) c = read();StringBuilder res = new StringBuilder();do {res.appendCodePoint(c);c = read();}while (!isSpaceChar(c));return res.toString();} 
        public long l(){int c = read();while (isSpaceChar(c)) c = read();int sgn = 1;if (c == '-') { sgn = -1 ; c = read() ; }long res = 0; do{ if (c < '0' || c > '9') throw new InputMismatchException();res *= 10 ; res += c - '0' ; c = read();}while(!isSpaceChar(c));return res * sgn;} 
        public int i(){int c = read() ;while (isSpaceChar(c)) c = read();int sgn = 1;if (c == '-') { sgn = -1 ; c = read() ; }int res = 0;do{if (c < '0' || c > '9') throw new InputMismatchException();res *= 10 ; res += c - '0' ; c = read() ;}while(!isSpaceChar(c));return res * sgn;} 
        public double d() throws IOException {return Double.parseDouble(s()) ;}
        public boolean isSpaceChar(int c) { return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1; } 
        public boolean isEndOfLine(int c) { return c == '\n' || c == '\r' || c == -1; } 
        public int[] arr(int n){int[] ret = new int[n];for (int i = 0; i < n; i++) {ret[i] = i();}return ret;}
    }
    
    
 
           //       |----|       /\      |    |   -----   |
           //       |   /       /  \     |    |     |     |
           //       |--/       /----\    |----|     |     |
           //       |   \     /      \   |    |     |     |
           //       |    \   /        \  |    |   -----   -------


    static int n,m;
    public static void main(String args[])throws IOException
    {
        PrintWriter out=new PrintWriter(System.out);
        Reader sc=new Reader();
        n=sc.i();m=sc.i();
        ArrayList<Integer> adj[]=new ArrayList[1001];
        HashMap<Integer,Integer> hm[]=new HashMap[1001];
        
        for(int i=0;i<1001;i++)
        {
            adj[i]=new ArrayList();
            hm[i]=new HashMap();
        }
        for(int i=0;i<n;i++)
        {
            int a=sc.i();
            int b=sc.i();
            adj[b].add(a);
            hm[b].put(a,hm[b].getOrDefault(a,0)+1);
        }
        int count[]=new int[1001];
        int q[][]=new int[m][2];
        for(int i=0;i<m;i++)
        {
            int a=sc.i();
            int b=sc.i();
            q[i][0]=a;
            q[i][1]=b;
            count[b]++;
        }
        int ans=0;
        for(int i=0;i<1001;i++)
        ans+=Math.min(count[i],adj[i].size());
        int ans1=0;
        for(int i=0;i<m;i++)
        {
            int a=q[i][0];
            int b=q[i][1];
            if(hm[b].get(a)==null);
            else
            {
                if(hm[b].get(a)==0)
                continue;
                ans1++;
                hm[b].put(a,hm[b].get(a)-1);
            }
        }
        out.println(ans+" "+ans1);
        out.flush();
    }
}