import java.util.*;
import java.io.*;
public class Main {
    //System.out.println("YES");
//System.out.println("NO");
 
//int n=sc.nextInt();
//int a[]=new int[n];
//for(int i=0;i<n;i++)
//a[i]=sc.nextInt();
 
//int n=sc.nextInt();
//long a[]=new long[n];
//for(int i=0;i<n;i++)
//a[i]=sc.nextLong();
 
//System.out.println();
 
//String str=sc.next();
//long n=sc.nextLong();
 
      static class Reader {
        final private int BUFFER_SIZE = 1 << 16;
        private DataInputStream din;
        private byte[] buffer;
        private int bufferPointer, bytesRead;
 
        public Reader()
        {
            din = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }
 
        public Reader(String file_name) throws IOException
        {
            din = new DataInputStream(
                new FileInputStream(file_name));
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }
 
        public String readLine() throws IOException
        {
            byte[] buf = new byte[64]; // line length
            int cnt = 0, c;
            while ((c = read()) != -1) {
                if (c == '\n') {
                    if (cnt != 0) {
                        break;
                    }
                    else {
                        continue;
                    }
                }
                buf[cnt++] = (byte)c;
            }
            return new String(buf, 0, cnt);
        }
 
        public int nextInt() throws IOException
        {
            int ret = 0;
            byte c = read();
            while (c <= ' ') {
                c = read();
            }
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
 
            if (neg)
                return -ret;
            return ret;
        }
 
        public long nextLong() throws IOException
        {
            long ret = 0;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            if (neg)
                return -ret;
            return ret;
        }
 
        public double nextDouble() throws IOException
        {
            double ret = 0, div = 1;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();
 
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
 
            if (c == '.') {
                while ((c = read()) >= '0' && c <= '9') {
                    ret += (c - '0') / (div *= 10);
                }
            }
 
            if (neg)
                return -ret;
            return ret;
        }
 
        private void fillBuffer() throws IOException
        {
            bytesRead = din.read(buffer, bufferPointer = 0,
                                 BUFFER_SIZE);
            if (bytesRead == -1)
                buffer[0] = -1;
        }
 
        private byte read() throws IOException
        {
            if (bufferPointer == bytesRead)
                fillBuffer();
            return buffer[bufferPointer++];
        }
 
        public void close() throws IOException
        {
            if (din == null)
                return;
            din.close();
        }
    }
    public static class Pair implements Comparable<Pair> {
        long x;
        int y;
        Pair(long a,int b) {
            x=a;
            y=b;
        }
       public   int compareTo(Pair p) {
            return Long.compare(x,p.x);
        }
    }
    public static void main(String[] args) throws IOException{
        //Scanner sc=new Scanner(System.in);
        Reader sc=new Reader();
        PrintWriter out=new PrintWriter(System.out);
        int t = sc.nextInt();
		while(t-->0) {
		    
		    int n=sc.nextInt();
		    Pair a[]=new Pair[n];
		    long sum=0;
		    for(int i=0;i<n;i++){
		    a[i]=new Pair(sc.nextLong(),i+1);
		    sum+=a[i].x;
		    }
		    Arrays.sort(a);
		    long count=1;
		    for(int i=n-2;i>=0;i--) {
		        sum=sum-a[i+1].x;
		        if(sum<a[i+1].x)
		        break;
		        else 
		        count++;
		    }
		    
		    ArrayList<Integer> al=new ArrayList<>();
		    for(int i=n-1;i>=n-count;i--)
		    al.add(a[i].y);
		    Collections.sort(al);
		    out.println(al.size());
		    for(int i=0;i<al.size();i++)
		    out.print(al.get(i)+" ");
		    out.println();
		    
		    
		}
		out.flush();
		out.close();
    }
}