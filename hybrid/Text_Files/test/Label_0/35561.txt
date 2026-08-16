import java.util.*;
import java.awt.Point;
import java.io.*;
import java.math.BigInteger;

public class DNotGood
{
    FastScanner in;
    PrintWriter out;
    
    public void solve() throws IOException
    {
        int n     = in.nextInt();       
        int mas[] = in.nextIntArray(n);
        
        int      countPosl    = 1;
        boolean foundDif     = false;
        double  dif          = -1;
        int      lastVal      = -1;
        int      lastValIndex = -1;
        
        int lastPosl = 0;
        
        for(int i = 0; i < n; i++)
        {
            if(mas[i] != -1)
            {
                if(lastValIndex > -1)
                {
                    if(foundDif)
                    {
                        if((int)(lastVal + (i - lastValIndex) * dif) != mas[i] || mas[i] - (i - lastPosl) * dif <= 0)
                        {
                            foundDif = false;
                            countPosl++;    
                            lastPosl = i;
                        }
                    }
                    else
                    {
                        dif = 1.0 * (mas[i] - lastVal) / (i - lastValIndex);
                        
                        if((int)dif != dif || mas[i] - (i - lastPosl) * dif <= 0)
                        {
                            countPosl++;
                            lastPosl = i;
                        }
                        else
                        {
                            foundDif = true;
                        }
                        
                    }
                }
                
                lastVal      = mas[i];
                lastValIndex = i;
            }
            else if(foundDif && lastValIndex != -1)
            {
                if(lastVal + (i - lastValIndex) * dif <= 0)
                {
                    countPosl++;
                    lastValIndex = -1;
                    lastPosl = i;
                    foundDif = false;
                }
            }
        }
        
        out.print(countPosl);
        
    }

    public void run()
    {
        try
        {
            in = new FastScanner();
            out = new PrintWriter(System.out);

            solve();

            out.close();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
    }

    class FastScanner
    {
        BufferedReader  br;
        StringTokenizer st;

        FastScanner()
        {

            br = new BufferedReader(new InputStreamReader(System.in));

        }

        FastScanner(File f)
        {
            try
            {
                br = new BufferedReader(new FileReader(f));
            }
            catch (FileNotFoundException e)
            {
                e.printStackTrace();
            }
        }

        String next()
        {
            while (st == null || !st.hasMoreTokens())
            {
                try
                {
                    st = new StringTokenizer(br.readLine());
                }
                catch (IOException e)
                {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt()
        {
            return Integer.parseInt(next());
        }

        long nextLong()
        {
            return Long.parseLong(next());
        }

        double nextDouble()
        {
            return Double.parseDouble(next());
        }

        int[] nextIntArray(int size)
        {
            int[] array = new int[size];

            for (int i = 0; i < size; i++)
            {
                array[i] = nextInt();
            }

            return array;
        }

        long[] nextLongArray(int size)
        {
            long[] array = new long[size];

            for (int i = 0; i < size; i++)
            {
                array[i] = nextLong();
            }

            return array;
        }

        BigInteger nextBigInteger()
        {
            return new BigInteger(next());
        }

        Point nextIntPoint()
        {
            int x = nextInt();
            int y = nextInt();
            return new Point(x, y);
        }

        Point[] nextIntPointArray(int size)
        {
            Point[] array = new Point[size];

            for (int index = 0; index < size; ++index)
            {
                array[index] = nextIntPoint();
            }

            return array;
        }

        List<Integer>[] readGraph(int vertexNumber, int edgeNumber, boolean undirected)
        {
            List<Integer>[] graph = new List[vertexNumber];

            for (int index = 0; index < vertexNumber; ++index)
            {
                graph[index] = new ArrayList<Integer>();
            }

            while (edgeNumber-- > 0)
            {
                int from = nextInt() - 1;
                int to = nextInt() - 1;

                graph[from].add(to);
                if (undirected)
                    graph[to].add(from);
            }

            return graph;
        }
    }

    public static void main(String[] arg)
    {
        new DNotGood().run();
    }
}