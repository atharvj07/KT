import java.util.*;
import java.io.*;

public class D
{

    Reader in;
    PrintWriter out;
    int i = 0, j = 0;
    void solve()
    {
        
        long a1 = in.nextLong(), b1 = in.nextLong(), a2 = in.nextLong(), b2 = in.nextLong();
        Choc c1 = new Choc(a1, b1);
        Choc c2 = new Choc(a2, b2);
        if (c1.getArea() != c2.getArea())
        {
            out.println("-1");
            return;
        }
        long time = 0;
        if (c1.get3() > c2.get3())
        {
            time += (c1.get3() - c2.get3());
            c1.reduce3(c1.get3() - c2.get3());
        }
        else if (c1.get3() < c2.get3())
        {
            time += (c2.get3() - c1.get3());
            c2.reduce3(c2.get3() - c1.get3());
        }
        if (c1.get2() > c2.get2())
        {
            time += (c1.get2() - c2.get2());
            c1.reduce2(c1.get2() - c2.get2());
        }
        else if (c1.get2() < c2.get2())
        {
            time += (c2.get2() - c1.get2());
            c2.reduce2(c2.get2() - c1.get2());
        }
        out.println(time);
        out.println(c1.getS());
        out.println(c2.getS());

        
        







        //END
        
    }
    class Choc
    {
        Dimension d1, d2;
        long total3, total2, totalArea;
        public Choc(long n1, long n2)
        {
            d1 = new Dimension(n1);
            d2 = new Dimension(n2);
            total3 = d1.getNum3() + d2.getNum3();
            total2 = d1.getNum2() + d2.getNum2();
            totalArea = d1.getNum() * d2.getNum();
        }
        public long get3()
        {
            return total3;
        }
        public long get2()
        {
            return total2;
        }
        public long getArea()
        {
            return totalArea;
        }
        public void reduce3(long n)
        {
            if (d1.getNum3() > 0)
            {
                if (d1.getNum3() < n)
                {
                    n -= d1.getNum3();
                    d1.reduce3(d1.getNum3());
                }
                else
                {
                    d1.reduce3(n);
                    n = 0;
                }
            }
            if (n > 0)
            {
                d2.reduce3(n);
                n = 0;
            }
            total3 = d1.getNum3() + d2.getNum3();
            total2 = d1.getNum2() + d2.getNum2();

        }
        public void reduce2(long n)
        {
            if (d1.getNum2() > 0)
            {
                if (d1.getNum2() < n)
                {
                    n -= d1.getNum2();
                    d1.reduce2(d1.getNum2());
                }
                else
                {
                    d1.reduce2(n);
                    n = 0;
                }
            }
            if (n > 0)
            {
                d2.reduce2(n);
                n = 0;
            }
            total2 = d1.getNum2() + d2.getNum2();
        }
        public String getS()
        {
            return ("" + d1.getD() + " " + d2.getD());
        }

    }
    class Dimension
    {
        long num3, num2, num;
        public Dimension(long n)
        {
            num3 = 0;
            num2 = 0;
            num = n;
            while (num % 3 == 0)
            {
                num3++;
                num /= 3;
            }
            while (num % 2 == 0)
            {
                num2++;
                num /= 2;
            }
        }
        public long getNum3()
        {
            return num3;
        }
        public long getNum2()
        {
            return num2;
        }
        public long getNum()
        {
            return num;
        }
        public void reduce3(long n)
        {
            num3 -= n;
            num2 += n;
        }
        public void reduce2(long n)
        {
            num2 -= n;
        }
        public long getD()
        {
            long val = num * (long)(Math.pow(3, num3)) * (long)(Math.pow(2, num2));
            return val;
        }
    }

    void runIO()
    {
        in = new Reader();
        out = new PrintWriter(System.out, false);
        solve();
        out.close();
    }

    public static void main(String[] args)
    {
        new D().runIO();
    }


    // input/output
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

        

        public final String next()
        {
            int c = read();
            while (isSpaceChar(c))
            {
                c = read();
            }
            StringBuilder res = new StringBuilder();
            do
            {
                res.append((char) c);
                c = read();
            } while (!isSpaceChar(c));
            return res.toString();
        }

        private boolean isSpaceChar(int c)
        {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        public int nextInt()
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

        public long nextLong()
        {
            long ret = 0;
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

        public double nextDouble()
        {
            double ret = 0, div = 1;
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
            if (c == '.')
                while ((c = read()) >= '0' && c <= '9')
                    ret += (c - '0') / (div *= 10);
            if (neg)
                return -ret;
            return ret;
        }

        public int[] readIntArray(int size)
        {
            int[] arr = new int[size];
            for (int i = 0; i < size; i++)
                arr[i] = nextInt();
            return arr;
        }

        public long[] readLongArray(int size)
        {
            long[] arr = new long[size];
            for (int i = 0; i < size; i++)
                arr[i] = nextInt();
            return arr;
        }

        private void fillBuffer()
        {
            try
            {
                bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
            }
            catch (IOException e)
            {

            }
            
            if (bytesRead == -1)
                buffer[0] = -1;
        }

        private byte read()
        {
            if (bufferPointer == bytesRead)
                fillBuffer();
            return buffer[bufferPointer++];
        }
    }
}
