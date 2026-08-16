import java.io.*;
import java.util.StringTokenizer;

class Rectangle {
	double x[] = new double[2];
	double y[] = new double[2];

	Rectangle(double x1,double y1,double x2,double y2) { //左下:(x0,y0) 右上:(x1,y1)
		x[0] = x1;
		y[0] = y1;
		x[1] = x2;
		y[1] = y2;
	}

	boolean hasIntersection(Rectangle r) {
		if (this.x[0]<=r.x[0]&&r.x[0]<=this.x[1]) {
			return checkY(r);
		} else if (r.x[0]<=this.x[0]&&this.x[0]<=r.x[1]) {
			return checkY(r);
		}
		return false;
	}

	boolean checkY(Rectangle r) {
		if (this.y[0]<=r.y[0]&&r.y[0]<=this.y[1]) return true;
		else if (this.y[0]<=r.y[1]&&r.y[1]<=this.y[1]) return true;
		else if (r.y[0]<=this.y[0]&&this.y[1]<=r.y[1]) return true;
		else return false;
	}
}

class Main {
	public static void main(String args[]) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String buf;

		try {
			while ((buf = br.readLine())!=null) {
				StringTokenizer st = new StringTokenizer(buf);
				double x[] = new double[4];
				double y[] = new double[4];
				for (int i=0;i<4;i++) {
					x[i] = Double.parseDouble(st.nextToken());
					y[i] = Double.parseDouble(st.nextToken());
				}
				Rectangle r[] = new Rectangle[2];
				r[0] = new Rectangle(x[0],y[0],x[1],y[1]);
				r[1] = new Rectangle(x[2],y[2],x[3],y[3]);
				if (r[0].hasIntersection(r[1])) System.out.println("YES");
				else System.out.println("NO");
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}