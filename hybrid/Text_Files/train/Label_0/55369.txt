import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner in=new Scanner (System.in);
        PrintWriter out=new PrintWriter(System.out);
        TreeSet<Integer> set=new TreeSet<>();
        int q=Integer.parseInt(in.next());
        for(int i=0;i<q;i++) {
            int odr=Integer.parseInt(in.next());

            switch(odr) {
            case 0:
            	int x0=Integer.parseInt(in.next());
            	if(!set.contains(x0)) set.add(x0);
            	out.println(set.size());
            	break;

            case 1:
            	int x1=Integer.parseInt(in.next());
            	out.println(set.contains(x1)? 1:0);
            	break;
            }

        }
        out.flush();
    }

}
