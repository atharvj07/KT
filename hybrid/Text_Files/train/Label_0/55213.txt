import java.util.*;
import java.io.*;
public class Main
{
	static class Reader
	{
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
			din = new DataInputStream(new FileInputStream(file_name));
			buffer = new byte[BUFFER_SIZE];
			bufferPointer = bytesRead = 0;
		}

		public String readLine() throws IOException
		{
			byte[] buf = new byte[201]; // line length
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
          static ArrayDeque<Integer> node=new ArrayDeque<>();static boolean visit[];
          static void dfs1(int u){
           visit[u]=true;
           for(int v:ja[u]){
            if(!visit[v]){
             dfs1(v);
            }
           }node.addFirst(u);
          }
          static int gsz=0;
          static int comp[],sn=0;
          static void dfs2(int u,int n){
           ++gsz;visit[u]=true;comp[u]=n;sn=u;
           for(int v:jar[u]){
            if(!visit[v]){
             dfs2(v,n);
            }
           }
          }
          static boolean verf,vv[];
          static void verify(int u,int n){
           if(!verf)return;vv[u]=true;
           for(int v:ja[u]){
            if(vv[v])continue;
            if(comp[v]==n)verify(v,n);
            else{
              verf=false;return;
            }
           }
          }
         public static void main(String[] args) throws IOException
	{
	   Reader in=new Reader();PrintWriter out=new PrintWriter(System.out);
           int n=in.nextInt(),m=in.nextInt(),h=in.nextInt();
           make(n,m,h,in);
           visit=new boolean[n+1];vv=new boolean[n+1];comp=new int[n+1];
           for(int i=1;i<=n;i++){
            if(!visit[i])dfs1(i);
           }
           Arrays.fill(visit,false);
           int ans=n+1;
           int acomp=0;int N=0;
           o:while(!node.isEmpty()){
            int v=node.pop();
            while(visit[v]){
             if(!node.isEmpty())v=node.pop();
             else break o;
            }gsz=0;
            dfs2(v,++N);verf=true;//System.out.println(hs[0]);
            verify(sn,N);
            if(verf){
             if(gsz<ans){
              ans=gsz;acomp=N;
             }
            }
           } 
           out.println(ans);
           for(int i=1;i<=n;i++){
            if(comp[i]==acomp)out.print(i+" ");
           }
             out.flush();out.close();
	}
             static int ja[][],t[],from[],to[],c[];
             static int jar[][],cr[];
             static void make(int n,int m,int h,Reader in) throws IOException{
              ja=new int[n+1][];from=new int[2*m];to=new int[2*m];c=new int[n+1];t=new int[n+1];
              jar=new int[n+1][];cr=new int[n+1];int N=-1;
              for(int i=1;i<=n;i++)t[i]=in.nextInt();
              for(int i=0;i<m;i++){
               int u=in.nextInt(),v=in.nextInt();
               if((t[u]+1)%h==t[v]){
                c[u]++;from[++N]=u;to[N]=v;
                cr[v]++;
               }
               if((t[v]+1)%h==t[u]){
                c[v]++;from[++N]=v;to[N]=u;
                cr[u]++;
               }
              }
              for(int i=1;i<=n;i++){
               ja[i]=new int[c[i]];c[i]=0;
               jar[i]=new int[cr[i]];cr[i]=0;
              }
              for(int i=0;i<=N;i++){
               ja[from[i]][c[from[i]]++]=to[i];
               jar[to[i]][cr[to[i]]++]=from[i];
              }
             }
}