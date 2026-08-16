import java.lang.reflect.Array;
import java.util.Scanner;
import java.io.*;
import java.util.*;
import java.math.*;
import java.lang.*;
import static java.lang.Math.*;
public class main implements Runnable {

    static ArrayList<pair> adj[];

    static void Check2(int n) {
        adj = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            adj[i] = new ArrayList<>();
        }

    }
    /*
    static void add(int i, int j) {
        adj[i].add(j);
        adj[j].add(i);
    }
*/


    public static void main(String[] args) {
        new Thread(null, new main(), "Check2", 1 << 26).start();// to increse stack size in java
    }
    static long mod = (long) (1e9 + 7);
    public void run() {
                                /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        //Scanner in=new Scanner(System.in);

        InputReader in = new InputReader(System.in);
        PrintWriter w = new PrintWriter(System.out);

        int n=in.nextInt();
        int m=in.nextInt();
        int a[][][]=new int[n+1][n+1][m+1];
        for(int i=0;i<m;i++){

            int d=in.nextInt();
            int b=in.nextInt();
            int c=in.nextInt();
            a[d][b][c]=1;
            a[b][d][c]=1;
        }
        HashSet <Integer> set=new HashSet<>();
        int v[][]=new int[n+1][n+1];
        ArrayList <Integer> list=new ArrayList<>();
        int v2[][][]=new int[n+1][n+1][m+1];
        for (int c=1;c<=m;c++) {
            for (int i = 1; i <= n; i++) {
                set.clear();
                list.clear();
                set.add(i);
                list.add(i);
                dfs(i,set,a,c,n,list);

                for(int ie=0;ie<list.size();ie++){

                    for(int j=0;j<list.size();j++){

                        if(v2[list.get(ie)][list.get(j)][c]==0) {
                            v[list.get(ie)][list.get(j)]++;
                            v2[list.get(ie)][list.get(j)][c]=1;
                        }
                    }

                }
            }


        }
        int q=in.nextInt();
        while (q-->0){
            int u=in.nextInt();
            int v3=in.nextInt();
            w.println(v[u][v3]);
        }


        w.close();
    }

    static void dfs(int i,HashSet <Integer> set,int a[][][],int color,int n,ArrayList <Integer> list){

        for(int j=1;j<=n;j++){
            if(a[i][j][color]==1&&!set.contains(j)){
                set.add(j);
                list.add(j);
                dfs(j,set,a,color,n,list);
            }
        }

    }
    static class pair {
            int y,color;
            pair(int a,int b){
                y=a;
                color=b;
            }
    }

    static long power(long x,long y){
        if(y==0)return 1%mod;
        if(y==1)return x%mod;


        long res=1;
        x=x%mod;
        while(y>0){


            if((y%2)!=0){
                res=(res*x)%mod;
            }


            y=y/2;
            x=(x*x)%mod;
        }


        return res;



    }


    static  int gcd(int a,int b){

        if(b==0)return a;
        return gcd(b,a%b);
    }

    static  void sev(int a[],int n){

        for(int i=2;i<=n;i++)a[i]=i;
        for(int i=2;i<=n;i++){

            if(a[i]!=0){
                for(int j=2*i;j<=n;){

                    a[j]=0;
                    j=j+i;
                }
            }

        }

    }



    static class node{

        int y;
        int val;

        node(int a,int b){

            y=a;
            val=b;

        }


    }

    static class InputReader
    {
        private InputStream stream;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;
        private SpaceCharFilter filter;

        public InputReader(InputStream stream)
        {
            this.stream = stream;
        }

        public int read()
        {
            if (numChars==-1)
                throw new InputMismatchException();

            if (curChar >= numChars)
            {
                curChar = 0;
                try
                {
                    numChars = stream.read(buf);
                }
                catch (IOException e)
                {
                    throw new InputMismatchException();
                }

                if(numChars <= 0)
                    return -1;
            }
            return buf[curChar++];
        }

        public String nextLine()
        {
            BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
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
        public int nextInt()
        {
            int c = read();

            while(isSpaceChar(c))
                c = read();

            int sgn = 1;

            if (c == '-')
            {
                sgn = -1;
                c = read();
            }

            int res = 0;
            do
            {
                if(c<'0'||c>'9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = read();
            }
            while (!isSpaceChar(c));

            return res * sgn;
        }

        public long nextLong()
        {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            int sgn = 1;
            if (c == '-')
            {
                sgn = -1;
                c = read();
            }
            long res = 0;

            do
            {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = read();
            }
            while (!isSpaceChar(c));
            return res * sgn;
        }

        public double nextDouble()
        {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            int sgn = 1;
            if (c == '-')
            {
                sgn = -1;
                c = read();
            }
            double res = 0;
            while (!isSpaceChar(c) && c != '.')
            {
                if (c == 'e' || c == 'E')
                    return res * Math.pow(10, nextInt());
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = read();
            }
            if (c == '.')
            {
                c = read();
                double m = 1;
                while (!isSpaceChar(c))
                {
                    if (c == 'e' || c == 'E')
                        return res * Math.pow(10, nextInt());
                    if (c < '0' || c > '9')
                        throw new InputMismatchException();
                    m /= 10;
                    res += (c - '0') * m;
                    c = read();
                }
            }
            return res * sgn;
        }

        public String readString()
        {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            StringBuilder res = new StringBuilder();
            do
            {
                res.appendCodePoint(c);
                c = read();
            }
            while (!isSpaceChar(c));

            return res.toString();
        }

        public boolean isSpaceChar(int c)
        {
            if (filter != null)
                return filter.isSpaceChar(c);
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        public String next()
        {
            return readString();
        }

        public interface SpaceCharFilter
        {
            public boolean isSpaceChar(int ch);
        }
    }







}