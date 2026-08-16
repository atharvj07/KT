import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Set;

public class Main {
    Scanner sc = new Scanner(System.in);

    void run() {
        for (;;) {
            // 1 行目 ビルの階数 n(整数)
            // 2 行目 1 つ目のビル a の 1 階から n 階までの壁の情報 a1 a2 ... an(すべて整数;半角空白区切り)
            // 各 ai は、i 階目の壁の情報を表し、意味は以下のとおりです。
            // 0:普通の壁
            // 1:はしご(i 階と i+1 階にまたがる)
            // 2:すべる壁
            // 3 行目 2 つ目のビル b の 1 階から n 階までの壁の情報 b1 b2 ... bn(すべて整数;半角空白区切り)
            int n = sc.nextInt();
            if (n == 0)
                break;
            int fs[][] = new int[2][n];
            for (int i = 0; i < n; i++) {
                fs[0][i] = sc.nextInt();
            }
            for (int i = 0; i < n; i++) {
                fs[1][i] = sc.nextInt();
            }
            Queue<Data> q = new LinkedList<Data>();
            int sfa = 0;
            int sfb = 0;
            if (fs[0][0] == 1)
                while (sfa + 1 < n && fs[0][sfa + 1] == 1)
                    sfa++;
            if (fs[1][0] == 1)
                while (sfb + 1 < n && fs[1][sfb + 1] == 1)
                    sfb++;
            q.add(new Data(0, sfa, 0));
            q.add(new Data(1, sfb, 0));
            Set<String> set = new HashSet<String>();
            boolean na = true;
            while (!q.isEmpty()) {
                Data d = q.poll();
                int b = d.b;
                int f = d.f;
                if (set.contains(b + " " + f))
                    continue;
                set.add(b + " " + f);
                int t = d.t;
                if (f == n - 1 && fs[b][n - 1] != 2) {
                    System.out.println(t);
                    na = false;
                    break;
                }
                int nb = b ^ 1;
                for (int i = 0; i < 3; i++) {
                    // 向かい側のビルへジャンプするときには、
                    // 同じ階・1つ上の階・2 つ上の階の、いずれかに飛び移ることができます。
                    if (i + f >= n)
                        continue;
                    int nf = f + i;
                    switch (fs[nb][i + f]) {
                    case 0:
                        q.add(new Data(nb, nf, t + 1));
                        break;
                    case 1:
                        while (nf + 1 < n && fs[nb][nf + 1] == 1)
                            nf++;
                        q.add(new Data(nb, nf, t + 1));
                        break;
                    case 2:
                        while (fs[nb][nf] == 2)
                            nf--;
                        q.add(new Data(nb, nf, t + 1));
                        break;
                    }
                }

            }
            if (na)
                System.out.println("NA");
        }
    }

    public static void main(String[] args) {
        new Main().run();
    }
}

class Data {
    int b;
    int f;
    int t;

    Data(int b, int f, int t) {
        this.b = b;
        this.f = f;
        this.t = t;
    }

    public String toString() {
        return b + " " + f + " " + t;
    }
}