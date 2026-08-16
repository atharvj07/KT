import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            int t = sc.nextInt();
            int h = sc.nextInt();
            int s = sc.nextInt();
            if (t == -1 && h == -1 && s == -1) {
                break;
            }
            int time=7200-(t*3600+h*60+s);
            int tt=time/3600;
            time-=tt*3600;
            int hh=time/60;
            time-=hh*60;
            int ss=time;
            System.out.println("0"+tt+":"+(hh/10==0?"0"+hh:hh)+":"+(ss/10==0?"0"+ss:ss));
            time=(7200-(t*3600+h*60+s))*3;
            tt=time/3600;
            time-=tt*3600;
            hh=time/60;
            time-=hh*60;
            ss=time;
            System.out.println("0"+tt+":"+(hh/10==0?"0"+hh:hh)+":"+(ss/10==0?"0"+ss:ss));       
        }
    }
}
