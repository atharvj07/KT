import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.*;


public class C 
{
    private static Comparator<int[]> cmp = new Comparator<int[]>() {
        
        @Override
        public int compare(int[] a, int[] b) {
            if(a[0] != b[0])
                return Integer.compare(a[0], b[0]);
            else
                return Integer.compare(a[1], b[1]);
        }
    };
    public static void main(String [] args) throws IOException
    {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter writer = new PrintWriter(System.out);
        
        int n = Integer.parseInt(reader.readLine());
        int [][] competitors = new int[n][];
        int [] maxXY = new int[10000+13];
        for(int i = 0 ; i < n ; i++)
        {
            StringTokenizer tokenizer = new StringTokenizer(reader.readLine());
            int s = Integer.parseInt(tokenizer.nextToken());
            int r = Integer.parseInt(tokenizer.nextToken());
            
            maxXY[s] = Math.max(maxXY[s], r);
            
            competitors[i] = new int[]{s, r};
        }
        
        
        int best = 0;
        int [][] convex = new int[n][];
        int sz = 0;
        for(int i = 10000 ; i >= 1 ; i--)
            if(maxXY[i] > best)
            {
                best = maxXY[i];
                while(sz > 1 && ccw(convex[sz-2], convex[sz-1], new int[] {i, maxXY[i]}) < 0)
                    sz--;
                convex[sz++] = new int[] {i, maxXY[i]};
            }
        
        Arrays.sort(convex, 0, sz, cmp);
        
        boolean [] good = new boolean[n];
        for(int i = 0 ; i < n ; i++)
            if(Arrays.binarySearch(convex, 0, sz, competitors[i], cmp) >= 0)
                good[i] = true;
        
        for(int i = 0 ; i < n ; i++)
            if(good[i])
                writer.print((i+1)+" ");
        writer.println();
        
        writer.flush();
        writer.close();
        
    }
    
    private static long ccw(int[] a, int[] b,int[] c)
    {
        long u1 = (a[0]-b[0])*1L*(a[1]-c[1]);
        
        long u2 = (a[1]-b[1])*1L*(a[0]-c[0]);
    
        return Long.compare(u1*b[1]*1L*c[0], u2*b[0]*1L*c[1]);  
    }
    
}
