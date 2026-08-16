import java.math.BigDecimal;
import java.util.PriorityQueue;
import java.util.Scanner;

class Stuff implements Comparable<Stuff> {
    int v;
    int w;
    double performance;

    Stuff(int v, int w) {
        this.v = v;
        this.w = w;
        performance = 1.0 * v / w;
    }

    public int compareTo(Stuff s) {
        if(performance < s.performance) return 1;
        if(performance > s.performance) return -1;
        return 0;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
 
        int n = sc.nextInt();
        int w = sc.nextInt();
        PriorityQueue<Stuff> que = new PriorityQueue<>();
        for(int i = 0; i < n; i++) {
            int vi = sc.nextInt();
            int wi = sc.nextInt();
            que.add(new Stuff(vi, wi));
        }

        double res = 0;
        while(w > 0 && !que.isEmpty()) {
            Stuff s = que.poll();
            if(w >= s.w) {
                res += s.v;
                w -= s.w;
            }else {
                res += s.performance * w;
                w = 0;
            }
        }

        System.out.println(BigDecimal.valueOf(res).toPlainString());
 
        sc.close();
    }
}
