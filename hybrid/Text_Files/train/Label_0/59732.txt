import java.util.*;

public class Test {

    class P {
        double x;
        double y;

        P(double xx, double yy) {
            x = xx;
            y = yy;
        }

        P() {
        }

        P from(P o) {
            x = o.x;
            y = o.y;

            return this;
        }

        P to(P o) {
            x = o.x - x;
            y = o.y - y;

            return this;
        }

        double below(P o) {
            return x * o.y - y * o.x;
        }

        public String toString() {
            return "(" + x + "," + y + ")";
        }
    }

    class L {
        final P p;

        L(P p, double dx, double dy) {
            this.p = p;

            this.a = dy;
            this.b = -dx;
            this.c = -a * p.x - b * p.y;
        }

        L(P from, P to) {
            this(from, to.x - from.x, to.y - from.y);
        }

        P intersect(L o) {
            double d = a * o.b - b * o.a;
            return new P((b * o.c - c * o.b) / d,
                    (c * o.a - a * o.c) / d);
        }

        // ax + by + c = 0;
        double a, b, c;
    }

    int n, q;
    P[] p;
    double totalArea = 0;
    double[] areas;

    Scanner sca = new Scanner(System.in);

    void start() {
        n = sca.nextInt();
        q = sca.nextInt();

        p = new P[n];
        for (int i = 0; i < n; i++)
            p[i] = new P(sca.nextInt(), sca.nextInt());

        areas = new double[n + 1];
        for (int i = 1; i <= n; i++) {
            P p1 = p[i % n], p0 = p[i - 1];
            areas[i] = areas[i - 1] + (p1.x - p0.x) * (p1.y + p0.y);
        }
        totalArea = areas[n];

        for (int i = 0; i < q; i++) {
            P q = new P(sca.nextInt(), sca.nextInt());
            solve(q);
        }
    }

    void solve(P q) {
        double start = 0, end = Math.PI;
        double zero = 0;
        boolean found = false;
        double ans = -1;

        P e = new P(), e1 = new P();

        for (int it = 0; it < 60; it++) {
            double mid = (start + end) / 2;
            if (mid == start || mid == end) break;
            if (it == 0) mid = start;

            P d = new P(Math.cos(mid), Math.sin(mid));
            L l = new L(q, d.x, d.y);

            boolean reverse = false;
            if (d.below(e.from(p[0]).to(p[1])) < 0) {
                d.x = -d.x;
                d.y = -d.y;
                l = new L(q, d.x, d.y);
                reverse = true;
            }

            int ll = 0, rr = n - 1;
            while (ll < rr) {
                int i = (ll + rr + 1) / 2;
                if (d.below(e.from(p[i]).to(p[(i + 1) % n])) >= 0 &&
                        d.below(e.from(p[i]).to(p[1]).to(e1.from(p[0]).to(p[i]))) >= 0) ll = i;
                else rr = i - 1;
            }
            int maxId = (ll + 1) % n;

            ll = maxId + 1;
            rr = maxId + n - 1;
            while (ll < rr) {
                int i = (ll + rr) / 2;
                if (d.below(e.from(p[i % n]).to(p[(i + 1) % n])) < 0) ll = i + 1;
                else rr = i;
            }
            int minId = ll;


            ll = maxId;
            rr = minId;
            while (ll < rr) {
                int i = (ll + rr + 1) / 2;
                if (d.below(e.from(q).to(p[i % n])) > 0) ll = i;
                else rr = i - 1;
            }
            int last = (ll + n) % n;

            ll = minId;
            rr = maxId + n;
            while (ll < rr) {
                int i = (ll + rr) / 2;
                if (d.below(e.from(q).to(p[i % n])) <= 0) ll = i + 1;
                else rr = i;
            }
            int first = ll % n;

            L lFirst = new L(p[(first + n - 1) % n], p[first]);
            P inFirst = l.intersect(lFirst);

            L lLast = new L(p[last], p[(last + 1) % n]);
            P inLast = l.intersect(lLast);

            double res = 0;
            res += (p[first].x - inFirst.x) * (p[first].y + inFirst.y);
            if (last < first) res += totalArea;
            res += areas[last] - areas[first];
            res += (inLast.x - p[last].x) * (p[last].y + inLast.y);
            res += (inFirst.x - inLast.x) * (inFirst.y + inLast.y);

            if (reverse) {
                res = totalArea - res;
            }

            if (it == 0) {
                zero = res;
                continue;
            }

            if (Math.abs(totalArea - 2 * res) < totalArea * 1e-4) {
                found = true;
                ans = mid;
                break;
            }

            if ((res > 0.5 * totalArea) == (zero > 0.5 * totalArea)) start = mid;
            else end = mid;
        }
        System.out.println(found ? ans : -1);
    }

    public static void main(String[] args) {

        new Test().start();
    }
}
