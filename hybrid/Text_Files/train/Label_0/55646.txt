
import java.awt.Point;
import java.io.*;
import java.util.Arrays;
public class p84c {
    public static void main(String[] args) throws Exception {
        p84cc in = new p84cc(System.in);
        int n = in.nextLong();
        circle[] circles = new circle[n];
        for (int i = 0; i < circles.length; i++) {
            circles[i]  = new circle(in.nextLong(), in.nextLong(), i);
        }
        Arrays.sort(circles);
        int m = in.nextLong();
        hit[] hits = new hit[m];
        
        for (int i = 0; i < m; i++) {
            hits[i] = new hit(in.nextLong(), in.nextLong(), i);
        }
        Arrays.sort(hits);
        int [] result  = new int[n];
        Arrays.fill(result, 999999);
        int j = 0;
        for (int i = 0; i < hits.length;) {
            int temp = j;
            for (; j < result.length;) {
                double distance = Math.sqrt(hits[i].y*hits[i].y  + (hits[i].x-circles[j].center)*(hits[i].x-circles[j].center) );
                if(distance<=circles[j].radius) {
                        result[circles[j].index] = Math.min(result[circles[j].index], hits[i].index);
                        j++;
                } else break;
            }
            if(j == result.length) {
                j--;
                i++;
                continue;
            }
            if(hits[i].x<=(circles[j].center+circles[j].radius)) {
                i++;
                
                j = temp;
                
            } else {
                j++;
            }
            
        }
        int count = 0;
        for (int i = 0; i < result.length; i++) {
            if(result[i]!= 999999)
                count++;
        }
        System.out.println(count);
        for (int i = 0; i < result.length; i++) {
            if(result[i] == 999999 )
                System.out.print("-1 ");
            else System.out.print((result[i]+1)+" ");
        }
    }
}
class circle implements Comparable<circle>{
    int center;
    int radius;
    int index;
    public circle(int a , int b , int in) {
        center = a;
        radius = b;
        index = in;
    }
    public int compareTo(circle o) {
        return center - o.center;
    }
    
}
class hit extends Point implements Comparable<hit> {
    int index;
    public hit (int x , int y , int in) {
        super(x,y);
        index = in;
    }
    public int compareTo(hit o) {
        if(x!=o.x) {
            return x-o.x;
        }
        if(y!=o.y) {
            return y-o.y;
        }
        return index - o.index;
    }
    
}
//BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
class p84cc {
    final private int BUFFER_SIZE = 1 << 16;
    private DataInputStream din;
    private byte[] buffer;
    private int bufferPointer, bytesRead;

    public p84cc(InputStream in) {
        din = new DataInputStream(in);
        buffer = new byte[BUFFER_SIZE];
        bufferPointer = bytesRead = 0;
    }

    public int nextLong() throws Exception {
        int ret = 0;
        byte c = read();
        
        while (c <= ' ')
            c = read();
        boolean neg = c == '-';
        if (neg)
            c = read();
        do {
            ret = ret * 10 + c - '0';
            c = read();
        } while (c > ' ');
        if (neg)
            return -ret;
        return ret;
    }
    
    public char nextChar() throws Exception {
        char ret = ' ';
        byte c = read();
        
        while (c <= ' ')
            c = read();
        
        ret = (char)c;
            
        
        return ret;
    }
    public String nextString() throws Exception {
        StringBuffer ret = new StringBuffer();
        byte c = read();
        
        while (c <= ' ')
            c = read();
        do {
            ret = ret.append((char)c);
            c = read();
        } while (c > ' ');
        
        return ret.toString();
    }
    
    private void fillBuffer() throws Exception {
        bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
        if (bytesRead == -1)
            buffer[0] = -1;
    }

    private byte read() throws Exception {
        if (bufferPointer == bytesRead)
            fillBuffer();
        return buffer[bufferPointer++];
    }
}