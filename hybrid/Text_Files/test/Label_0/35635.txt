//created by Whiplash99
import java.io.*;
import java.util.*;
public class G
{
    private static int tin[], tout[], timer=1;
    private static ArrayDeque<Integer> edge[];
    static class Segtree  //max query with range updates
    {
        int N, max[], delta[];
        Segtree(int NN){N=NN;max=new int[4*N];delta=new int[4*N];}
        int func(int a, int b){return Math.max(a,b);}
        void prop(int i){delta[2*i+1]+=delta[i]; delta[2*i+2]+=delta[i]; delta[i]=0;}
        void fix(int i){max[i]=func(max[2*i+1]+delta[2*i+1],max[2*i+2]+delta[2*i+2]);}
        void update(int a, int b, int val){update(0,0,N-1,a,b,val);}
        void update(int i, int l, int r, int a, int b, int val)
        {
            if(r<a||b<l) return;
            if(a<=l&&r<=b) { delta[i]+=val; return;}

            prop(i);
            int m=(l+r)/2;
            update(2*i+1,l,m,a,b,val);
            update(2*i+2,m+1,r,a,b,val);
            fix(i);
        }
        int query(){return max[0]+delta[0];}
    }
    private static void DFS(int u)
    {
        ArrayDeque<Integer> stack=new ArrayDeque<>();
        stack.push(u);

        while (!stack.isEmpty())
        {
            u=stack.peek();
            if(tin[u]==0) tin[u]=timer++;
            else
            {
                stack.pop();
                tout[u]=timer-1;
                continue;
            }
            while (!edge[u].isEmpty())
            {
                int v=edge[u].poll();
                if(tin[v]==0) stack.push(v);
            }
        }
    }
    public static void main(String[] args) throws IOException
    {
        Reader r=new Reader();

        int i,N;
        
        N=r.nextInt();
        int K=r.nextInt();
        
        int a[]=new int[N+5];
        for(i=0;i<N;i++) a[i]=r.nextInt();
        a[N]=N+5;

        edge=new ArrayDeque[N+5];
        tin=new int[N+5]; tout=new int[N+5];
        for(i=0;i<=N;i++) edge[i]=new ArrayDeque<>();

        ArrayDeque<Integer> stack=new ArrayDeque<>();
        for(i=0;i<=N;i++)
        {
            while (!stack.isEmpty()&&a[i]>a[stack.peek()])
            {
                edge[i].add(stack.peek());
                edge[stack.pop()].add(i);
            }
            stack.push(i);
        }

        DFS(N);
        Segtree ST=new Segtree(tout[N]+1);
        StringBuilder sb=new StringBuilder();

        for(i=0;i<K;i++) ST.update(tin[i], tout[i],1);
        sb.append(ST.query()).append(" ");

        for(i=K;i<N;i++)
        {
            ST.update(tin[i-K], tout[i-K], -1);
            ST.update(tin[i], tout[i], 1);
            sb.append(ST.query()).append(" ");
        }

        System.out.println(sb);
    }
    static class Reader 
    { 
        final private int BUFFER_SIZE = 1 << 16;private DataInputStream din;private byte[] buffer;private int bufferPointer, bytesRead;
        public Reader(){din=new DataInputStream(System.in);buffer=new byte[BUFFER_SIZE];bufferPointer=bytesRead=0;
        }public Reader(String file_name) throws IOException{din=new DataInputStream(new FileInputStream(file_name));buffer=new byte[BUFFER_SIZE];bufferPointer=bytesRead=0;
        }public String readLine() throws IOException{byte[] buf=new byte[64];int cnt=0,c;while((c=read())!=-1){if(c=='\n')break;buf[cnt++]=(byte)c;}return new String(buf,0,cnt);
        }public int nextInt() throws IOException{int ret=0;byte c=read();while(c<=' ')c=read();boolean neg=(c=='-');if(neg)c=read();do{ret=ret*10+c-'0';}while((c=read())>='0'&&c<='9');if(neg)return -ret;return ret;
        }public long nextLong() throws IOException{long ret=0;byte c=read();while(c<=' ')c=read();boolean neg=(c=='-');if(neg)c=read();do{ret=ret*10+c-'0';}while((c=read())>='0'&&c<='9');if(neg)return -ret;return ret;
        }public double nextDouble() throws IOException{double ret=0,div=1;byte c=read();while(c<=' ')c=read();boolean neg=(c=='-');if(neg)c = read();do {ret=ret*10+c-'0';}while((c=read())>='0'&&c<='9');if(c=='.')while((c=read())>='0'&&c<='9')ret+=(c-'0')/(div*=10);if(neg)return -ret;return ret;
        }private void fillBuffer() throws IOException{bytesRead=din.read(buffer,bufferPointer=0,BUFFER_SIZE);if(bytesRead==-1)buffer[0]=-1;
        }private byte read() throws IOException{if(bufferPointer==bytesRead)fillBuffer();return buffer[bufferPointer++];
        }public void close() throws IOException{if(din==null) return;din.close();}
    }
}