import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class cbr47c {

    public static void main(String[] args) throws IOException {
        new cbr47c().run();
    }

    private void run() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<Point> points = new ArrayList<Point>(n);
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            points.add(new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }
        convexHull(points);
        n = points.size();
        long r = 4;
        for (int i = 0; i < n; i++)
            if (i == 0)
                r += Math.max(Math.abs(points.get(i).x - points.get(n - 1).x),
                        Math.abs(points.get(i).y - points.get(n - 1).y));
            else
                r += Math.max(Math.abs(points.get(i).x - points.get(i - 1).x),
                        Math.abs(points.get(i).y - points.get(i - 1).y));
        PrintWriter pw = new PrintWriter(System.out);
        pw.println(r);
        pw.flush();
    }

    boolean cw(Point p1, Point p2, Point p3) {
        return p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y) < 0;
    }

    boolean ccw(Point p1, Point p2, Point p3) {
        return p1.x * (p2.y - p3.y) + p2.x * (p3.y - p1.y) + p3.x * (p1.y - p2.y) > 0;
    }

    void convexHull(List<Point> points) {
        int c = points.size();
        if (c == 1)
            return;
        Collections.sort(points);
        Point p1 = points.get(0), p2 = points.get(c - 1);
        ArrayList<Point> up = new ArrayList<Point>(c / 2);
        ArrayList<Point> down = new ArrayList<Point>(c / 2);
        up.add(p1);
        down.add(p1);
        for (int i = 1; i < c; i++) {
            if (i == c - 1 || cw(p1, points.get(i), p2)) {
                while (up.size() > 1 && !cw(up.get(up.size() - 2), up.get(up.size() - 1), points.get(i)))
                    up.remove(up.size() - 1);
                up.add(points.get(i));
            }
            if (i == c - 1 || ccw(p1, points.get(i), p2)) {
                while (down.size() > 1 && !ccw(down.get(down.size() - 2), down.get(down.size() - 1), points.get(i)))
                    down.remove(down.size() - 1);
                down.add(points.get(i));
            }
        }
        points.clear();
        for (int i = 0; i < up.size(); i++)
            points.add(up.get(i));
        for (int i = down.size() - 2; i > 0; i--)
            points.add(down.get(i));
    }

    class Point implements Comparable<Point> {
        long x, y;

        Point(long x, long y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return "x: " + x + " y: " + y;
        }

        @Override
        public int compareTo(Point point) {
            return (x < point.x || (x == point.x && y < point.y)) ? 1 : -1;
        }
    }

}