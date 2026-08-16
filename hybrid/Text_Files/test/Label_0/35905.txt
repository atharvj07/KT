import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.*;
import java.lang.Math.*;
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        int n = in.nextInt();
        long x = in.nextLong();
        long[]candies = new long[n];
        long s=0;long total;long over;
        candies[0] = in.nextLong();
        for(int i=1;i<n;i++){
            candies[i] = in.nextLong();
            total= candies[i]+candies[i-1];
            over = total-x;
            if (over>0){
                long remove = Math.min(candies[i],over);
                candies[i]-=remove;
                over-=remove;
                s+=remove;
            }
            if (over>0){
                long remove = Math.min(candies[i-1],over);
                candies[i-1]-=remove;
                over-=remove;
                s+=remove;
            }
        }
        System.out.println(s);

    }
}