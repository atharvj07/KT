import java.io.*;
import java.util.*;
class disc
{
	ArrayList<Integer> a=new ArrayList<Integer>();
	ArrayList<Integer> i=new ArrayList<Integer>();
}
class node
{
	ArrayList<Integer> adj=new ArrayList<Integer>();
	int value;
}
public class Main
{	
	static Set<Integer> ins=new HashSet<Integer>();
	static void dfs(int at, disc a)
	{
		if(!ins.contains(at))
		{
			a.i.add(graph[at].value);
			a.a.add(at);
			ins.add(at);
			Iterator<Integer> it=graph[at].adj.iterator();
			while(it.hasNext())
				dfs(it.next(),a);
		}
	}
	static node[] graph;
	public static void main(String[] args) throws IOException
	{
		Reader in=new Reader();
		int n=in.nextInt(),m=in.nextInt();
		graph=new node[n];
		int te,te1;
		for(int i=0; i<n; i++)
		{
			graph[i]=new node();
			graph[i].value=in.nextInt();
		}
		for(int i=0; i<m; i++)
		{
			te=in.nextInt();
			te1=in.nextInt();
			graph[te1].adj.add(te);
			graph[te].adj.add(te1);
		}
		ArrayList<disc> ho=new ArrayList<disc>();
		for(int i=0; i<n; i++)
		{
			if(!ins.contains(i))
			{
				disc te2=new disc();
				ho.add(te2);
				dfs(i, te2);
			}
		}
		graph=null;
		ins=null;
		Iterator<disc> itr=ho.iterator();
		ArrayList<Integer> all=new ArrayList<Integer>();
		long ans=0;
		int hosize=ho.size();
		if(hosize>1)
		{
			disc hola;
			while(itr.hasNext())
			{
				hola=itr.next();
				Collections.sort(hola.i);
				Iterator<Integer> itro=hola.i.iterator();
				ans+=itro.next();
				while(itro.hasNext())
					all.add(itro.next());
			}
			itr=null;
			ho=null;
			Collections.sort(all);
			if(all.size()<hosize-2)
				System.out.println("Impossible");
			else
			{
				Iterator<Integer> it=all.iterator();
				for(int i=0; i<hosize-2; i++)
					ans+=it.next();
				System.out.println(ans);
			}
		}
		else
			System.out.println(0);
	}
	static StringBuilder ans1=new StringBuilder();
	static String pr(String a, long b)
	{
		String c="";
		while(b>0)
		{
			if(b%2==1)
				c=c.concat(a);
			a=a.concat(a);
			b>>=1;
		}
		return c;
	}
	static class Reader
    {
        final private int BUFFER_SIZE = 1 << 16;
        private DataInputStream din;
        private byte[] buffer;
        private int bufferPointer, bytesRead;
        StringTokenizer st;
        public Reader()
        {
            din = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        } 
        public Reader(String file_name) throws IOException
        {
            din = new DataInputStream(new FileInputStream(file_name));
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }
        public String next() throws IOException
        {
        	while(st==null||!st.hasMoreElements())
        	{
        		try
        		{
        			st=new StringTokenizer(readLine());
        		}
        		catch(IOException e)
        		{
        			e.printStackTrace();
        		}
        	}
        	return
        			st.nextToken();
        }
        public String readLine() throws IOException
        {
            byte[] buf = new byte[255]; // line length
            int cnt = 0, c;
            while ((c = read()) != -1)
            {
                if (c == '\n')
                    break;
                buf[cnt++] = (byte) c;
            }
            return new String(buf, 0, cnt);
        }
        public int nextInt() throws IOException
        {
            int ret = 0;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do
            {
                ret = ret * 10 + c - '0';
            }  while ((c = read()) >= '0' && c <= '9');
 
            if (neg)
                return -ret;
            return ret;
        }
        public long nextlong() throws IOException
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
            }
            while ((c = read()) >= '0' && c <= '9');
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
            }
            while ((c = read()) >= '0' && c <= '9');
 
            if (c == '.')
            {
                while ((c = read()) >= '0' && c <= '9')
                {
                    ret += (c - '0') / (div *= 10);
                }
            }
 
            if (neg)
                return -ret;
            return ret;
        }
        private void fillBuffer() throws IOException
        {
            bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
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
}