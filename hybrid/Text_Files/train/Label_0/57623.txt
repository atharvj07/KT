
import java.awt.geom.AffineTransform;
import java.awt.geom.Point2D;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String[] tmpArray = br.readLine().split(" ");
		double px1 = Double.parseDouble(tmpArray[0]);
		double py1 = Double.parseDouble(tmpArray[1]);
		double px2 = Double.parseDouble(tmpArray[2]);
		double py2 = Double.parseDouble(tmpArray[3]);

		Point2D p1 = new Point2D.Double(px1, py1);
		Point2D p2 = new Point2D.Double(px2, py2);

		int q = Integer.parseInt(br.readLine());

		for(int i = 0; i < q; i++){
			tmpArray = br.readLine().split(" ");
			double x = Double.parseDouble(tmpArray[0]);
			double y = Double.parseDouble(tmpArray[1]);

			Point2D p = new Point2D.Double(x,y);

			int result = checkClockwise(p, p1, p2);

			switch (result) {
			case COUNTER_CLOCKWISE:
				System.out.println("COUNTER_CLOCKWISE");
				break;

			case CLOCKWISE:
				System.out.println("CLOCKWISE");
				break;

			case ONLINE_BACK:
				System.out.println("ONLINE_BACK");
				break;

			case ONLINE_FRONT:
				System.out.println("ONLINE_FRONT");
				break;

			case ON_SEGMENT:
				System.out.println("ON_SEGMENT");
				break;

			default:
				break;
			}
		}

	}

	static final int COUNTER_CLOCKWISE = 1;
	static final int CLOCKWISE = 2;
	static final int ONLINE_BACK = 3;
	static final int ONLINE_FRONT = 4;
	static final int ON_SEGMENT = 5;
	static final double EPS = 0.00000001;

	//p1,p2が作るベクトルに対してpの位置関係を調べる
	static int checkClockwise(Point2D p, Point2D p1, Point2D p2){
		if(p1.getX() > p2.getX() || (p1.getX() == p2.getX() && p1.getY() > p2.getY())){
			AffineTransform rotate = AffineTransform.getQuadrantRotateInstance(2);
			Point2D tmp = null;
			p = rotate.transform(p, tmp);
			p1 = rotate.transform(p1, tmp);
			p2 = rotate.transform(p2, tmp);

//			System.out.println(p);
		}

		double theta = Math.PI/2;

		//直線のなす角が90度ではないときはここで計算
		if(p1.getX() != p2.getX()){
			theta = Math.atan((p1.getY() - p2.getY()) / (p1.getX() - p2.getX()));
		}


		AffineTransform affine;// = AffineTransform.getTranslateInstance(p1.getX(), p1.getY());
//		affine.concatenate(AffineTransform.getRotateInstance(theta));
//		affine.concatenate(new AffineTransform(1, 0, 0, -1, 0, 0));
		affine = AffineTransform.getRotateInstance(-theta);
		affine.concatenate(AffineTransform.getTranslateInstance(-p1.getX(), -p1.getY()));

		Point2D pD = new Point2D.Double();
		pD = affine.transform(p, pD);
		Point2D p2D = new Point2D.Double();
		p2D = affine.transform(p2, p2D);

		if(pD.getY() > EPS){
			return COUNTER_CLOCKWISE;
		}
		else if(pD.getY() < -EPS){
			return CLOCKWISE;
		}
		else if(pD.getX() < 0){
			return ONLINE_BACK;
		}
		else if(pD.getX() > p2D.getX()){
			return ONLINE_FRONT;
		}
		else {
			return ON_SEGMENT;
		}

	}

}

