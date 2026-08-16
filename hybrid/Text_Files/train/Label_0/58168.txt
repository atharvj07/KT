import java.util.*;
import java.io.*;


public class Main {

    public static void main(String args[]){
         FastScanner sc = new FastScanner();
         PrintWriter out = new PrintWriter(System.out);
         int H = sc.nextInt();
         int W = sc.nextInt();
         int[][] G = new int[10][10];
         for(int i=0;i<10;i++){
             for(int j=0;j<10;j++){
                 G[i][j] = sc.nextInt();
             }
         }
         HashMap<Integer,Integer> t = new HashMap<>(11);
         t.put(-1,0);
         t.put(0,(int)graph.dijkstra(G, 0, 1));
         t.put(1,(int)graph.dijkstra(G, 1, 1));
         t.put(2,(int)graph.dijkstra(G, 2, 1));
         t.put(3,(int)graph.dijkstra(G, 3, 1));
         t.put(4,(int)graph.dijkstra(G, 4, 1));
         t.put(5,(int)graph.dijkstra(G, 5, 1));
         t.put(6,(int)graph.dijkstra(G, 6, 1));
         t.put(7,(int)graph.dijkstra(G, 7, 1));
         t.put(8,(int)graph.dijkstra(G, 8, 1));
         t.put(9,(int)graph.dijkstra(G, 9, 1));

         int res = 0;
         for(int i=0;i<H;i++){
             for(int j=0;j<W;j++){
                 res += t.get(sc.nextInt());
             }
         }

        //  int[] dist = {1,2};

        //  PriorityQueue<Integer> manage = new PriorityQueue<>((x,y) -> dist[x]-dist[y]);

        //  manage.add(0);
        //  manage.add(1);
        //  out.println(manage.peek());
        //  dist[1] = -1;
        //  manage.remove(1);
        //  manage.add(1);
        //  out.println(manage.peek());


         out.println(res);
         out.flush();
        //  System.out.println(sum);
    }
}

class MyMath{
    public static long gcm(long a, long b){
        if(a<b) return gcm(b, a);

        if(a%b==0 || b==0) return b;

        long remainder = a%b;
        return gcm(b, remainder);
    }

    public static long summation(long a, long b){
        return b*(b+1)/2-a*(a-1)/2;
    }

    public static long factorial(long n){
        if(n<=1) return 1;
        else return factorial(n-1)*n;
    }

    public static long binomial(int a, int b){
        if(a<b) return 0;
        long[][] table = new long[a+1][a+1];
        for(int i=0;i<a+1;i++){
            table[0][a] =  0;
            table[i][0] = 1;
            table[i][i] = 1;
        }
        for(int i=1;i<a+1;i++){
            for(int j=1;j<a+1;j++){
                if(i<j) table[i][j] = 0;
                else{
                    table[i][j] = table[i-1][j-1] + table[i-1][j];
                }
            }
        }
        return table[a][b];

    }
}

class graph{
    public static long dijkstra(int[][] G, int s, int t){
        Integer[] dist = new Integer[G.length];
        PriorityQueue<Integer> manage = new PriorityQueue<>((x,y) -> dist[x]-dist[y]);
        HashSet<Integer> searched = new HashSet<>();
        Arrays.fill(dist,Integer.MAX_VALUE);
        dist[s] = 0;
        searched.add(s);
        for(int i=0;i<G.length;i++){
            if(G[s][i]!=-1){
                dist[i] = G[s][i];
                manage.add(i);
            }
        }
        while(manage.size()>0){
            int now = manage.poll();
            searched.add(now);
            for(int i=0;i<G.length;i++){
                if(G[now][i]!=-1){
                    if(!searched.contains(i)){
                        if(dist[i]==Integer.MAX_VALUE){
                            dist[i] = dist[now] + G[now][i];
                            manage.add(i);
                        }
                        else{
                            dist[i] = Math.min(dist[i],dist[now]+G[now][i]);
                            manage.remove(i);
                            manage.add(i);
                        }
                    }
                }
            }
            if(searched.contains(t)) break;
        }

        return dist[t];
    }
}


class FastScanner {
    private final InputStream in = System.in;
    private final byte[] buffer = new byte[1024];
    private int ptr = 0;
    private int buflen = 0;
    private boolean hasNextByte() {
        if (ptr < buflen) {
            return true;
        }else{
            ptr = 0;
            try {
                buflen = in.read(buffer);
            } catch (IOException e) {
                e.printStackTrace();
            }
            if (buflen <= 0) {
                return false;
            }
        }
        return true;
    }
    private int readByte() { if (hasNextByte()) return buffer[ptr++]; else return -1;}
    private static boolean isPrintableChar(int c) { return 33 <= c && c <= 126;}
    public boolean hasNext() { while(hasNextByte() && !isPrintableChar(buffer[ptr])) ptr++; return hasNextByte();}
    public String next() {
        if (!hasNext()) throw new NoSuchElementException();
        StringBuilder sb = new StringBuilder();
        int b = readByte();
        while(isPrintableChar(b)) {
            sb.appendCodePoint(b);
            b = readByte();
        }
        return sb.toString();
    }
    public long nextLong() {
        if (!hasNext()) throw new NoSuchElementException();
        long n = 0;
        boolean minus = false;
        int b = readByte();
        if (b == '-') {
            minus = true;
            b = readByte();
        }
        if (b < '0' || '9' < b) {
            throw new NumberFormatException();
        }
        while(true){
            if ('0' <= b && b <= '9') {
                n *= 10;
                n += b - '0';
            }else if(b == -1 || !isPrintableChar(b)){
                return minus ? -n : n;
            }else{
                throw new NumberFormatException();
            }
            b = readByte();
        }
    }
    public int nextInt() {
        long nl = nextLong();
        if (nl < Integer.MIN_VALUE || nl > Integer.MAX_VALUE) throw new NumberFormatException();
        return (int) nl;
    }
    public double nextDouble() { return Double.parseDouble(next());}
}