public class Main{
  public void run(java.io.InputStream in, java.io.PrintStream out){
    java.util.Scanner sc = new java.util.Scanner(in);
    double cx, cy, r, x1, y1, x2, y2;
    int q, i;
    double l1x, l1y, l2x, l2y, d, t1, t2, ax, ay, bx, by, a, bb, c, tmp;

    cx = sc.nextDouble(); cy = sc.nextDouble(); r = sc.nextDouble();
    q = sc.nextInt();

    for(i = 0;i < q;i++){
      x1 = sc.nextDouble(); y1 = sc.nextDouble();
      x2 = sc.nextDouble(); y2 = sc.nextDouble();

      l1x = x2 - x1; l1y = y2 - y1;
      l2x = x1 - cx; l2y = y1 - cy;
      a = l1x * l1x + l1y * l1y;
      bb = l1x * l2x + l1y * l2y;
      c = l2x * l2x + l2y * l2y - r * r;
      d = Math.sqrt(bb * bb - a * c);

      t1 = (-bb + d) / a;
      t2 = (-bb - d) / a;
      ax = x1 + t1 * l1x; ay = y1 + t1 * l1y;
      bx = x1 + t2 * l1x; by = y1 + t2 * l1y;

      if(ax > bx || (ax == bx && ay > by)){
        tmp = ax; ax = bx; bx = tmp;
        tmp = ay; ay = by; by = tmp;
      }

      out.println(ax + " " + ay + " " + bx + " " + by);
    }

    sc.close();
  }
  public static void main(String[] args){
    (new Main()).run(System.in, System.out);
  }
}