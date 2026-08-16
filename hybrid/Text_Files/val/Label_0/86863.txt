
import java.util.Scanner;

public class CF_108A {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        String time = input.next();
        String[] times = {"01:10","02:20","03:30","04:40","05:50","10:01","11:11","12:21","13:31","14:41","15:51","20:02",
                          "21:12","22:22","23:32"};
        int i=0;
        while (i<times.length && time.compareTo(times[i])>=0)
            i++;
        if (i==times.length) System.out.println("00:00");
        else System.out.println(times[i]);
    }
}
