import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws Exception {
        PrintWriter out = new PrintWriter(System.out,true);
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(in.readLine());
        double vx = Integer.parseInt(st.nextToken());
        double vy = Integer.parseInt(st.nextToken());
        double vz = Integer.parseInt(st.nextToken());
        double EPS=1e-9;
        double x=a/2.0,y=m,z=0;
        double[] t = new double[5];
        while (y!=0) {
            t[0]=-x/vx;
            t[1]=(a-x)/vx;
            t[2]=(b-z)/vz;
            t[3]=-z/vz;
            t[4]=-y/vy;
            boolean br=false;
            double mm=1e18;
            int mi;
            for(int i = 0;i < 5;i++) {
                if (t[i]>EPS && t[i]<mm) {
                    mm=t[i];
                    mi=i;
                }
            }
            x+=mm*vx;
            y+=mm*vy;
            z+=mm*vz;
            if (Math.abs(mm-t[0])<EPS) vx*=-1;
            if (Math.abs(mm-t[1])<EPS) vx*=-1;
            if (Math.abs(mm-t[2])<EPS) vz*=-1;
            if (Math.abs(mm-t[3])<EPS) vz*=-1;
            if (Math.abs(mm-t[4])<EPS) br=true;
            if (br) {
                out.printf(Locale.US,"%.8f %.8f\n",x,z);
                return;
            }
        }
    }
}