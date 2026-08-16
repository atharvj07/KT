import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;

/* abhi2601 */

public class Q1 implements Runnable{

    final static long mod = (long)1e9 + 7;

    class Pair{
        int l,r;
        Pair(int l,int r){
            this.l=l;
            this.r=r;
        }
    }

    public void run(){
        InputReader sc = new InputReader(System.in);
        PrintWriter w = new PrintWriter(System.out);
        int n=sc.nextInt();
        int k=sc.nextInt();
        int a[][]=new int[n+1][3];
        ArrayList<Integer>al=new ArrayList<>();
        for(int i=0;i<k;i++){
            int q=sc.nextInt();
            al.add(q);
            a[q][0]=1;
            /*if(q!=n && a[q+1][0]==1) a[q+1][1]=1;
            if(q!=1 && a[q-1][0]==1) a[q-1][2]=1;*/
        }
        HashSet<Integer>hs=new HashSet<>();
        for(int i=k-1;i>=0;i--){
            int q=al.get(i);
            hs.add(q);
            if(hs.contains(q+1)) a[q][2]=1;
            if(hs.contains(q-1)) a[q][1]=1;
        }
        int ans=0;
        for(int i=1;i<=n;i++){
            for(int j=0;j<3;j++){
                if(a[i][j]==0){
                    //w.println(i+" "+j);
                    ans++;
                }
            }
        }
        w.println(ans-2);
        w.close();
    }
    //static PrintWriter w;
    /*File in=new File("input.txt");
        File out=new File("output.txt");
        Scanner sc= null;
        try {
            sc = new Scanner(in);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        try {
            w=new PrintWriter(out);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }*/
    static class InputReader {

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

    public static void main(String args[]) throws Exception
    {
        new Thread(null, new Q1(),"q1",1<<26).start();
    }
}