import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.Map;
import java.util.Objects;

public class D478Div2
{
    public static void main(String[] args)
    {
        new D478Div2(System.in, System.out);
    }

    private static class Solver implements Runnable
    {
        int n, a, b;
        Point[] velocities;
        long[] p;
        InputReader in;
        PrintWriter out;

        void solve() throws IOException
        {
            n = in.nextInt();
            a = in.nextInt();
            b = in.nextInt();
            velocities = new Point[n];
            p = new long[n];

            for (int i = 0; i < n; i++)
            {
                in.nextInt();
                velocities[i] = new Point(in.nextInt(), in.nextInt());
                p[i] = a * velocities[i].x - velocities[i].y;
            }

            Map<Long, Integer> map = new HashMap<>();
            Map<Point, Integer> map2 = new HashMap<>();

            for (int i = 0; i < n; i++)
            {
                Integer cnt = map.get(p[i]);

                if (cnt == null)
                    map.put(p[i], 1);
                else
                    map.put(p[i], cnt + 1);

                Point pt = new Point(p[i], velocities[i].x);

                cnt = map2.get(pt);

                if (cnt == null)
                    map2.put(pt, 1);
                else
                    map2.put(pt, cnt + 1);
            }

/*            System.out.println("map :");
            for (Map.Entry<Long, Integer> entry : map.entrySet())
                System.out.println(entry);*/

            long ans = 0;

            for (int i = 0; i < n; i++)
            {
                ans += map.getOrDefault(p[i], 0);
                ans -= map2.getOrDefault(new Point(p[i], velocities[i].x), 0);
            }

            out.println(ans);
        }

        class Point
        {
            long x, y;

            Point(long x, long y)
            {
                this.x = x;
                this.y = y;
            }

            @Override
            public boolean equals(Object obj)
            {
                Point pt = (Point) obj;

                return x == pt.x && y == pt.y;
            }

            @Override
            public int hashCode()
            {
                return Objects.hash(x, y);
            }

        }

        Solver(InputReader in, PrintWriter out)
        {
            this.in = in;
            this.out = out;
        }

        @Override
        public void run()
        {
            try
            {
                solve();
            }
            catch (IOException e)
            {
                e.printStackTrace();
            }
        }

    }

    private static class InputReader
    {
        private InputStream stream;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;

        int read()
        {
            if (numChars == -1)
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
                if (numChars <= 0)
                    return -1;
            }

            return buf[curChar++];
        }

        int nextInt()
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

            int res = 0;

            do
            {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();

                res *= 10;
                res += c & 15;

                c = read();
            } while (!isSpaceChar(c));

            return res * sgn;
        }

        boolean isSpaceChar(int c)
        {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        void close()
        {
            try
            {
                stream.close();
            }
            catch (IOException e)
            {
                e.printStackTrace();
            }
        }

        InputReader(InputStream stream)
        {
            this.stream = stream;
        }

    }

    private D478Div2(InputStream inputStream, OutputStream outputStream)
    {
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        Thread thread = new Thread(null, new Solver(in, out), "Solver", 1 << 29);

        try
        {
            thread.start();
            thread.join();
        }
        catch (InterruptedException e)
        {
            e.printStackTrace();
        }

        in.close();
        out.flush();
        out.close();
    }

}
